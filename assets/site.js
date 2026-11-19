const esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const reduce=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const pad=i=>String(i+1).padStart(2,"0");

/* ---------- contadores ---------- */
const fmt=(v,d)=>v.toLocaleString("pt-BR",{minimumFractionDigits:d,maximumFractionDigits:d});
function count(el){
  if(el.dataset.done) return; el.dataset.done=1;
  const to=parseFloat(el.dataset.count), d=+(el.dataset.dec||0), suf=el.dataset.suffix||"";
  if(reduce){el.textContent=fmt(to,d)+suf;return;}
  const t0=performance.now(), D=1600;
  (function step(t){const p=Math.min((t-t0)/D,1), e=1-Math.pow(1-p,4); el.textContent=fmt(to*e,d)+suf; if(p<1) requestAnimationFrame(step);})(t0);
}

/* ---------- revelar ao rolar (conteúdo já visível em repouso) ---------- */
const revealSel=".card,.faq details,.steps > div,.figure-wide,.band h2,.band .eyebrow,.lede,.prose > *,.split p,.chips,.mosaic figure,.item,.person,.stats > div,.rec-foot,.leader,.audience > div,.benefit,.viewer,.open,.addr > div,.facts > div,.card,.faq details,.steps > div,.figure-wide,.more,.tags,.final .ctas,.col > h3,.ft-grid > div,.ft-bottom,.cap";
const els=[...document.querySelectorAll(revealSel)];
const vh=window.innerHeight;
const io=new IntersectionObserver(es=>es.forEach(en=>{
  if(!en.isIntersecting) return;
  const el=en.target; if(el.classList.contains("pre")){el.classList.add("shown"); el.classList.remove("pre");}
  el.querySelectorAll("[data-count]").forEach(count); if(el.matches("[data-count]")) count(el);
  io.unobserve(el);
}),{threshold:.12,rootMargin:"0px 0px -10% 0px"});
if(!reduce){
  els.forEach(el=>{
    const r=el.getBoundingClientRect();
    if(r.top>vh*0.92){
      const sib=[...el.parentElement.children].filter(c=>c.matches(revealSel));
      el.style.setProperty("--d",(Math.max(0,sib.indexOf(el))%6)*110+"ms");
      el.classList.add("pre");
    }
    io.observe(el);
  });
  /* no fim da página, o que ficou colado na borda inferior também aparece */
  addEventListener("scroll",()=>{
    if(innerHeight+scrollY<document.documentElement.scrollHeight-4) return;
    document.querySelectorAll(".pre").forEach(el=>{el.classList.add("shown");el.classList.remove("pre");});
  },{passive:true});
}
/* números do topo contam ao carregar */
document.querySelectorAll(".facts [data-count]").forEach(el=>setTimeout(()=>count(el),reduce?0:900));
document.querySelectorAll("[data-count]").forEach(el=>{ if(!el.closest(".facts")) new IntersectionObserver((es,o)=>es.forEach(en=>{if(en.isIntersecting){count(en.target);o.disconnect();}}),{threshold:.6}).observe(el);});

/* ---------- topo, progresso, menu ativo, parallax ---------- */
const top_=document.querySelector(".top"), prog=document.querySelector(".progress"), heroImg=document.querySelector(".hero-img"), finalImg=document.querySelector(".final-img");
const links=[...document.querySelectorAll(".top .main a")].filter(a=>(a.getAttribute("href")||"").startsWith("#"));
const secs=links.map(a=>document.querySelector(a.getAttribute("href")));
let ticking=false;
function onScroll(){
  const y=window.scrollY, h=document.documentElement.scrollHeight-window.innerHeight;
  top_.classList.toggle("scrolled",y>40);
  prog.style.transform=`scaleX(${h>0?y/h:0})`;
  if(!reduce){
    if(heroImg) heroImg.style.transform=`translate3d(0,${y*0.28}px,0) scale(1.08)`;
    if(finalImg){const fr=finalImg.parentElement.getBoundingClientRect(); finalImg.style.transform=`translate3d(0,${(fr.top-window.innerHeight)*-0.12}px,0) scale(1.15)`;}
  }
  let act=-1; secs.forEach((s,i)=>{if(s&&s.getBoundingClientRect().top<window.innerHeight*0.4) act=i;});
  links.forEach((a,i)=>a.classList.toggle("active",i===act));
  ticking=false;
}
addEventListener("scroll",()=>{if(!ticking){ticking=true;requestAnimationFrame(onScroll);}},{passive:true});
onScroll();
document.documentElement.classList.add("js");
/* risco sob o destaque: desenha da esquerda para a direita quando o texto entra na tela */
document.querySelectorAll(".u").forEach(u=>{
  if(reduce){u.classList.add("in");return;}
  new IntersectionObserver((es,o)=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add("in");o.disconnect();}}),{threshold:.6}).observe(u);
});
setTimeout(()=>document.querySelectorAll(".u:not(.in)").forEach(u=>{const b=u.getBoundingClientRect();if(b.top<innerHeight&&b.bottom>0)u.classList.add("in");}),1500);

/* ---------- cartões: brilho que segue o mouse ---------- */
document.querySelectorAll(".person,.leader,.benefit").forEach(c=>c.addEventListener("pointermove",e=>{const r=c.getBoundingClientRect();c.style.setProperty("--mx",(e.clientX-r.left)+"px");c.style.setProperty("--my",(e.clientY-r.top)+"px");}));

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
