#!/usr/bin/env python3
"""Gerador estático do site WeNorth Club.

Monta todas as páginas a partir de um template único (head SEO, menu, rodapé,
popup de captura e banner de cookies) e grava os arquivos na raiz do projeto.

Uso:  python3 _gerador/build.py
Esta pasta (_gerador) NÃO deve ser enviada ao servidor.

Conteúdo fictício: todo trecho criado sem base no descritivo é envolvido por
F(nota, html). Ele vira um comentário <!-- FICTÍCIO --> no HTML e entra no
relatório CONTEUDO-FICTICIO.md, para o copywriter reescrever.
"""
import hashlib
import html
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTES = os.path.join(RAIZ, "_gerador", "partes")
DOMINIO = "https://wenorthclub.com.br"
HOJE = "2026-11-18"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


import json as _json
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "partes", "imagens.json")) as _f:
    IMG = _json.load(_f)   # gerado por _gerador/imagens.py: nome -> {w, h}

SIZES_CARD = "(max-width:620px) 92vw, (max-width:980px) 46vw, 380px"
SIZES_PADRAO = "(max-width:900px) 92vw, 560px"


def otimizar_imgs(doc):
    """Ajusta toda <img> local: largura/altura reais, srcset leve, decoding assíncrono."""
    def troca(m):
        tag = m.group(0)
        src = re.search(r'src="/img/([a-z0-9-]+)\.webp"', tag)
        if not src:
            return tag
        nome = src.group(1)
        if nome not in IMG:
            raise SystemExit(f"imagem sem medidas em imagens.json: {nome}")
        d = IMG[nome]
        tag = re.sub(r'\s(width|height)="\d+"', "", tag)
        extra = f' width="{d["w"]}" height="{d["h"]}"'
        if nome + "-640" in IMG and "srcset" not in tag:
            extra += f' srcset="/img/{nome}-640.webp 640w, /img/{nome}.webp {d["w"]}w"'
            if "sizes=" not in tag:
                extra += f' sizes="{SIZES_PADRAO}"'
        if "decoding=" not in tag:
            extra += ' decoding="async"'
        return tag[:-1].rstrip("/").rstrip() + extra + ">"
    return re.sub(r"<img\b[^>]*>", troca, doc)


def ler(nome):
    with open(os.path.join(PARTES, nome), encoding="utf-8") as f:
        return f.read()


def gravar(caminho_rel, conteudo):
    destino = os.path.join(RAIZ, caminho_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)


# ---------------------------------------------------------------------------
# Registro de conteúdo fictício
# ---------------------------------------------------------------------------
FICTICIO = {}          # url -> [notas]
_pagina_atual = ["/"]


def F(nota, conteudo):
    """Marca um trecho como fictício (comentário no HTML + relatório)."""
    FICTICIO.setdefault(_pagina_atual[0], []).append(nota)
    return f"<!-- FICTÍCIO: {nota} -->{conteudo}<!-- /FICTÍCIO -->"


def em_pagina(url):
    _pagina_atual[0] = url


