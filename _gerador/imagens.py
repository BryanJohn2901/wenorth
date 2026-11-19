#!/usr/bin/env python3
"""Gera todas as imagens do site em WebP, no tamanho certo, a partir de _gerador/originais/.

Saídas (em /img):
  <nome>.webp          imagem principal (largura máxima por tipo)
  <nome>-640.webp      variante leve para cards e celular (fotos)
  og/<nome>.webp       1200x630 recortada, para compartilhamento (Open Graph)
  favicon.webp         ícone do site
  imagens.json         largura e altura reais de cada arquivo (usado pelo build.py)

Uso:  python3 _gerador/imagens.py
Requer: cwebp, ffmpeg (com libwebp) e webpinfo.
"""
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(RAIZ, "_gerador", "originais")
SAIDA = os.path.join(RAIZ, "img")
OG = os.path.join(SAIDA, "og")

# nome -> (largura máxima, qualidade, variante leve?, og?)
REGRAS = {
    "hero": (1920, 78, True, True),
    "andre": (900, 80, False, True),
    "rafael": (900, 80, False, True),
    "logo": (640, 90, False, False),
    "pta": (480, 90, False, False),
}
PADRAO = (1200, 80, True, True)     # fotos de ambientes, clube e pessoas


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def dimensoes(caminho):
    out = subprocess.run(["webpinfo", caminho], capture_output=True, text=True).stdout
    m = re.search(r"Width:\s*(\d+)\s*Height:\s*(\d+)", out.replace("\n", " "))
    return int(m.group(1)), int(m.group(2))


def largura_original(caminho):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width",
                          "-of", "csv=p=0", caminho], capture_output=True, text=True).stdout
    return int(out.strip())


def main():
    os.makedirs(OG, exist_ok=True)
    medidas = {}
    for arq in sorted(os.listdir(ORIG)):
        nome, ext = os.path.splitext(arq)
        if ext.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        src = os.path.join(ORIG, arq)
        larg, qual, leve, og = REGRAS.get(nome, PADRAO)
        alpha = ["-alpha_q", "100"] if ext.lower() == ".png" else []
        dst = os.path.join(SAIDA, nome + ".webp")
        ow = largura_original(src)
        # só reduz, nunca amplia
        redim = ["-resize", str(larg), "0"] if ow > larg else []
        run(["cwebp", "-quiet", "-q", str(qual), "-m", "6", *alpha, *redim, src, "-o", dst])
        w, h = dimensoes(dst)
        medidas[nome] = {"w": w, "h": h}
        if leve:
            d640 = os.path.join(SAIDA, nome + "-640.webp")
            run(["cwebp", "-quiet", "-q", "76", "-m", "6", "-resize", "640", "0", src, "-o", d640])  # fotos têm >= 1200 px
            w2, h2 = dimensoes(d640)
            medidas[nome + "-640"] = {"w": w2, "h": h2}
        if og:
            d_og = os.path.join(OG, nome + ".webp")
            run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-vf",
                 "scale=1200:630:force_original_aspect_ratio=increase,crop=1200:630" if nome not in ("andre", "rafael")
                 else "scale=1200:-1,crop=1200:630:0:0",
                 "-c:v", "libwebp", "-quality", "80", "-frames:v", "1", d_og])
            medidas["og/" + nome] = {"w": 1200, "h": 630}

    # favicon: recorta o símbolo (quadrado à esquerda do logotipo) do logo original
    logo = os.path.join(ORIG, "logo.png")
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", logo, "-vf",
         "crop=ih:ih:0:0,pad=iw+ih*0.2:ih+ih*0.2:(ow-iw)/2:(oh-ih)/2:color=0x000F0F,scale=192:192",
         "-c:v", "libwebp", "-lossless", "1", "-frames:v", "1", os.path.join(SAIDA, "favicon.webp")])
    medidas["favicon"] = {"w": 192, "h": 192}

    with open(os.path.join(RAIZ, "_gerador", "partes", "imagens.json"), "w") as f:
        json.dump(medidas, f, indent=1, sort_keys=True)
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(SAIDA) for f in fs)
    print(f"{len(medidas)} arquivos WebP em /img · {total / 1024:.0f} KB no total")


if __name__ == "__main__":
    main()
