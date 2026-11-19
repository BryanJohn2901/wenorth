
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
const revealSel=".band h2,.band .eyebrow,.lede,.prose > *,.split p,.chips,.mosaic figure,.item,.person,.stats > div,.rec-foot,.leader,.audience > div,.benefit,.viewer,.open,.addr > div,.facts > div,.card,.faq details,.steps > div,.figure-wide,.more,.tags,.final .ctas,.col > h3,.ft-grid > div,.ft-bottom,.cap";
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
      el.style.setProperty("--d",(Math.max(0,sib.indexOf(el))%6)*80+"ms");
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
const links=[...document.querySelectorAll(".top nav a")];
const secs=links.map(a=>document.querySelector(a.getAttribute("href")));
let ticking=false;
function onScroll(){
  const y=window.scrollY, h=document.documentElement.scrollHeight-window.innerHeight;
  top_.classList.toggle("scrolled",y>40);
  prog.style.transform=`scaleX(${h>0?y/h:0})`;
  if(!reduce){
    heroImg.style.transform=`translate3d(0,${y*0.28}px,0) scale(1.08)`;
    const fr=finalImg.parentElement.getBoundingClientRect(); finalImg.style.transform=`translate3d(0,${(fr.top-window.innerHeight)*-0.12}px,0) scale(1.15)`;
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