# ---------------------------------------------------------------------------
# Assets compartilhados
# ---------------------------------------------------------------------------
CSS_EXTRA = r"""
/* ================= PÁGINAS INTERNAS ================= */
.skip{position:absolute;left:-999px;top:8px;z-index:300;background:var(--lime);color:var(--ink);padding:10px 16px;border-radius:999px;font-weight:600;text-decoration:none}
.skip:focus{left:16px}
.top .main a[aria-current="page"]{color:var(--white)}
.top .main a[aria-current="page"]::after{transform:scaleX(1)}
.menu-btn{--ring:var(--lime);position:relative;isolation:isolate;display:inline-flex;align-items:center;justify-content:center;flex:none;width:48px;height:48px;padding:0;border:1.5px solid rgba(130,230,40,.75);border-radius:999px;background:rgba(130,230,40,.12);color:var(--white);font:600 15px/1 var(--body);cursor:pointer;-webkit-tap-highlight-color:transparent;touch-action:manipulation;transition:background .25s,color .25s,transform .2s,box-shadow .3s;animation:glow 2.6s 1.3s ease-in-out infinite}
.menu-btn::after{content:"";position:absolute;inset:-4px;border-radius:inherit;padding:2px;pointer-events:none;background:conic-gradient(from var(--a),transparent 0 68%,var(--ring) 92%,transparent 100%);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:spin 3.2s 1.6s linear infinite}
.menu-btn .ico{display:grid;gap:4px;width:20px}
.menu-btn .ico i{display:block;height:2px;border-radius:2px;background:var(--lime);transition:width .3s cubic-bezier(.2,.7,.2,1),background .25s}
.menu-btn .ico i:nth-child(1){width:20px}
.menu-btn .ico i:nth-child(2){width:13px;justify-self:end}
.menu-btn .ico i:nth-child(3){width:17px}
.menu-btn:hover,.menu-btn[aria-expanded="true"]{background:var(--lime);color:var(--ink);transform:translateY(-2px);box-shadow:0 10px 30px -10px rgba(130,230,40,.7);animation-play-state:paused}
.menu-btn:hover .ico i,.menu-btn[aria-expanded="true"] .ico i{background:var(--ink);width:20px}
.menu-btn:focus-visible{outline:2px solid var(--white);outline-offset:4px}
@media (hover:none){.menu-btn:hover{transform:none;background:rgba(130,230,40,.12);color:var(--white);box-shadow:none}.menu-btn:hover .ico i{background:var(--lime)}.menu-btn:hover .ico i:nth-child(2){width:13px}.menu-btn:hover .ico i:nth-child(3){width:17px}}
.top-right{display:flex;align-items:center;gap:14px}
@media (max-width:1180px){.top .main{display:none}}

/* menu lateral */
.drawer-bg{position:fixed;inset:0;z-index:90;background:rgba(0,0,0,.6);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);opacity:0;visibility:hidden;transition:opacity .35s,visibility 0s .35s}
.drawer-bg.is-open{opacity:1;visibility:visible;transition:opacity .35s}
.drawer{position:fixed;top:0;right:0;z-index:95;width:min(440px,100%);height:100vh;height:100dvh;display:flex;flex-direction:column;background:var(--ink);border-left:1px solid var(--line);transform:translateX(100%);visibility:hidden;transition:transform .45s cubic-bezier(.2,.7,.2,1),visibility 0s .45s}
.drawer.is-open{transform:none;visibility:visible;transition:transform .45s cubic-bezier(.2,.7,.2,1)}
.drawer-head{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:88px;padding:env(safe-area-inset-top,0px) max(24px,env(safe-area-inset-right,0px)) 0 24px;border-bottom:1px solid var(--line)}
.drawer-head img{height:28px;width:auto}
.drawer-close{all:unset;width:44px;height:44px;border-radius:50%;display:grid;place-items:center;border:1.5px solid var(--line);color:var(--aqua);font-size:24px;line-height:1;cursor:pointer}
.drawer-close:hover{border-color:var(--lime);color:var(--white)}
.drawer-close:focus-visible{outline:2px solid var(--lime);outline-offset:3px}
.drawer-body{flex:1;overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;padding:4px max(24px,env(safe-area-inset-right,0px)) 24px 24px}
.drawer summary{-webkit-tap-highlight-color:transparent;min-height:44px}
.drawer li a{min-height:44px;box-sizing:border-box}
.drawer details{border-bottom:1px solid var(--line)}
.drawer summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;padding:20px 0;font-family:var(--mono);font-weight:500;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--lime)}
.drawer summary::-webkit-details-marker{display:none}
.drawer summary::after{content:"+";font-size:16px;letter-spacing:0;color:var(--aqua-soft)}
.drawer details[open] summary::after{content:"–"}
.drawer ul{list-style:none;margin:-6px 0 18px;padding:0;display:grid;gap:2px}
.drawer li a{display:block;padding:9px 0;font-size:17px;font-weight:400;color:var(--aqua);text-decoration:none;transition:color .2s,padding-left .3s}
.drawer li a:hover{color:var(--white);padding-left:8px}
.drawer li a[aria-current="page"]{color:var(--lime)}
.drawer-foot{padding:20px 24px calc(20px + env(safe-area-inset-bottom,0px));border-top:1px solid var(--line);display:grid;gap:14px}
.drawer-foot .btn{justify-content:center}
.drawer-foot p{margin:0;font-size:14px;color:var(--aqua-soft)}
.drawer-foot a:not(.btn){color:var(--aqua)}
@media (max-width:520px){.top .hdr-cta{display:none}.top .wrap > a img{height:26px;width:auto}.top .wrap{height:72px}.top.scrolled .wrap{height:64px}}

.phero{position:relative;overflow:hidden;border-bottom:1px solid var(--line)}
.phero-img{position:absolute;inset:0;background:var(--img) 50% 50%/cover no-repeat;opacity:.5}
.phero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--ink) 0%,rgba(0,15,15,.88) 45%,rgba(0,15,15,.35) 100%),linear-gradient(0deg,var(--ink),rgba(0,15,15,0) 50%)}
.phero .wrap{position:relative;z-index:1;padding-block:clamp(48px,7vw,104px) clamp(48px,6vw,84px)}
.phero h1{font-size:clamp(36px,5vw,68px);line-height:1.02;color:var(--white);max-width:18ch}
.phero .lede{color:var(--aqua)}
.phero .ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:38px}
.phero .cap{position:absolute;right:max(20px,env(safe-area-inset-right,0px));bottom:16px;z-index:1}
.phero.plain::after{display:none}
.crumbs{margin:0 0 30px;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:6px 10px;font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--aqua-soft)}
.crumbs li+li::before{content:"/";margin-right:10px;color:var(--line)}
.crumbs a{text-decoration:none;color:var(--aqua-soft)}
.crumbs a:hover{color:var(--white)}
.crumbs [aria-current]{color:var(--lime)}

.prose{max-width:72ch}
.prose > :first-child{margin-top:0}
.prose h2{font-size:clamp(28px,3vw,40px);max-width:none;margin:64px 0 20px;color:var(--white)}
.prose h3{font-size:24px;margin:40px 0 14px;color:var(--white)}
.prose p{margin:0 0 24px;font-weight:400}
.prose ul,.prose ol{margin:0 0 24px;padding-left:1.2em;font-weight:400}
.prose li{margin-bottom:10px}
.prose li::marker{color:var(--lime)}
.prose a{color:var(--lime)}
.prose strong{color:var(--white);font-weight:500}
.paper .prose h2,.paper .prose h3,.paper .prose strong{color:var(--paper-ink)}
.paper .prose a{color:#0E5A3C}
.paper .prose li::marker{color:#0E5A3C}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(32px,6vw,80px);align-items:start}
@media (max-width:900px){.two{grid-template-columns:1fr}}

.figure-wide{margin:0;position:relative;border-radius:4px;overflow:hidden;background:var(--deep)}
.figure-wide img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover}
.figure-wide figcaption{position:absolute;left:12px;bottom:12px;font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;background:var(--ink);color:var(--aqua-soft);padding:6px 10px;border-radius:3px}
.figure-tall img{aspect-ratio:3/4;object-position:50% 20%}

.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:52px}
.cards.two-col{grid-template-columns:repeat(2,minmax(0,1fr))}
.card{position:relative;display:flex;flex-direction:column;background:var(--deep);border:1px solid var(--line);border-radius:4px;overflow:hidden;text-decoration:none;color:var(--aqua);transition:transform .45s cubic-bezier(.2,.7,.2,1),border-color .3s}
.card:hover{transform:translateY(-6px);border-color:rgba(130,230,40,.55)}
.card figure{margin:0;aspect-ratio:16/10;overflow:hidden;background:var(--ink)}
.card figure img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.card:hover figure img{transform:scale(1.06)}
.card .body{display:flex;flex-direction:column;gap:12px;padding:24px 24px 28px;flex:1}
.card .k{font-family:var(--mono);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--lime)}
.card h3{font-size:22px;color:var(--white);line-height:1.2}
.card p{margin:0;font-size:15px;color:var(--aqua-soft);font-weight:400}
.card .go{margin-top:auto;padding-top:10px;font-family:var(--mono);font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--lime)}
@media (max-width:980px){.cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:620px){.cards,.cards.two-col{grid-template-columns:1fr}}

.faq{margin-top:48px;border-top:1px solid var(--line);max-width:880px}
.faq details{border-bottom:1px solid var(--line);padding:24px 0}
.faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:20px;font-family:var(--display);font-size:clamp(19px,2vw,23px);font-weight:500;color:var(--white);line-height:1.3}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-family:var(--mono);color:var(--lime);flex:none}
.faq details[open] summary::after{content:"–"}
.faq details p{margin:16px 0 0;max-width:70ch;font-weight:400}
.paper .faq,.paper .faq details{border-color:var(--paper-line)}
.paper .faq summary{color:var(--paper-ink)}
.paper .faq summary::after{color:#0E5A3C}

.more{display:inline-flex;align-items:center;gap:10px;margin-top:40px;font-family:var(--mono);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--lime);text-decoration:none;border-bottom:1px solid currentColor;padding-bottom:5px;transition:gap .3s}
.more:hover{gap:16px}
.paper .more{color:#0E5A3C}
.leader h3 a{color:inherit;text-decoration:none}
.leader h3 a::before{content:"";position:absolute;inset:0;z-index:1}

.steps{counter-reset:s;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;margin-top:52px;border-top:1px solid var(--line)}
.steps > div{counter-increment:s;padding:28px 28px 28px 0;border-bottom:1px solid var(--line)}
.steps > div::before{content:counter(s,decimal-leading-zero);display:block;font-family:var(--mono);font-size:13px;letter-spacing:.2em;color:var(--lime);margin-bottom:14px}
.steps h3{color:var(--white);font-size:22px}
.steps p{margin:12px 0 0;font-size:16px;font-weight:400;max-width:34ch}
@media (max-width:900px){.steps{grid-template-columns:1fr}}

.post-meta{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:28px;font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--aqua-soft)}
.post-meta b{color:var(--lime);font-weight:500}
.tags{display:flex;flex-wrap:wrap;gap:10px;margin-top:32px}
.tags a{font-size:14px;font-weight:500;border:1.5px solid var(--line);border-radius:999px;padding:7px 14px;text-decoration:none;color:var(--aqua)}
.tags a:hover,.tags a[aria-current]{border-color:var(--lime);color:var(--lime)}
.final .ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:36px}
.notfound{min-height:60vh;display:flex;align-items:center}
.paper .item{border-color:var(--paper-line)}
.paper .item b{color:var(--paper-ink)}
.paper .item p{color:var(--paper-ink)}
.paper .item:hover b{color:#0E5A3C}
.paper .stats + .stats{margin-top:0;border-top:0}
/* chips de presença de marca (fundo escuro): mais destaque */
.chip{display:inline-flex;align-items:center;gap:9px;padding:9px 16px;color:var(--white);background:rgba(130,230,40,.1);border-color:rgba(130,230,40,.6);opacity:1;cursor:default;transition:background .25s,color .25s,transform .25s,box-shadow .3s}
.chip::before{content:"";flex:none;width:7px;height:7px;border-radius:50%;background:var(--lime);box-shadow:0 0 0 0 rgba(130,230,40,.6);animation:pulse 2.4s infinite}
.chip:nth-child(2)::before{animation-delay:.4s}.chip:nth-child(3)::before{animation-delay:.8s}.chip:nth-child(4)::before{animation-delay:1.2s}
.chip:hover{background:var(--lime);color:var(--ink);transform:translateY(-2px);box-shadow:0 10px 26px -10px rgba(130,230,40,.8)}
.chip:hover::before{background:var(--ink)}
.paper .chip{color:inherit;background:transparent;border-color:currentColor;padding:7px 14px;opacity:.9}
.paper .chip::before{display:none}
.paper .chip:hover{background:transparent;color:inherit;transform:none;box-shadow:none}
.paper .chip.on,.paper .chip.on:hover{background:var(--lime);border-color:var(--lime);color:var(--ink);opacity:1}
/* espaço entre os números do hero e o desenho do mouse */
.hero .wrap{padding-bottom:110px}
@media (max-width:720px){.hero .wrap{padding-bottom:56px}}

/* linhas que se desenham conforme a rolagem */
.dl{background-repeat:no-repeat;background-origin:border-box;background-clip:border-box;transition:background-size 1.2s cubic-bezier(.2,.7,.2,1) var(--dd,0ms),padding-left .4s cubic-bezier(.2,.7,.2,1),transform .5s cubic-bezier(.2,.7,.2,1)}

/* barra de rolagem na identidade */
html{scrollbar-color:var(--lime) var(--ink);scrollbar-width:thin}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:var(--ink);border-left:1px solid var(--line)}
::-webkit-scrollbar-thumb{background:var(--lime);border:2px solid var(--ink);border-radius:999px}
::-webkit-scrollbar-thumb:hover{background:#9BF04C}
.drawer-body,.pop-box{scrollbar-color:var(--lime) transparent}


/* botões flutuantes: WhatsApp e voltar ao topo */
.fab{position:fixed;right:max(20px,env(safe-area-inset-right,0px));bottom:calc(20px + env(safe-area-inset-bottom,0px) + var(--ck-h,0px));z-index:80;display:flex;flex-direction:column;align-items:center;gap:12px;transition:bottom .35s cubic-bezier(.2,.7,.2,1)}
.fab a,.fab button{position:relative;display:grid;place-items:center;width:58px;height:58px;border-radius:50%;border:0;padding:0;cursor:pointer;text-decoration:none;-webkit-tap-highlight-color:transparent;touch-action:manipulation;transition:transform .25s,background .25s,box-shadow .3s,opacity .3s,visibility 0s}
.fab a:focus-visible,.fab button:focus-visible{outline:2px solid var(--white);outline-offset:4px}
.fab .wa{background:#25D366;color:#fff;box-shadow:0 10px 28px -8px rgba(37,211,102,.7)}
.fab .wa svg{width:30px;height:30px}
.fab .wa::before{content:"";position:absolute;inset:0;border-radius:50%;background:#25D366;z-index:-1;animation:waPulse 2.4s ease-out infinite}
.fab .wa:hover{background:#128C7E;transform:translateY(-3px) scale(1.04)}
.fab .wa .tip{position:absolute;right:calc(100% + 12px);top:50%;transform:translateY(-50%) translateX(8px);opacity:0;pointer-events:none;white-space:nowrap;background:var(--ink);color:var(--white);border:1px solid var(--line);border-radius:999px;padding:9px 16px;font:500 14px/1 var(--body);transition:opacity .25s,transform .25s}
.fab .wa:hover .tip,.fab .wa:focus-visible .tip{opacity:1;transform:translateY(-50%)}
.fab .top-btn{width:48px;height:48px;background:var(--deep);color:var(--lime);border:1.5px solid rgba(130,230,40,.7);box-shadow:0 8px 24px -10px rgba(0,0,0,.8);opacity:0;visibility:hidden;transform:translateY(10px);transition:opacity .3s,transform .3s,visibility 0s .3s,background .25s,color .25s}
.fab .top-btn.show{opacity:1;visibility:visible;transform:none;transition:opacity .3s,transform .3s,background .25s,color .25s}
.fab .top-btn.show:hover{background:var(--lime);color:var(--ink);transform:translateY(-3px)}
.fab .top-btn svg{width:20px;height:20px}
@keyframes waPulse{0%{transform:scale(1);opacity:.55}70%,100%{transform:scale(1.55);opacity:0}}
@media (max-width:540px){.fab .wa{width:54px;height:54px}.fab .wa .tip{display:none}}
@media (min-width:768px){#aviso-cookies{right:calc(max(20px,env(safe-area-inset-right,0px)) + 58px + 24px)}}

/* rolagem suave (Lenis) */
html.lenis,html.lenis body{height:auto}
.lenis.lenis-smooth{scroll-behavior:auto!important}
.lenis.lenis-smooth [data-lenis-prevent]{overscroll-behavior:contain}
.lenis.lenis-stopped{overflow:hidden}

/* seleção de texto na cor da marca */
::selection{background:var(--lime);color:var(--ink);text-shadow:none}
::-moz-selection{background:var(--lime);color:var(--ink);text-shadow:none}
input::selection,textarea::selection{background:var(--lime);color:var(--ink)}
img::selection{background:rgba(130,230,40,.35)}
/* imagens com width/height no HTML nunca ficam esticadas */
img{height:auto}
.leaders > .leader{--d:0ms!important}
/* ===== ambientes: galeria que anda na horizontal conforme a rolagem ===== */
.hs{--W:clamp(280px,86vw,1180px);position:relative;margin-top:48px}
.hs-sticky{display:block}
.hs-bar{display:flex;align-items:center;gap:20px;width:100%;max-width:1180px;box-sizing:border-box;margin:0 auto 26px;padding-inline:max(20px,env(safe-area-inset-left,0px))}
.hs-count{font-family:var(--mono);font-size:13px;letter-spacing:.24em;color:var(--lime);white-space:nowrap;min-width:5.2em}
.hs-line{position:relative;flex:1;height:2px;background:var(--line);overflow:hidden}
.hs-line span{position:absolute;inset:0;background:var(--lime);transform:scaleX(0);transform-origin:left}
.hs-nav{display:flex;gap:10px}
.hs-nav button{all:unset;box-sizing:border-box;width:44px;height:44px;border-radius:50%;border:1.5px solid var(--line);display:grid;place-items:center;color:var(--aqua);cursor:pointer;font-size:18px;transition:border-color .4s var(--soft),color .4s var(--soft),background .4s var(--soft)}
.hs-nav button:hover{border-color:var(--lime);color:var(--lime)}
.hs-nav button:focus-visible{outline:2px solid var(--lime);outline-offset:3px}
.hs-nav button[disabled]{opacity:.35;cursor:default;border-color:var(--line);color:var(--aqua)}
.hs-track{display:flex;gap:40px;padding-inline:max(20px,calc((100% - var(--W)) / 2));overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding-bottom:8px}
.hs-track::-webkit-scrollbar{display:none}
.hs-slide{flex:none;width:var(--W);display:grid;grid-template-columns:minmax(0,1fr);gap:22px;align-items:center;scroll-snap-align:center}
@media (min-width:901px){.hs-slide{grid-template-columns:minmax(0,1.55fr) minmax(0,1fr);gap:clamp(28px,3vw,48px)}}
.hs-slide figure{margin:0;position:relative;aspect-ratio:16/9;border-radius:4px;overflow:hidden;background:var(--deep)}
.hs-slide figure img{width:100%;height:100%;object-fit:cover}
.hs-slide .tag{max-width:calc(100% - 24px)}
.hs-info{max-width:66ch}
.hs-info .v-num{margin:0}
.hs-info h3{font-size:clamp(28px,3vw,40px);font-weight:500;color:var(--white);margin:8px 0 0}
.hs-info h3 a{color:inherit;text-decoration:none;background:linear-gradient(var(--lime),var(--lime)) no-repeat 0 100%/0 2px;transition:background-size .6s var(--soft)}
.hs-info h3 a:hover{background-size:100% 2px}
.hs-info .v-head{margin:10px 0 0}
.hs-info .v-txt{margin:6px 0 0}
.hs-info .v-label{margin:18px 0 0}
.hs-info .chips{margin-top:10px}
/* com JavaScript: a rolagem vertical da página empurra a galeria para o lado */
.js .hs:not(.hs-native) .hs-sticky{position:sticky;top:0;height:100vh;height:100svh;padding-top:96px;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
.js .hs:not(.hs-native) .hs-track{overflow:visible;scroll-snap-type:none;will-change:transform;padding-bottom:0;width:max-content;min-width:100%}
.js .hs:not(.hs-native) .hs-slide{opacity:.32;transform:scale(.965);transition:opacity .8s var(--soft),transform .8s var(--soft)}
.js .hs:not(.hs-native) .hs-slide.is-active{opacity:1;transform:none}
@media (max-width:700px){.hs{--W:clamp(260px,88vw,920px)}.hs-slide .tag{font-size:9px;letter-spacing:.1em;left:8px;bottom:8px;padding:5px 8px}.hs-track{gap:22px}.hs-nav button{width:40px;height:40px}.hs-bar{gap:14px}}

/* ================= ANIMAÇÕES MAIS SUAVES =================
   Mesma coreografia, porém mais lenta, com curvas sem arranque brusco e deslocamentos menores. */
:root{--soft:cubic-bezier(.25,.8,.25,1);--softer:cubic-bezier(.33,.9,.4,1)}
/* entrada do hero */
@keyframes rise{from{transform:translateY(60%);opacity:0}to{transform:none;opacity:1}}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.split-h .ln > span{animation:rise 1.5s var(--soft) both}
.split-h .ln:nth-child(2) > span{animation-delay:.18s}
.split-h .ln:nth-child(3) > span{animation-delay:.36s}
.hero .eyebrow{animation:fade 1.2s .1s ease-out both}
.hero .pillars{animation:fade 1.2s .8s ease-out both}
.hero .ctas{animation:fadeUp 1.2s 1s var(--soft) both}
.hero .facts > div{animation:fadeUp 1.2s var(--soft) both}
.hero .facts > div:nth-child(1){animation-delay:1.2s}.hero .facts > div:nth-child(2){animation-delay:1.32s}
.hero .facts > div:nth-child(3){animation-delay:1.44s}.hero .facts > div:nth-child(4){animation-delay:1.56s}
.hero .facts::before{animation:draw 2s 1.1s var(--soft) both}
.hero-img{animation-duration:34s}
.facts .lime b::after{animation-duration:3.2s}
.scroll-cue span{animation-duration:2.8s;animation-timing-function:ease-in-out}
.js .hero .u{transition-delay:1.7s}
/* revelar ao rolar */
.pre{transform:translateY(22px)}
.mosaic figure.pre,.person.pre,.leader.pre{transform:translateY(22px) scale(.985)}
.shown{opacity:1;transform:none;transition:none;animation:revealIn 1.3s var(--d,0ms) var(--soft) backwards}
@keyframes revealIn{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
.js .u{transition:background-size 1.6s .45s var(--soft)}
.dl{transition:background-size 1.7s var(--dd,0ms) var(--soft),padding-left .6s var(--soft),transform .7s var(--soft)}
/* botões */
.btn{transition:background .5s var(--soft),color .5s var(--soft),transform .5s var(--soft),box-shadow .6s var(--soft),border-color .5s var(--soft);animation-duration:3.8s}
.btn::before{animation-duration:5s}
.btn::after{animation-duration:5.5s}
.btn.ghost{animation:none}
.menu-btn{transition:background .5s var(--soft),color .5s var(--soft),transform .5s var(--soft),box-shadow .6s var(--soft),border-color .5s var(--soft)}
.chip{transition:background .5s var(--soft),color .5s var(--soft),transform .5s var(--soft),box-shadow .6s var(--soft)}
.chip::before{animation-duration:3.4s}
.open::before{animation-duration:5.5s}
/* menu do topo */
.top{transition:background .6s var(--soft),border-color .6s var(--soft)}
.top .wrap{transition:height .6s var(--soft)}
.top .main a{transition:color .4s var(--soft)}
.top .main a::after{transition:transform .6s var(--soft)}
/* cards, listas e imagens */
.card{transition:transform .7s var(--soft),border-color .5s var(--soft)}
.card figure img,.mosaic figure img,.person img,.leader > img,.env figure img{transition:transform 1.8s var(--soft)}
.person div{transition:transform .7s var(--soft)}
.person::after,.leader::after{transition:opacity .6s var(--soft)}
.leader{transition:transform .7s var(--soft)}
.benefit{transition:padding-left .6s var(--soft)}
.benefit::before{transition:width .6s var(--soft)}
.item{transition:padding-left .55s var(--soft)}
.item b{transition:color .5s var(--soft)}
.more{transition:gap .5s var(--soft)}
.drawer li a{transition:color .4s var(--soft),padding-left .5s var(--soft)}
.faq summary::after{transition:transform .4s var(--soft)}
/* visualizador de ambientes */
.v-media img{transition:opacity 1.5s ease,transform 8s linear}
.v-info.in > *{animation:fadeUp .9s both var(--soft)}
.v-info.in .chip{animation:fadeUp .8s both var(--soft);animation-delay:calc(.3s + var(--k) * 100ms)}
.v-tabs button{transition:color .4s var(--soft),padding-left .5s var(--soft)}
/* faixa corrida */
.mq-track{animation-duration:60s}
/* menu lateral, popup, botões flutuantes */
.drawer-bg{transition:opacity .5s ease,visibility 0s .5s}
.drawer-bg.is-open{transition:opacity .5s ease}
.drawer{transition:transform .65s var(--soft),visibility 0s .65s}
.drawer.is-open{transition:transform .65s var(--soft)}
.fab{transition:bottom .5s var(--soft)}
.fab .wa::before{animation-duration:3.2s}
.fab .top-btn{transition:opacity .45s ease,transform .5s var(--soft),visibility 0s .45s,background .4s,color .4s}
.fab .top-btn.show{transition:opacity .45s ease,transform .5s var(--soft),background .4s,color .4s}
@keyframes glow{0%,100%{box-shadow:0 0 0 0 rgba(130,230,40,0)}50%{box-shadow:0 0 22px 1px rgba(130,230,40,.3)}}
@keyframes waPulse{0%{transform:scale(1);opacity:.45}70%,100%{transform:scale(1.5);opacity:0}}



"""


