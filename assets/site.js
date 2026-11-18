const envs=[
 ["Vitrine de parceiros","A vitrine é o primeiro contato de quem entra.","O túnel de entrada expõe os produtos das marcas parceiras em prateleiras iluminadas. É o corredor por onde todos passam e um dos pontos mais fotografados do clube.",["Suplementação","Vestuário","Farmácia de manipulação"]],
 ["Recepção","A primeira impressão, em wellness.","A recepção apresenta a assinatura do clube e, ao fundo, a Gluteus Zone sob o mezanino. É o primeiro enquadramento de quem chega.",["Parede de marca","Gluteus Zone ao fundo"]],
 ["Photo spot","Um lugar feito para a foto.","No lounge da entrada, uma asa de LED sobre grade metálica, com o nome da marca acima. É o ponto pensado para a foto de chegada de cada convidado.",["Naming do photo spot","Asa de LED na cor da marca"]],
 ["Salão multiesportes","Cada área do salão tem nome e dono.","Musculação, treino funcional e Hyrox no mesmo salão de pé-direito duplo, onde todo o conteúdo de treino é gravado. As zonas são setorizadas por pintura e letreiro na parede.",["Leg Day Zone","Functional Training Zone","Pista de sled","Estação de avaliação"]],
 ["Gluteus Zone","A área mais filmada do treino feminino.","Sob o mezanino, uma parede inteira dedicada às máquinas de glúteo. O letreiro fica exatamente atrás de quem grava a execução.",["Naming da Gluteus Zone","Cenário fixo dos conteúdos"]],
 ["Recovery","O momento que todos filmam: a banheira de gelo.","Banheira de gelo, sauna e botas de compressão num ambiente de spa. A marca fica no painel iluminado atrás da banheira.",["Recovery by","Sauna","Compressão"]],
 ["Estúdio de podcast","A marca atrás de quem está no microfone.","O convidado se fotografa sentado de frente para o microfone. A marca aparece na faixa do vidro, na placa da mesa e no painel lateral, com a academia ao fundo.",["Podcast by","Placa na mesa","Painel lateral"]],
 ["North Room","Sala de mentorias, cursos e imersões.","Palco das mentorias, pós-graduações e imersões, também disponível para locação por empresas. A parede de ativação é o fundo de toda foto de palestrante e turma.",["North Room by","Parede de ativação","Tela de abertura dos eventos"]],
 ["Vestiário","O espelho é o ponto de selfie do clube.","No espelho de corpo inteiro e nos espelhos das pias, a faixa da marca parceira. Aparece em toda foto pós-treino.",["Espelhos by","Cosméticos, higiene e farmácia"]],
 ["Jardim suspenso","A marca integrada ao verde.","Na parede externa, um jardim vertical com o nome da marca em letras iluminadas, visível do mezanino e das estações de trabalho.",["Jardim by","Letreiro iluminado"]]
];
const esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const reduce=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const pad=i=>String(i+1).padStart(2,"0");

if(document.getElementById("viewer")){
/* ---------- Ambientes: visualizador interativo ---------- */
const tabs=document.getElementById("vtabs"), media=document.getElementById("vmedia"), info=document.getElementById("vinfo"), bar=document.getElementById("vbar");
tabs.innerHTML=envs.map(([name],i)=>`<button type="button" role="tab" id="vt${i}" aria-selected="${i===0}" data-i="${i}"><span>${pad(i)}</span>${esc(name)}</button>`).join("");
media.innerHTML=envs.map(([name],i)=>`<img src="/img/a${pad(i)}.webp" alt="${esc(name)}, imagem ilustrativa" class="${i===0?"on":""}" ${i>1?'loading="lazy"':""}>`).join("");
let cur=0, timer=null, paused=false, start=0;
const DUR=6500;
function renderInfo(i){
  const [name,head,txt,chips]=envs[i];
  info.innerHTML=`<p class="v-num">Ambiente ${pad(i)} / 10</p><h3>${esc(name)}</h3><p class="v-head">${esc(head)}</p><p class="v-txt">${esc(txt)}</p>
  <p class="v-label">Presença de marca</p><div class="chips">${chips.map((c,k)=>`<span class="chip" style="--k:${k}">${esc(c)}</span>`).join("")}</div>`;
  info.classList.remove("in"); void info.offsetWidth; info.classList.add("in");
}
function go(i,user){
  cur=(i+envs.length)%envs.length;
  media.querySelectorAll("img").forEach((im,k)=>im.classList.toggle("on",k===cur));
  tabs.querySelectorAll("button").forEach((b,k)=>{b.setAttribute("aria-selected",k===cur); if(k===cur&&user) b.scrollIntoView({block:"nearest",inline:"center",behavior:reduce?"auto":"smooth"});});
  renderInfo(cur); start=performance.now();
}
tabs.addEventListener("click",e=>{const b=e.target.closest("button"); if(b){go(+b.dataset.i,true);}});
tabs.addEventListener("keydown",e=>{if(e.key==="ArrowRight"||e.key==="ArrowDown"){e.preventDefault();go(cur+1,true);document.getElementById("vt"+cur).focus();}if(e.key==="ArrowLeft"||e.key==="ArrowUp"){e.preventDefault();go(cur-1,true);document.getElementById("vt"+cur).focus();}});
const viewer=document.getElementById("viewer");
viewer.addEventListener("mouseenter",()=>paused=true); viewer.addEventListener("mouseleave",()=>{paused=false;start=performance.now()-(parseFloat(bar.style.width)||0)/100*DUR;});
let inView=false;
new IntersectionObserver(es=>es.forEach(en=>inView=en.isIntersecting),{threshold:.3}).observe(viewer);
function tick(t){
  if(!reduce){
    if(inView&&!paused){const p=Math.min((t-start)/DUR,1); bar.style.width=(p*100)+"%"; if(p>=1) go(cur+1,false);}
    else if(!inView){start=t-(parseFloat(bar.style.width)||0)/100*DUR;}
  }
  requestAnimationFrame(tick);
}
go(0,false); requestAnimationFrame(tick);

}
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
const revealSel=".card,.faq details,.steps > div,.figure-wide,.band h2,.band .eyebrow,.lede,.split p,.chips,.mosaic figure,.item,.person,.stats > div,.rec-foot,.leader,.audience > div,.benefit,.viewer,.open,.addr > div,.facts > div";
const els=[...document.querySelectorAll(revealSel)];
const vh=window.innerHeight;
const io=new IntersectionObserver(es=>es.forEach(en=>{
  if(!en.isIntersecting) return;
  const el=en.target; el.classList.add("shown"); el.classList.remove("pre");
  el.querySelectorAll("[data-count]").forEach(count); if(el.matches("[data-count]")) count(el);
  io.unobserve(el);
}),{threshold:.15,rootMargin:"0px 0px -6% 0px"});
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
  /* rede de segurança: tudo aparece mesmo sem rolagem */
  setTimeout(()=>document.querySelectorAll(".pre").forEach(el=>{el.classList.remove("pre");el.querySelectorAll("[data-count]").forEach(c=>{c.dataset.done=1;})}),6000);
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