def montar_assets():
    css = ler("home.css")
    css = css.replace("url(img/hero.jpg)", "url(/img/hero.webp)")
    # o menu principal passa a ser <nav class="main"> (o menu lateral tem estilo próprio)
    css = css.replace(".top nav{", ".top .main{").replace(".top nav a", ".top .main a")
    css = css.replace("@media (max-width:900px){.top nav{display:none}}", "")
    css += CSS_EXTRA
    gravar("assets/site.css", css.strip() + "\n")

    js = ler("site_orig.js")
    # links do menu viram páginas: o menu ativo por rolagem só vale para âncoras
    js = js.replace('const links=[...document.querySelectorAll(".top nav a")];',
                    'const links=[...document.querySelectorAll(".top .main a")].filter(a=>(a.getAttribute("href")||"").startsWith("#"));')
    js = js.replace("%6)*80+", "%6)*110+")
    js = js.replace("    heroImg.style.transform", "    if(heroImg) heroImg.style.transform")
    js = js.replace("    const fr=finalImg.parentElement", "    if(finalImg){const fr=finalImg.parentElement")
    js = js.replace("scale(1.15)`;\n", "scale(1.15)`;}\n")
    js = js.replace('const revealSel=".band h2,', 'const revealSel=".card,.faq details,.steps > div,.figure-wide,.band h2,')
    js += r"""
/* ---------- menu lateral ---------- */
const menuBtn=document.querySelector(".menu-btn"), drawer=document.getElementById("menu-lateral"), drawerBg=document.querySelector(".drawer-bg");
if(menuBtn&&drawer){
  const setOpen=(open,devolverFoco=true)=>{
    drawer.classList.toggle("is-open",open); if(drawerBg) drawerBg.classList.toggle("is-open",open);
    menuBtn.setAttribute("aria-expanded",open); drawer.setAttribute("aria-hidden",!open);
    document.body.style.overflow=open?"hidden":"";document.documentElement.style.overflow=open?"hidden":"";
    if(open) setTimeout(()=>drawer.querySelector(".drawer-close").focus(),60); else if(devolverFoco) menuBtn.focus();
  };
  menuBtn.addEventListener("click",()=>setOpen(true));
  drawer.querySelector(".drawer-close").addEventListener("click",()=>setOpen(false));
  if(drawerBg) drawerBg.addEventListener("click",()=>setOpen(false));
  document.addEventListener("keydown",e=>{if(e.key==="Escape"&&drawer.classList.contains("is-open")) setOpen(false);});
  drawer.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>setOpen(false,false)));
  /* foco preso dentro do menu enquanto aberto */
  drawer.addEventListener("keydown",e=>{
    if(e.key!=="Tab") return;
    const f=[...drawer.querySelectorAll("a,button,summary")].filter(el=>el.offsetParent!==null);
    if(!f.length) return; const first=f[0], last=f[f.length-1];
    if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}
    else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}
  });
}

/* ---------- linhas que se desenham conforme a rolagem ---------- */
(function(){
  const sel=".hero,.phero,.agenda,.col,.item,.benefits,.benefit,.stats,.rec-foot,.audience,.addr,footer,.ft-bottom,.steps,.steps > div,.faq,.faq details";
  const lados={top:["0 0","100% W","0 W"],bottom:["0 100%","100% W","0 W"],left:["0 0","W 100%","W 0"],right:["100% 0","W 100%","W 0"]};
  const els=[...document.querySelectorAll(sel)];
  const io=new IntersectionObserver(es=>es.forEach(en=>{if(!en.isIntersecting) return; const el=en.target; el.style.backgroundSize=el.dataset.dlFim; io.unobserve(el);}),{threshold:0,rootMargin:"0px 0px -8% 0px"});
  els.forEach(el=>{
    const cs=getComputedStyle(el), img=[], pos=[], ini=[], fim=[];
    for(const lado in lados){
      const w=parseFloat(cs[`border-${lado}-width`]); if(!w||cs[`border-${lado}-style`]==="none") continue;
      const cor=cs[`border-${lado}-color`]; if(cor==="rgba(0, 0, 0, 0)"||cor==="transparent") continue;
      const [p,f,i]=lados[lado];
      img.push(`linear-gradient(${cor},${cor})`); pos.push(p); fim.push(f.replace("W",w+"px")); ini.push(i.replace("W",w+"px"));
      el.style[`border${lado[0].toUpperCase()+lado.slice(1)}Color`]="transparent";
    }
    if(!img.length) return;
    if(reduce){ el.style.backgroundImage=img.join(","); el.style.backgroundPosition=pos.join(","); el.style.backgroundSize=fim.join(","); el.classList.add("dl"); return; }
    const irmaos=[...el.parentElement.children].filter(c=>c.matches(sel));
    el.style.setProperty("--dd",(Math.max(0,irmaos.indexOf(el))%6)*90+"ms");
    el.style.backgroundImage=img.join(","); el.style.backgroundPosition=pos.join(","); el.style.backgroundSize=ini.join(",");
    el.dataset.dlFim=fim.join(",");
    el.classList.add("dl");
    requestAnimationFrame(()=>io.observe(el));
  });
})();

/* ---------- rolagem suave ---------- */
(function(){
  if(reduce||typeof Lenis==="undefined") return;
  document.documentElement.style.scrollBehavior="auto";
  const lenis=new Lenis({duration:1.5,easing:t=>1-Math.pow(1-t,4),smoothWheel:true,wheelMultiplier:.9});
  window.lenis=lenis;
  function raf(t){lenis.raf(t);requestAnimationFrame(raf);}
  requestAnimationFrame(raf);
  /* âncoras da própria página: rolagem suave descontando o menu fixo */
  document.addEventListener("click",e=>{
    const a=e.target.closest('a[href^="#"]'); if(!a||e.defaultPrevented) return;
    const id=a.getAttribute("href"); if(id.length<2) return;
    const alvo=document.querySelector(id); if(!alvo) return;
    e.preventDefault(); const topo=document.querySelector(".top"); const off=(topo?topo.offsetHeight:0)+12; lenis.scrollTo(Math.max(0,alvo.getBoundingClientRect().top+window.scrollY-off)); history.replaceState(null,"",id);
  });
  /* menu lateral e popup travam a rolagem: pausa o Lenis junto */
  document.querySelectorAll(".drawer-body,.pop-box,.v-tabs").forEach(el=>el.setAttribute("data-lenis-prevent",""));
  new MutationObserver(()=>{document.body.style.overflow==="hidden"?lenis.stop():lenis.start();}).observe(document.body,{attributes:true,attributeFilter:["style"]});
})();

/* ---------- botões flutuantes ---------- */
(function(){
  const topBtn=document.querySelector(".top-btn"); if(!topBtn) return;
  const atualiza=()=>topBtn.classList.toggle("show",window.scrollY>500);
  addEventListener("scroll",atualiza,{passive:true}); atualiza();
  topBtn.addEventListener("click",()=>{ if(window.lenis) window.lenis.scrollTo(0); else window.scrollTo({top:0,behavior:reduce?"auto":"smooth"}); });
  /* no celular, o banner de cookies ocupa a base: os botões sobem junto */
  const ck=document.getElementById("aviso-cookies"), raiz=document.documentElement;
  if(ck){
    const ajusta=()=>{const visivel=!ck.classList.contains("hidden");raiz.style.setProperty("--ck-h",(visivel&&innerWidth<768)?(ck.offsetHeight+16)+"px":"0px");};
    new MutationObserver(ajusta).observe(ck,{attributes:true,attributeFilter:["class"]}); addEventListener("resize",ajusta); setTimeout(ajusta,50);
  }
})();

/* ---------- ambientes: galeria horizontal guiada pela rolagem ---------- */
(function(){
  const hs=document.getElementById("hs"); if(!hs) return;
  const sticky=hs.querySelector(".hs-sticky"), track=hs.querySelector(".hs-track"), slides=[...hs.querySelectorAll(".hs-slide")];
  const fill=hs.querySelector(".hs-line span"), cnt=hs.querySelector(".hs-count"), prev=hs.querySelector(".hs-prev"), next=hs.querySelector(".hs-next");
  const N=slides.length; let dist=0, total=0, step=1, atual=-1, K=.8;
  const nativo=()=>{ hs.classList.add("hs-native"); hs.style.height=""; track.style.transform=""; };
  if(reduce){ nativo(); ligaBotoesNativo(); return; }
  function medir(){
    dist=Math.max(0,track.scrollWidth-sticky.clientWidth);
    step=N>1?slides[1].offsetLeft-slides[0].offsetLeft:1;
    total=Math.max(1,dist*K);
    hs.style.height=(sticky.offsetHeight+total)+"px";
    atualiza();
  }
  function progresso(){
    const topo=hs.getBoundingClientRect().top;
    return Math.min(1,Math.max(0,-topo/total));
  }
  function atualiza(){
    const p=progresso(), x=p*dist;
    track.style.transform="translate3d("+(-x)+"px,0,0)";
    fill.style.transform="scaleX("+p+")";
    const i=Math.min(N-1,Math.max(0,Math.round(x/step)));
    if(i!==atual){
      atual=i;
      slides.forEach((s,k)=>s.classList.toggle("is-active",k===i));
      cnt.textContent=String(i+1).padStart(2,"0")+" / "+String(N).padStart(2,"0");
      if(prev) prev.disabled=i===0; if(next) next.disabled=i===N-1;
    }
  }
  let tk=false;
  addEventListener("scroll",()=>{if(!tk){tk=true;requestAnimationFrame(()=>{atualiza();tk=false;});}},{passive:true});
  addEventListener("resize",medir);
  addEventListener("load",medir);
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(medir);
  function ir(i){
    i=Math.min(N-1,Math.max(0,i));
    const base=hs.getBoundingClientRect().top+scrollY;
    const alvo=base+Math.min(1,(i*step)/Math.max(1,dist))*total;
    if(window.lenis) window.lenis.scrollTo(alvo); else scrollTo({top:alvo,behavior:"smooth"});
  }
  if(prev) prev.addEventListener("click",()=>ir(atual-1));
  if(next) next.addEventListener("click",()=>ir(atual+1));
  medir();
  function ligaBotoesNativo(){}
})();
function ligaBotoesNativo(){
  const hs=document.getElementById("hs"); if(!hs) return;
  const track=hs.querySelector(".hs-track"), prev=hs.querySelector(".hs-prev"), next=hs.querySelector(".hs-next");
  const passo=()=>{const s=track.querySelectorAll(".hs-slide");return s.length>1?s[1].offsetLeft-s[0].offsetLeft:track.clientWidth;};
  if(prev) prev.addEventListener("click",()=>track.scrollBy({left:-passo(),behavior:"auto"}));
  if(next) next.addEventListener("click",()=>track.scrollBy({left:passo(),behavior:"auto"}));
}
"""
    gravar("assets/site.js", js.strip() + "\n")

    cap = ler("captura_orig.js")
    cap = cap.replace(
        "const CTA_IDS      = ['btn-inscreva-nav', 'btn-inscreva-hero', 'btn-garantir-vaga', 'btn-footer-parceiro'];",
        "const CTA_IDS      = ['btn-inscreva-nav', 'btn-inscreva-hero', 'btn-garantir-vaga', 'btn-footer-parceiro', 'btn-cta-menu', 'btn-cta-pagina', 'btn-cta-marcas', 'btn-cta-convite'];")
    assert "btn-cta-menu" in cap
    gravar("assets/captura.js", cap.strip() + "\n")

    def versao(rel):
        with open(os.path.join(RAIZ, rel), "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    return {k: versao(f"assets/{k}") for k in ("site.css", "site.js", "captura.js")}


# ---------------------------------------------------------------------------
# Peças do template
# ---------------------------------------------------------------------------
MENU = [
    ("/", "Início"),
    ("/quem-somos/", "Quem somos"),
    ("/o-clube/", "O clube"),
    ("/ambientes/", "Ambientes"),
    ("/para-marcas/", "Para marcas"),
    ("/blog/", "Blog"),
]


def grupos_menu():
    """Todas as páginas do site, organizadas para o menu lateral."""
    import conteudo
    return [
        ("Principal", [("/", "Início"), ("/quem-somos/", "Quem somos"), ("/a-marca/", "A marca"),
                       ("/andre-albuquerque/", "André Albuquerque"), ("/rafael-tonietto/", "Rafael Tonietto")]),
        ("O clube", [("/o-clube/", "O clube"), ("/agenda/", "Agenda"), ("/comunidade/", "Comunidade"),
                     ("/business/", "Business"), ("/education/", "Education"), ("/wellness/", "Wellness")]),
        ("Ambientes", [("/ambientes/", "Todos os ambientes")] +
         [(f"/ambientes/{a[0]}/", a[1]) for a in conteudo.AMBIENTES]),
        ("Para marcas", [("/para-marcas/", "Para marcas"), ("/para-marcas/naming-e-ativacoes/", "Naming e ativações"),
                         ("/para-marcas/eventos-e-lancamentos/", "Eventos e lançamentos"),
                         ("/para-marcas/midia-espontanea/", "Mídia espontânea")]),
        ("Blog", [("/blog/", "Todos os artigos")] + [(f"/blog/{c}/", n) for c, (n, _) in conteudo.CATS.items()]),
        ("Atendimento", [("/convite/", "Pedir convite"), ("/contato/", "Contato"), ("/programas/", "Programas"),
                         ("/politica-de-privacidade/", "Política de Privacidade"), ("/termos-de-uso/", "Termos de Uso")]),
    ]


def cabecalho(url):
    def atual(href):
        return url == href or (href != "/" and url.startswith(href))

    def item(href, nome, exato=False):
        sim = (url == href) if exato else atual(href)
        marca = ' aria-current="page"' if sim else ""
        return f'<a href="{href}"{marca}>{nome}</a>'

    links = "\n      ".join(item(h, n) for h, n in MENU)
    grupos = grupos_menu()
    # abre o grupo que contém a página atual; se nenhum, abre o "Principal"
    aberto = next((g for g, itens in grupos if any(h == url for h, _ in itens)), "Principal")
    blocos = "\n".join(
        f'    <details{" open" if g == aberto else ""}><summary>{g}</summary><ul>'
        + "".join(f"<li>{item(h, n, exato=True)}</li>" for h, n in itens) + "</ul></details>"
        for g, itens in grupos)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="top">
  <div class="wrap">
    <a href="/" aria-label="WeNorth Club, início"><img src="/img/logo.webp" alt="WeNorth Club" width="205" height="32"></a>
    <nav class="main" aria-label="Principal">
      {links}
    </nav>
    <div class="top-right">
      <a class="btn hdr-cta" id="btn-inscreva-nav" href="/convite/">Seja parceiro</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu-lateral" aria-label="Abrir menu com todas as páginas"><span class="ico" aria-hidden="true"><i></i><i></i><i></i></span></button>
    </div>
  </div>
  <div class="progress" aria-hidden="true"></div>
</header>
<div class="drawer-bg" aria-hidden="true"></div>
<aside class="drawer" id="menu-lateral" aria-label="Menu com todas as páginas" aria-hidden="true">
  <div class="drawer-head">
    <img src="/img/logo.webp" alt="WeNorth Club" width="180" height="28">
    <button type="button" class="drawer-close" aria-label="Fechar menu">&times;</button>
  </div>
  <nav class="drawer-body" aria-label="Todas as páginas">
{blocos}
  </nav>
  <div class="drawer-foot">
    <a class="btn" id="btn-cta-menu" href="/convite/">Seja parceiro</a>
    <p>Rua Eng. Arthur Bettes, 419 · Portão · Curitiba/PR<br><a href="https://wa.me/554188239396" target="_blank" rel="noopener">(41) 98823-9396</a></p>
  </div>
</aside>'''


RODAPE = '''<footer>
  <div class="wrap">
    <div class="ft-grid">
      <div class="ft-brand">
        <img src="/img/logo.webp" alt="WeNorth Club" width="205" height="32" loading="lazy">
        <p>O clube de negócios do fitness e wellness no Brasil. Business, Education e Wellness em mais de 600 m² em Curitiba/PR.</p>
        <p class="ft-legal">Grupo WeNorth · Personal Trainer Academy como principal integrante · Curitiba, PR</p>
      </div>
      <div class="ft-col">
        <h4>O clube</h4>
        <ul>
          <li><a href="/o-clube/">O clube</a></li>
          <li><a href="/agenda/">Agenda</a></li>
          <li><a href="/comunidade/">Comunidade</a></li>
          <li><a href="/ambientes/">Ambientes</a></li>
          <li><a href="/business/">Business</a></li>
          <li><a href="/education/">Education</a></li>
          <li><a href="/wellness/">Wellness</a></li>
        </ul>
      </div>
      <div class="ft-col">
        <h4>Institucional</h4>
        <ul>
          <li><a href="/quem-somos/">Quem somos</a></li>
          <li><a href="/a-marca/">A marca</a></li>
          <li><a href="/andre-albuquerque/">André Albuquerque</a></li>
          <li><a href="/rafael-tonietto/">Rafael Tonietto</a></li>
          <li><a href="/para-marcas/">Para marcas</a></li>
          <li><a href="/programas/">Programas</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="https://www.personaltraineracademy.com.br/" target="_blank" rel="noopener">Personal Trainer Academy</a></li>
        </ul>
      </div>
      <div class="ft-col">
        <h4>Fale conosco</h4>
        <p><a class="ft-tel" href="https://wa.me/554188239396" target="_blank" rel="noopener">(41) 98823-9396</a></p>
        <p><a href="mailto:contato@ptadigital.com.br">contato@ptadigital.com.br</a></p>
        <p>Rua Eng. Arthur Bettes, 419<br>Portão · Curitiba/PR</p>
        <p><a href="/contato/">Contato</a> · <a href="/convite/" id="btn-footer-parceiro">Seja parceiro</a></p>
      </div>
    </div>
    <div class="ft-bottom">
      <span>© 2026 WeNorth Club. Todos os direitos reservados.</span>
      <nav aria-label="Legal"><a href="/politica-de-privacidade/">Política de Privacidade</a><a href="/termos-de-uso/">Termos de Uso</a><span>Imagens dos ambientes ilustrativas · projeto em desenvolvimento</span></nav>
    </div>
  </div>
</footer>'''


def popup_html():
    p = ler("popup.html")
    p = p.replace('href="https://wenorthclub.com.br/politica-de-privacidade/" target="_blank" rel="noopener"',
                  'href="/politica-de-privacidade/"')
    assert 'href="/politica-de-privacidade/"' in p
    return p


ORG = {
    "@type": "Organization",
    "@id": DOMINIO + "/#org",
    "name": "WeNorth Club",
    "url": DOMINIO + "/",
    "logo": DOMINIO + "/img/logo.webp",
    "slogan": "O clube de negócios do fitness e wellness no Brasil.",
    "parentOrganization": {"@type": "Organization", "name": "Personal Trainer Academy",
                           "url": "https://www.personaltraineracademy.com.br/"},
    "address": {"@type": "PostalAddress", "streetAddress": "Rua Eng. Arthur Bettes, 419",
                "addressLocality": "Curitiba", "addressRegion": "PR", "addressCountry": "BR"},
    "telephone": "+55-41-98823-9396",
    "email": "contato@ptadigital.com.br",
}


def breadcrumb_ld(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMINIO + h}
        for i, (h, n) in enumerate(crumbs)]}


def faq_ld(perguntas):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in perguntas]}


def limpar_ficticio(txt):
    return re.sub(r"<!--.*?-->", "", txt)


PAGINAS = []   # (url, titulo, descricao, prioridade, noindex)


def pagina(url, titulo, descricao, corpo, *, crumbs=None, schema=None, og_img="/img/hero.jpg",
           noindex=False, cta_final=True, prioridade="0.7", og_type="website", home=False):
    versoes = ASSETS
    canon = DOMINIO + url
    nome_og = re.sub(r"^/img/(.+)\.(?:jpg|webp|png)$", r"\1", og_img)
    if "og/" + nome_og not in IMG:
        raise SystemExit(f"sem imagem de compartilhamento para {og_img}")
    og_img = f"/img/og/{nome_og}.webp"
    graph = [] if home else [ORG]
    if crumbs:
        graph.append(breadcrumb_ld(crumbs))
    graph += schema or []
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace('.jpg"', '.webp"')
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    t = html.escape(titulo)
    d = html.escape(descricao)
    final = cta_final_html() if cta_final else ""
    doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#000F0F">
<meta property="og:locale" content="pt_BR">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="WeNorth Club">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMINIO}{og_img}">
<meta property="og:image:type" content="image/webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{DOMINIO}{og_img}">
<link rel="icon" type="image/webp" href="/img/favicon.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans+Condensed:wght@500;600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={versoes['site.css']}">
<script type="application/ld+json">{ld}</script>
</head>
<body>
{cabecalho(url)}

<main id="conteudo">
{corpo}
{final}
</main>

{RODAPE}

<div class="fab">
  <a class="wa" href="https://wa.me/554188239396?text=Ol%C3%A1%2C%20vim%20pelo%20site%20do%20WeNorth%20Club%20e%20quero%20falar%20com%20a%20equipe." target="_blank" rel="noopener" aria-label="Falar com a equipe no WhatsApp"><span class="tip">Fale no WhatsApp</span><svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.04 3C8.85 3 3 8.84 3 16.02c0 2.3.6 4.54 1.74 6.52L3 29l6.62-1.7a13.02 13.02 0 0 0 6.42 1.64h.01c7.18 0 13.03-5.84 13.03-13.02C29.08 8.84 23.22 3 16.04 3Zm0 23.7h-.01a10.8 10.8 0 0 1-5.5-1.5l-.4-.23-3.93 1.01 1.05-3.83-.26-.4a10.7 10.7 0 0 1-1.66-5.73c0-5.95 4.85-10.8 10.82-10.8 2.89 0 5.6 1.12 7.64 3.17a10.72 10.72 0 0 1 3.16 7.64c0 5.96-4.86 10.67-10.91 10.67Zm5.93-8.1c-.33-.16-1.93-.95-2.23-1.06-.3-.11-.52-.16-.74.17-.22.32-.85 1.06-1.04 1.28-.19.22-.38.24-.7.08-.33-.16-1.38-.51-2.63-1.62-.97-.87-1.63-1.94-1.82-2.27-.19-.33-.02-.5.14-.66.15-.15.33-.38.5-.57.16-.19.22-.33.33-.55.11-.22.05-.41-.03-.57-.08-.16-.74-1.78-1.01-2.44-.27-.64-.54-.55-.74-.56h-.63c-.22 0-.57.08-.87.41-.3.33-1.14 1.11-1.14 2.72 0 1.6 1.17 3.15 1.33 3.37.16.22 2.3 3.5 5.57 4.91.78.34 1.38.54 1.86.69.78.25 1.49.21 2.05.13.63-.09 1.93-.79 2.2-1.55.27-.76.27-1.41.19-1.55-.08-.14-.3-.22-.63-.38Z"/></svg></a>
  <button type="button" class="top-btn" aria-label="Voltar ao topo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>
</div>

{popup_html()}
<script src="https://unpkg.com/lenis@1.1.20/dist/lenis.min.js"></script>
<script src="/assets/site.js?v={versoes['site.js']}"></script>
<script src="/assets/captura.js?v={versoes['captura.js']}"></script>
</body>
</html>
'''
    doc = otimizar_imgs(doc)
    arquivo = "404.html" if url == "/404.html" else (url.strip("/") + "/index.html" if url != "/" else "index.html")
    gravar(arquivo, doc)
    if not noindex:
        PAGINAS.append((url, titulo, descricao, prioridade))


def cta_final_html(titulo='Venha conhecer o <span class="u">clube</span>.'):
    return f'''  <section class="band final" id="contato">
    <div class="final-img" aria-hidden="true"></div>
    <div class="wrap">
      <p class="eyebrow">Business · Education · Wellness</p>
      <h2>{titulo}</h2>
      <div class="open"><span>Inauguração prevista</span><b>Fevereiro de 2027</b></div>
      <div class="ctas"><a class="btn" id="btn-garantir-vaga" href="/convite/">Quero ser parceiro</a><a class="btn ghost" href="/contato/">Falar com a equipe</a></div>
      <div class="addr">
        <div><small>Endereço</small><p>Rua Eng. Arthur Bettes, 419<br>Portão · Curitiba/PR</p></div>
      </div>
    </div>
  </section>'''


def phero(crumbs, eyebrow, h1, lede="", img="/img/hero.webp", ctas="", cap=True):
    itens = []
    for i, (h, n) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            itens.append(f'<li><span aria-current="page">{n}</span></li>')
        else:
            itens.append(f'<li><a href="{h}">{n}</a></li>')
    lede_html = f'\n      <p class="lede">{lede}</p>' if lede else ""
    ctas_html = f'\n      <div class="ctas">{ctas}</div>' if ctas else ""
    cap_html = '\n    <span class="cap">Imagem ilustrativa · projeto em desenvolvimento</span>' if cap else ""
    return f'''  <section class="phero">
    <div class="phero-img" style="--img:url({img})" aria-hidden="true"></div>{cap_html}
    <div class="wrap">
      <nav aria-label="Você está em"><ol class="crumbs">{"".join(itens)}</ol></nav>
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>{lede_html}{ctas_html}
    </div>
  </section>'''


def card(href, img, alt, k, titulo, texto, go="Ver mais"):
    return f'''<a class="card" href="{href}"><figure><img src="{img}" alt="{alt}" loading="lazy" sizes="{SIZES_CARD}"></figure><div class="body"><span class="k">{k}</span><h3>{titulo}</h3><p>{texto}</p><span class="go">{go} →</span></div></a>'''


def faq_html(perguntas):
    itens = "\n".join(f'        <details><summary>{q}</summary><p>{a}</p></details>' for q, a in perguntas)
    return f'      <div class="faq">\n{itens}\n      </div>'


# ---------------------------------------------------------------------------
# Arquivos de SEO
# ---------------------------------------------------------------------------
def arquivos_seo():
    urls = [(u, p) for u, _, _, p in PAGINAS]
    # inclui o subsite /programas/, exceto as páginas que agora apontam canonical para a raiz
    with open(os.path.join(RAIZ, "programas", "sitemap.xml"), encoding="utf-8") as f:
        for loc in re.findall(r"<loc>(.*?)</loc>", f.read()):
            caminho = loc.replace(DOMINIO, "")
            if caminho not in ("/programas/sobre/", "/programas/marcas/"):
                urls.append((caminho, "0.6"))
    linhas = "\n".join(f"  <url><loc>{DOMINIO}{u}</loc><lastmod>{HOJE}</lastmod><priority>{p}</priority></url>"
                       for u, p in urls)
    gravar("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{linhas}\n</urlset>\n')
    gravar("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /obrigado/\n\nSitemap: {DOMINIO}/sitemap.xml\n")
    blocos = {}
    for u, t, d, _ in PAGINAS:
        grupo = ("Blog" if u.startswith("/blog/") else "Ambientes" if u.startswith("/ambientes/")
                 else "Para marcas" if u.startswith("/para-marcas/") else "Páginas principais")
        blocos.setdefault(grupo, []).append(f"- [{t}]({DOMINIO}{u}): {d}")
    corpo = "\n\n".join(f"## {g}\n\n" + "\n".join(v) for g, v in blocos.items())
    gravar("llms.txt", f"""# WeNorth Club

> O clube de negócios do fitness e wellness no Brasil. Espaço de mais de 600 m² em Curitiba/PR (Rua Eng. Arthur Bettes, 419, Portão), com inauguração prevista para fevereiro de 2027. Pilares: Business, Education e Wellness. Acesso apenas por convite. O WeNorth Club é a casa do grupo WeNorth, que tem a Personal Trainer Academy como principal integrante.

{corpo}

## Programas

- [Programas WeNorth]({DOMINIO}/programas/): eventos, imersões, mentorias e cursos da Personal Trainer Academy e do WeNorth Club.
""")
    gravar(".htaccess", "ErrorDocument 404 /404.html\n")


def relatorio_ficticio():
    titulos = {u: t for u, t, _, _ in PAGINAS}
    titulos.update(EXTRA_TITULOS)
    linhas = ["# Conteúdo fictício para o copywriter", "",
              "Trechos escritos sem base no descritivo do WeNorth Club. Cada um está marcado no HTML com "
              "`<!-- FICTÍCIO: ... -->` e precisa ser revisado ou reescrito antes da publicação.",
              "Para editar: o texto fica em `_gerador/conteudo.py`; depois rode `python3 _gerador/build.py`.", ""]
    total = 0
    for url, notas in FICTICIO.items():
        linhas.append(f"## {titulos.get(url, url)}  \n`{url}`\n")
        for n in notas:
            linhas.append(f"- [ ] {n}")
            total += 1
        linhas.append("")
    linhas.insert(4, f"**Total: {total} trechos em {len(FICTICIO)} páginas.**\n")
    gravar("CONTEUDO-FICTICIO.md", "\n".join(linhas))
    return total


EXTRA_TITULOS = {}

if __name__ == "__main__":
    ASSETS = montar_assets()
    import conteudo
    conteudo.gerar(sys.modules[__name__])
    arquivos_seo()
    n = relatorio_ficticio()
    print(f"{len(PAGINAS)} páginas indexáveis geradas · {n} trechos fictícios")
