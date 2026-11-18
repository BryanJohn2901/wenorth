
const PTA = "https://www.personaltraineracademy.com.br";
/* Links: no rascunho usamos #rotas; na versão publicada (WN_STATIC) cada página tem endereço próprio */
const STATIC=!!window.WN_STATIC;
const PFX=window.WN_PREFIX||"";
const L=r=>{
  if(!STATIC) return "#"+r;
  if(r===""||r==="inicio") return PFX+"/";
  if(r.startsWith("programa-")) return PFX+"/"+r.slice(9)+"/";
  if(r==="sobre"||r==="marcas"||r==="aplicar") return PFX+"/"+r+"/";
  return PFX+"/#"+r;
};
const WA_NUM="5541995018521";
const P = [
  {id:"summit", cat:"eventos", catLabel:"Evento", nome:"Summit PTA 2027", status:"live",
   desc:"Ciência do treino aplicada no palco, com posicionamento, conteúdo e vendas. Presencial e sem gravação.",
   facts:[["Formato","Presencial · Curitiba"],["Para","Personal, academias e estúdios"],["Data","Em breve"]],
   href:"https://ptadigital.com.br/summit-2027", cta:"Garantir ingresso"},
  {id:"biomecanica", cat:"online", catLabel:"Formação técnica", nome:"Biomecânica na Prática 2.0", status:"live",
   desc:"Biomecânica aplicada, avaliação, prescrição, reabilitação e posicionamento em um método para musculação e treino personalizado.",
   facts:[["Formato","Online gravado"],["Para","Personal trainers"],["Com","André Albuquerque"]],
   cta:"Ver curso"},
  {id:"mco", cat:"online", catLabel:"Negócios", nome:"Mapa da Consultoria Online", status:"live",
   desc:"O passo a passo para estruturar e vender a sua consultoria online, mesmo começando do zero e com poucos seguidores.",
   facts:[["Formato","Online gravado"],["Para","Profissionais da saúde e do fitness"],["Com","Rafael Tonietto"]],
   cta:"Ver curso"},
  {id:"next", cat:"imersoes", catLabel:"Imersão", nome:"Next Experience", status:"live",
   desc:"Três dias para começar no digital. Você sai com fotos, vídeos, dois produtos e a página de vendas prontos.",
   facts:[["Formato","Presencial · 3 dias, 20h"],["Para","Personal começando no digital"],["Turmas","Consulte as próximas datas"]],
   href:PTA+"/eventos/next", cta:"Ver a imersão"},
  {id:"academia-360", cat:"imersoes", catLabel:"Imersão · 3 dias", nome:"Academia 360", status:"soon",
   desc:"Três dias no Wenorth Club para olhar a academia inteira: números, preço e margem, retenção, equipe, processos, vendas, marketing, organização das máquinas e diferenciais.",
   facts:[["Formato","Presencial · 3 dias"],["Para","Donos de academia e estúdio"],["Onde","Wenorth Club, Curitiba"]],
   cta:"Aplicar"},
  {id:"ia", cat:"imersoes", catLabel:"Imersão · 1 dia", nome:"Implementação de IA", status:"soon",
   desc:"Um dia no Wenorth Club para sair com assistentes de IA funcionando no seu atendimento, no seu conteúdo e na sua rotina.",
   facts:[["Formato","Presencial · 1 dia"],["Para","Profissionais e academias"],["Requisito","Nenhum conhecimento técnico"]],
   cta:"Aplicar"},
  {id:"lancamento", cat:"imersoes", catLabel:"Imersão", nome:"Sprint de Lançamento no Estúdio", status:"soon",
   desc:"Três dias gravando o seu infoproduto no estúdio e no salão do clube, com página e plano de lançamento.",
   facts:[["Formato","Presencial · 3 dias"],["Para","Quem já tem audiência"],["Turma","10 a 15 pessoas"]],
   cta:"Aplicar"},
  {id:"scala", cat:"mentorias", catLabel:"Mentoria", nome:"Mentoria Scala", status:"live",
   desc:"Seis meses para montar e vender a consultoria online sem largar os atendimentos presenciais.",
   facts:[["Formato","Híbrido · 6 meses + 1 dia presencial"],["Para","Personal, fisio e nutri"],["Método","5 etapas e 6 faixas"]],
   href:PTA+"/mentorias/scala", cta:"Aplicar"},
  {id:"black", cat:"mentorias", catLabel:"Mentoria", nome:"Mentoria Black", status:"live", feat:true,
   desc:"Doze meses para faturar com o digital sem depender da agenda: infoproduto, copy, funil, tráfego e lançamento.",
   facts:[["Formato","Híbrido · 12 meses + 3 presenciais"],["Para","Quem fatura R$20 a 50 mil/mês no digital"],["Inclui","Acesso ao Wenorth Club"]],
   href:PTA+"/mentorias/black", cta:"Aplicar"},
  {id:"escala", cat:"mentorias", catLabel:"Programa híbrido", nome:"Escala de Clientes", status:"soon",
   desc:"Tráfego pago implementado com acompanhamento: anúncios no ar, contatos chegando no WhatsApp e um processo para transformar contato em cliente.",
   facts:[["Formato","Híbrido · 8 semanas + 1 dia presencial"],["Para","Profissionais e academias"],["Foco","Tráfego pago"]],
   cta:"Aplicar"},
  {id:"ignite-ads", cat:"mentorias", catLabel:"Programa · 6 meses", nome:"Ignite ADS", status:"live",
   desc:"Tráfego, funil e controle de leads em um só sistema: anúncios no Meta e no Google, uma página nova por mês e o CRM PTA para acompanhar cada lead até a venda.",
   facts:[["Formato","Online · reunião mensal"],["Para","Quem já vende e quer previsibilidade"],["Com","Júlio Muniz"]],
   cta:"Aplicar"},
  {id:"academia-certificada", cat:"mentorias", catLabel:"Programa híbrido", nome:"Academia Certificada", status:"soon",
   desc:"Nossos consultores vão até a sua academia para um dia de treinamento com a equipe, mais treinamento de vendas e cinco pós-graduações de bônus para os profissionais.",
   facts:[["Formato","Híbrido"],["Para","Donos de academia e a equipe"],["Onde","Na sua academia"]],
   cta:"Quero certificar"},
  {id:"autoridade-medica", cat:"mentorias", catLabel:"Programa híbrido", nome:"Autoridade Médica", status:"soon",
   desc:"Marketing e produção de conteúdo para médicos: posicionamento, roteiros, gravação no estúdio do Wenorth Club e mais pacientes particulares, dentro das regras do CFM.",
   facts:[["Formato","Híbrido · 4 meses + 2 dias de estúdio"],["Para","Médicos de consultório"],["Foco","Conteúdo e captação de pacientes"]],
   cta:"Aplicar"},
  {id:"patrimonio-medico", cat:"mentorias", catLabel:"Programa híbrido", nome:"Patrimônio Médico", status:"soon",
   desc:"Finanças e investimentos para médicos: pessoa física e PJ, impostos, proteção da renda e um plano de investimentos para construir patrimônio.",
   facts:[["Formato","Híbrido · 10 semanas + 1 presencial"],["Para","Médicos, residentes e recém-formados"],["Foco","Finanças e investimentos"]],
   cta:"Aplicar"},
  {id:"club", cat:"comunidade", catLabel:"Comunidade", nome:"Membership Wenorth Club", status:"soon",
   desc:"Comunidade anual de empresários, influenciadores e profissionais que movem o setor, com encontros no clube.",
   facts:[["Formato","Comunidade anual"],["Para","Alumni Black e donos de academia"],["Entrada","Apenas por convite"]],
   cta:"Pedir convite"}
];
const FMT={biomecanica:"online",summit:"presencial",next:"presencial","academia-360":"presencial",lancamento:"presencial",mco:"online",scala:"hibrido",black:"hibrido","academia-certificada":"hibrido",club:"comunidade",ia:"presencial",escala:"hibrido","ignite-ads":"hibrido","autoridade-medica":"hibrido","patrimonio-medico":"hibrido"};
P.forEach(p=>p.fmt=FMT[p.id]);
const TABS=[["presencial","Presenciais","presenciais"],["online","Cursos gravados","gravados"],["hibrido","Híbridos","híbridos"],["comunidade","Comunidade","de comunidade"]];
// Perfis de cada programa: personal (personal, nutri e fisio), medico e dono (academia ou estúdio)
const AUD={biomecanica:["personal"],mco:["personal"],next:["personal"],lancamento:["personal"],scala:["personal"],black:["personal","medico"],ia:["personal","medico","dono"],escala:["personal","medico","dono"],"ignite-ads":["personal","medico","dono"],summit:["personal","dono"],club:["personal","medico","dono"],"academia-360":["dono"],"academia-certificada":["dono"],"autoridade-medica":["medico"],"patrimonio-medico":["medico"]};
P.forEach(p=>p.aud=AUD[p.id]||["personal","medico","dono"]);
const AUD_ONE={personal:"Para profissionais",medico:"Para médicos",dono:"Para donos de academia"};
const AUD_NOUN={personal:"profissionais",medico:"médicos",dono:"academias"};
const audLabel=a=>a.length===1?AUD_ONE[a[0]]:a.length===3?"Para todos os perfis":"Para "+a.map(k=>AUD_NOUN[k]).join(" e ");
let aud="todos";
const fits=p=>aud==="todos"||p.aud.includes(aud);
const FMT_LABEL={presencial:"Presencial",online:"Gravado",hibrido:"Híbrido",comunidade:"Comunidade"};
const byId=Object.fromEntries(P.map(p=>[p.id,p]));
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

function cardHTML(p){
  const action = `<a class="link" href="${L("programa-"+p.id)}">Ver programa <span class="arrow">→</span></a>`;
  return `<article class="pcard" id="p-${p.id}">
    <div class="pc-top">
      <span class="tag">${audLabel(p.aud)}</span>
      <svg viewBox="0 0 355 340" aria-hidden="true"><path d="M0 340 110 0h63l90 283h13L186 0h59l110 340H220L141 92 60 340Z" fill="currentColor"/></svg>
      <h3>${esc(p.nome)}</h3>
      <div class="badges"><span>${esc(p.catLabel)}</span><span class="${p.status==="live"?"live":""}">${p.status==="live"?"Inscrições abertas":"Em breve"}</span></div>
    </div>
    <div class="pc-body">
      <p class="desc">${esc(p.desc)}</p>
      <div class="foot"><span class="fmt">${esc(p.facts[0][1])}</span>${action}</div>
    </div>
  </article>`;
}
const grid=document.getElementById("grid"), filters=document.getElementById("filters"), catTitle=document.getElementById("cat-title"), more=document.getElementById("more");
const prev=document.getElementById("prev"), next=document.getElementById("next");
let current="presencial";
function showTab(k){
  const has=f=>P.some(p=>p.fmt===f&&fits(p));
  filters.querySelectorAll(".tab").forEach(b=>b.hidden=!has(b.dataset.fmt));
  if(!has(k)) k=TABS.find(x=>has(x[0]))[0];
  current=k;
  const t=TABS.find(x=>x[0]===k);
  grid.classList.remove("all");
  grid.innerHTML=P.filter(p=>p.fmt===k&&fits(p)).map(cardHTML).join("");
  grid.scrollLeft=0;
  catTitle.innerHTML=`Conheça os programas <em class="hl">${t[2]}</em>`;
  filters.querySelectorAll(".tab").forEach(b=>{b.setAttribute("aria-selected",b.dataset.fmt===k);b.querySelector(".count").textContent=P.filter(p=>p.fmt===b.dataset.fmt&&fits(p)).length;});
  more.textContent="Ver todos os programas"; prev.hidden=next.hidden=false;
}
filters.innerHTML=TABS.map(([k,l])=>`<button class="tab" role="tab" id="c-${k}" data-fmt="${k}" aria-selected="false"><span class="dot" aria-hidden="true"></span>${l}<span class="count"></span></button>`).join("");
filters.addEventListener("click",e=>{const b=e.target.closest("[data-fmt]"); if(b) showTab(b.dataset.fmt);});
more.addEventListener("click",()=>{
  if(grid.classList.contains("all")){showTab(current);return;}
  grid.innerHTML=P.filter(fits).map(cardHTML).join("");
  grid.classList.add("all");
  catTitle.innerHTML=`Todos os <em class="hl">programas</em>`;
  filters.querySelectorAll(".tab").forEach(b=>b.setAttribute("aria-selected","false"));
  more.textContent="Ver menos"; prev.hidden=next.hidden=true;
});
prev.addEventListener("click",()=>grid.scrollBy({left:-grid.clientWidth,behavior:"smooth"}));
next.addEventListener("click",()=>grid.scrollBy({left:grid.clientWidth,behavior:"smooth"}));
function setAud(a){
  aud=a;
  document.querySelectorAll(".aud [data-aud]").forEach(b=>b.setAttribute("aria-selected",b.dataset.aud===a));
  try{localStorage.setItem("wn-aud",a)}catch(e){}
  const n=P.filter(fits).length;
  const st=document.getElementById("aud-status");
  if(st) st.innerHTML = a==="todos"
    ? `Mostrando os <b>${n} programas</b>. Escolha um perfil acima para ver só os seus.`
    : `Mostrando <b>${n} programas</b> para ${{personal:"personal trainers, nutricionistas e fisioterapeutas",medico:"médicos",dono:"donos de academia e estúdio"}[a]}.`;
  // ao escolher um perfil, abre o formato com mais programas para ele
  if(a!=="todos"){
    const cnt=k=>P.filter(p=>p.fmt===k&&fits(p)).length;
    current=TABS.map(t=>t[0]).reduce((b,k)=>cnt(k)>cnt(b)?k:b);
  }
  showTab(current);
}
document.addEventListener("click",e=>{
  const b=e.target.closest("[data-aud]"); if(!b) return;
  setAud(b.dataset.aud);
  if(b.dataset.scroll){
    document.getElementById("programas").scrollIntoView({behavior:"smooth"});
    // destaca a caixa de perfil para a pessoa ver que dá para trocar ali
    const box=document.getElementById("aud-box");
    if(box){box.classList.remove("flash"); setTimeout(()=>box.classList.add("flash"),500);}
  }
});
let savedAud="todos"; try{savedAud=localStorage.getItem("wn-aud")||"todos"}catch(e){}
setAud(["personal","medico","dono","todos"].includes(savedAud)?savedAud:"todos");


const sel=document.getElementById("f-prog");
P.forEach(p=>{const o=document.createElement("option");o.value=p.id;o.textContent=p.nome;sel.appendChild(o);});
grid.addEventListener("click",e=>{
  const b=e.target.closest("[data-pick]"); if(!b) return;
  sel.value=b.dataset.pick;
  document.getElementById("contato").scrollIntoView({behavior:"smooth"});
  setTimeout(()=>document.getElementById("f-nome").focus({preventScroll:true}),400);
});
document.getElementById("lead").addEventListener("submit",e=>{
  e.preventDefault();
  const n=document.getElementById("f-nome"), w=document.getElementById("f-wpp");
  if(!n.value.trim()){n.focus();return;}
  if(!w.value.trim()){w.focus();return;}
  document.getElementById("ok").hidden=false;
});

;

/* ===== Conteúdo das páginas de programa =====
   Programas existentes: dados das páginas atuais da PTA (out/2026).
   Programas novos (status "soon"): proposta; tudo entre [colchetes duplos] ou marcado "a definir" precisa ser confirmado. */
const MENT={
  rafael:{i:"RT",n:"Rafael Tonietto",r:"Doutor em educação e especialista em vendas no digital. Fundador e CEO da Personal Trainer Academy."},
  andre:{i:"AA",n:"André Albuquerque",r:"Mestre em biomecânica, fundador da Personal Trainer Academy e CEO do Wenorth Club."},
  artur:{i:"AM",n:"Artur Monteiro",r:"CEO do Mães em Forma."},
  julio:{i:"JM",n:"Júlio Muniz",r:"Head de Marketing e sócio da Personal Trainer Academy e do Grupo Wenorth. Mais de R$200 mil investidos em tráfego por mês, mais de 50 lançamentos digitais e 7 anos de experiência em funis e lançamentos."}
};
const D={
summit:{
  kicker:"Evento presencial · Curitiba/PR",
  title:"O evento que transforma bons profissionais em profissionais [reconhecidos]",
  sub:"Ciência do treino com aplicação prática em máquinas no palco, e um método de posicionamento, conteúdo e vendas. O conteúdo não é gravado: só quem está lá vive.",
  chips:["Presencial em Curitiba","Data a anunciar","Para personal, academias e estúdios"],
  cta:"Garantir ingresso",
  temasTitle:"O que você vai [ver no palco]",
  temas:["Treino e gestão","Posicionamento","Conteúdo que atrai clientes","Vendas pelo WhatsApp","Uso de IA no dia a dia","Precificação e recorrência","Retenção de alunos","Liderança de equipes"],
  para:{sim:["Personal trainers em início de carreira","Personal que já atende e quer crescer","Donos e gestores de academias e estúdios","Professores de academia"]},
  stat:["5.000+","vidas transformadas, segundo a Personal Trainer Academy"],
  oferta:{tipo:"ingressos",note:"Todos os ingressos dão acesso ao conteúdo completo. A diferença está na área da plateia e nas experiências extras.",href:"https://ptadigital.com.br/summit-2027",tiers:[
    {n:"Smart Pass",i:["Acesso ao evento","Certificado","Pasta e caneta"]},
    {n:"Gold Pass",hot:true,i:["Tudo do Smart","Área Gold na plateia","MiniBand PTA","Curso Biomecânica na Prática","Open bar de 2h no happy hour"]},
    {n:"VIP Pass",i:["Tudo do Gold","Área VIP na plateia","Coffee break na sala VIP","Acesso aos professores no backstage","Caderninho"]}]},
  faq:[["Serve para quem está começando?","Sim. O conteúdo atende iniciantes e quem já atende e quer crescer."],["O evento será gravado?","Não. O conteúdo é exclusivo para quem estiver presente."],["Qual a diferença entre os ingressos?","Todos dão acesso ao conteúdo completo. A diferença está na área da plateia, nos materiais e nas experiências extras."]]
},
next:{
  kicker:"Imersão presencial · 3 dias",
  title:"Saia da imersão com o seu digital [pronto para vender]",
  sub:"Três dias na sede da Personal Trainer Academy para fotografar, gravar, criar dois produtos digitais e montar a página de vendas. O objetivo é chegar a mais de R$10 mil por mês com consultoria online.",
  chips:["3 dias · 20 horas","Sede da PTA, Curitiba","Para personal começando no digital"],
  cta:"Quero a Next Experience",
  dores:["Você é bom tecnicamente, mas pouca gente te encontra no Instagram.","Não tem foto nem vídeo profissional para postar.","Não sabe o que vender online, nem por quanto.","Tentou montar página e automação sozinho e travou na parte técnica."],
  tese:"Você não sai com anotações. Sai com o [digital montado].",
  oque:"Uma imersão prática: cada etapa termina com algo pronto para usar no dia seguinte.",
  passos:[["Produzir","Sessão de fotos e gravação de vídeos profissionais, mesmo para quem nunca gravou."],["Criar","Critérios de conteúdo, estratégia de reels e dois produtos digitais prontos."],["Vender","Página de vendas em quatro etapas e automação configurada."]],
  modTitle:"O que acontece nos [três dias]",
  modulos:[["Sessão de fotos","Fotos profissionais para as redes sociais.",[]],["Gravação de vídeo","Vídeos profissionais, inclusive para iniciantes.",[]],["Conteúdo para o feed","Critérios de criação de posts.",[]],["Reels","Crescimento de seguidores e faturamento.",[]],["Produtos digitais","Dois produtos prontos para vender.",[]],["Automação","Automação de vendas.",[]],["Página de vendas","Fotos, logo, configuração e entrega com acesso.",[]]],
  entregaveis:["Fotos e vídeos profissionais","Dois produtos digitais prontos","Página de vendas no ar","Automação de vendas configurada"],
  oferta:{tipo:"aplicacao",inclui:["3 dias de imersão, 20 horas","Kit didático com apostila e caneta","Bônus: curso Biomecânica na Prática","Bônus: livro de marketing para personal","Bônus: camiseta personalizada"],extra:"Leve computador e celular."},
  faq:[["É presencial?","Sim. São três dias em Curitiba, com 20 horas no total."],["Preciso já criar conteúdo?","Não. A imersão inclui a produção de fotos e vídeos."],["O que preciso levar?","Computador e celular."],["E depois da imersão?","Quem quer acompanhamento para vender a consultoria online segue para a Mentoria Scala."]]
},
scala:{
  kicker:"Mentoria híbrida · 6 meses",
  title:"Dobre a sua renda em 6 meses [sem largar o presencial]",
  sub:"Mentoria para personal trainers, fisioterapeutas e nutricionistas montarem a consultoria online e venderem pelo Instagram, com acompanhamento até a execução.",
  chips:["6 meses","Online + 1 dia presencial","Entrada contínua"],
  cta:"Quero dobrar minha renda",
  dores:["Sua agenda está cheia e a renda bateu no teto das horas do dia.","Você posta, mas os posts não viram clientes.","Não sabe como montar e precificar uma consultoria online.","Começa sozinho, perde o ritmo e para no meio."],
  tese:"Primeiro, vender melhor o seu tempo. [Depois, crescer além dele.]",
  oque:"Um método em cinco etapas e um guia de seis faixas, da branca à marrom, com uma meta de clientes online por nível, até 20 a 30 clientes.",
  passos:[["Posicionamento","Quem você atende e por que escolhem você."],["Feed","Conteúdo que mostra autoridade."],["Stories","Relacionamento que aquece para a venda."],["Vendas","Conversa e fechamento."],["Produto","A consultoria online estruturada."]],
  para:{sim:["Personal trainers, fisioterapeutas e nutricionistas que atendem clientes","Quem quer aumentar o faturamento sem largar o presencial","Quem tem menos de mil seguidores e quer começar"],nao:["Quem espera resultado sem executar as tarefas","Quem não quer aparecer no Instagram","Quem não tem base de clientes presenciais","Quem já vende online e quer escalar: o caminho é a Mentoria Black"]},
  mentores:["rafael","artur"],convidados:"Equipe de execução: Thiago Coelho e Júlio Muniz (marketing e vendas). Convidados de turmas anteriores: Odam Brito, Vanessa Personal e Juarez Trancoso.",
  provas:[["10 consultorias em 3 dias","Vendidas depois de aplicar o método.","Charline"],["Faturamento dobrado","Resultado relatado em vídeo.","Sheila"],["500+ mentorados","Já passaram pela Scala.","Mentoria Scala"]],
  oferta:{tipo:"aplicacao",inclui:["Encontros ao vivo em grupo a cada 2 semanas","2 sessões individuais: com Rafael no mês 1 e com um mentor no mês 5","1 dia presencial em Curitiba ou em Alphaville/SP","Suporte do Anjo: acompanhamento quinzenal","Raio-X individual gravado do seu perfil","Guia das 6 faixas","Grupo exclusivo no WhatsApp"],garantia:"Se você cumprir pelo menos 80% do checklist de execução e não alcançar o resultado do seu nível, devolvemos o investimento. As regras completas são confirmadas pelo time comercial."},
  faq:[["Preciso ter muitos seguidores?","Não. A maior parte dos mentorados começa com menos de mil seguidores."],["Fisioterapeutas e nutricionistas podem participar?","Sim."],["Quanto tempo preciso por semana?","O tempo de executar as tarefas do método, mais os encontros quinzenais."],["O dia presencial está incluído?","Sim, está incluído no investimento."],["Qual a diferença para a Black?","A Scala ensina a vender melhor o seu tempo. A Black é para quem já vende online e quer faturar sem depender da agenda."]]
},
black:{
  kicker:"Mentoria híbrida · 12 meses",
  title:"Fature com o digital [sem depender da sua agenda]",
  sub:"Doze meses para quem já vende online construir infoproduto, funil, tráfego e lançamento. A projeção do programa chega a R$50 mil por mês vindos só do digital.",
  chips:["12 meses","3 encontros presenciais de 2 dias","Para quem fatura R$20 a 50 mil/mês"],
  cta:"Quero fazer minha aplicação",
  dores:["Sua renda para quando você para de atender.","Você vende consultoria, mas não tem um produto que escala.","Não tem funil nem tráfego rodando com previsibilidade.","Cada lançamento depende de sorte."],
  tese:"A Scala ensina a vender o seu tempo. [A Black ensina a vender sem ele.]",
  modTitle:"Seis competências, [duas por bimestre]",
  modulos:[["Posicionamento e narrativa","A história e a promessa que sustentam a sua marca.",[]],["Infoproduto","O produto que vende sem a sua hora.",[]],["Copy","Textos de página, anúncio e conteúdo.",[]],["Funil de vendas","CRM e follow-up.",["CRM","Follow-up"]],["Tráfego pago","Anúncios para alimentar o funil.",[]],["Lançamento","Planejamento e execução do lançamento.",[]]],
  para:{sim:["Personal trainers, fisioterapeutas, nutricionistas e médicos","Quem já vende online e fatura de R$20 mil a R$50 mil por mês","Quem tem verba para tráfego durante o programa"],nao:["Quem ainda não vende nada online: o caminho é a Mentoria Scala","Quem não tem verba para tráfego","Quem espera que outra pessoa monte a estrutura","Quem já tem time e processos consolidados"]},
  mentores:["rafael","artur","andre"],convidados:"Convidados: Ivan Querino, Jober Chaves, Noara Pozzer e Gilson Neves. A equipe de marketing e vendas da PTA dá apoio à execução.",
  provas:[["Lucro mais que triplicado","Com faturamento acima de R$120 mil.","Guilherme Chinellato"],["Ticket maior","Ofertas reorganizadas e lançamento do infoproduto Fecha Zíper.","Franciele Veronese"],["720 alunos ativos","E mais de 330 mil seguidores.","Odam Brito"]],
  oferta:{tipo:"aplicacao",inclui:["12 encontros ao vivo com análise do seu caso","12 sprints de implementação, um por mês","1:1 de uma hora na entrada","3 encontros presenciais de 2 dias, em São Paulo e Curitiba","Red Button: 2 acessos por ano a um mentor","Acesso ao Wenorth Club","Acompanhamento do Anjo: contato quinzenal","Grupo exclusivo no WhatsApp"],garantia:"Se você cumprir pelo menos 80% do checklist de execução e não alcançar o resultado do seu nível, devolvemos o investimento."},
  faq:[["Qual a diferença para a Scala?","A Scala foca em vender melhor o seu tempo. A Black foca em vender sem depender dele."],["Onde são os presenciais?","Em São Paulo e Curitiba."],["Quando começa?","A entrada é contínua. A coordenação responde à aplicação em até 48 horas."],["A projeção de R$50 mil é garantida?","Não. É uma projeção (100 alunos de consultoria a R$297 e 210 assinantes de infoproduto a R$97 por mês) e o resultado depende da execução de cada profissional."]]
},
biomecanica:{
  kicker:"Curso gravado · Formação técnica",
  title:"Técnica, ciência e posicionamento para ser [o treinador mais desejado] da sua cidade",
  sub:"O curso mais vendido da Personal Trainer Academy, agora totalmente atualizado. Biomecânica aplicada, métodos de treinamento, periodização, avaliação, reabilitação e posicionamento profissional em um só método.",
  chips:["Online gravado","Aulas curtas (microlearning)","Certificado chancelado pelo ACSM"],
  cta:"Quero o Biomecânica na Prática",
  facts:[["Formato","Online gravado"],["Carga horária","a definir"],["Módulos","7"],["Professor","André Albuquerque"],["Certificado","ACSM + físico"]],
  dores:["Só conhecimento técnico não está fazendo você se destacar.","Só saber vender não sustenta ninguém no mercado por muito tempo.","Seus alunos evoluem, mas sem consistência.","Você fica inseguro ao treinar aluno com dor ou lesão."],
  tese:"Técnica sem posicionamento não aparece. Posicionamento sem técnica [não se sustenta].",
  oque:"O método combina biomecânica, periodização e neurociência em três pilares e oito etapas, da primeira conversa com o aluno à entrega de resultado.",
  passos:[["Prescrição","Target do aluno e controle do treinamento: frequência, volume e técnicas de intensificação."],["Técnica","Exercício Alpha, expansão muscular, variações biomecânicas e fusão mente-músculo."],["Posicionamento","Experiência e resultado do aluno, provas sociais e o seu posicionamento como referência."]],
  modTitle:"Sete módulos, [do primeiro passo à referência]",
  modulos:[
    ["Fundação Biomecânica na Prática","Primeiros passos e a engrenagem para atrair e reter alunos de alto valor.",["Planilha 10K"]],
    ["Target do aluno e avaliação","Avaliar com precisão para prescrever melhor e valorizar o seu trabalho desde o início.",["Perfil DISC","Postural e funcional","Composição corporal","Neuromuscular","Biomecânica"]],
    ["Arquitetura da musculação","Fundamentos avançados e análise biomecânica vetorial em 4 passos.",["Sobrecarga","Intensidade x volume","Alavancas","Análise das máquinas"]],
    ["Maestria na sessão de treino","As 8 etapas do método aplicadas, com execução de membros superiores, inferiores e core.",["18 técnicas de intensificação","Modelos de 2 a 6x por semana","Comprimento muscular","Uni e bilateral"]],
    ["Avaliação e reabilitação de lesões","Compreender, avaliar e prescrever para as lesões mais comuns na musculação.",["Coluna","Joelho","Ombro","Quadril","Cotovelo"]],
    ["Gestão do personal","Organização e contratos para lucrar com estabilidade.",["Modelos de contrato","Organização financeira"]],
    ["Personal de valor","Atrair, vender e se posicionar como referência.",["Conteúdo para redes","Captação de alto valor","Script de vendas"]]
  ],
  capaz:["Avaliar o aluno com precisão, do perfil comportamental à biomecânica","Prescrever e periodizar com base em evidência","Treinar com segurança alunos com lesões comuns","Organizar contratos, finanças e se posicionar para atrair alunos de alto valor"],
  mentores:["andre"],
  oferta:{tipo:"checkout",h2:"Garanta o seu [acesso]",formSub:"Deixe seus dados e o time envia o link de compra pelo WhatsApp.",inclui:["Formação completa em aulas curtas (microlearning) [[carga horária e número de aulas a definir]]","Certificado internacional chancelado pelo ACSM","Certificado físico em metal ou acrílico, entregue em casa","Workbook Biomecânica na Prática 2.0","Box com 3 livros: Biomecânica Aplicada à Reabilitação de Lesões, Hipertrofia Máxima e Guia Definitivo de Marketing para Personal Trainers","Biblioteca com os 100 artigos mais recentes sobre hipertrofia, reabilitação e treinamento","Comunidade Biomecânica na Prática 2.0 Club","Bônus: Script de vendas para Direct e WhatsApp","Bônus: Checklist do engajamento digital","Bônus: Mapa da consultoria online"],garantia:"7 dias de garantia. [[confirmar condições]]"},
  faq:[["É uma pós-graduação?","Não. É uma especialização prática para aprimoramento técnico e profissional de personal trainers, sem caráter de pós-graduação ou mestrado acadêmico."],["Como são as aulas?","Aulas curtas e diretas, no formato microlearning, com entregáveis e ferramentas para usar no mesmo dia."],["Recebo certificado?","Sim. Certificado internacional chancelado pelo ACSM e um certificado físico entregue em casa após a conclusão."]]
},
mco:{
  kicker:"Curso gravado · Negócios",
  title:"O mapa para estruturar e vender a sua [consultoria online]",
  sub:"Para o personal que quer parar de depender de indicação e começar a vender online, mesmo com poucos seguidores. Não é um curso teórico: cada aula termina com uma ação prática.",
  chips:["Online gravado","Acesso vitalício","Com Rafael Tonietto"],
  cta:"Quero acesso ao MCO",
  facts:[["Formato","Online gravado"],["Módulos","6, em vídeo"],["Acesso","Vitalício, com atualizações"],["Materiais","Planilhas de estrutura"],["Professor","Rafael Tonietto"]],
  dores:["Seus clientes chegam só por indicação.","Você posta e os posts não viram clientes.","Acha que precisa de muitos seguidores para vender online.","Não sabe quanto cobrar nem como entregar a consultoria."],
  tese:"Consultoria online não depende de seguidores. Depende de [estrutura].",
  modTitle:"Seis módulos, [uma ação por aula]",
  modulos:[["[[Título do módulo 1]]","Os títulos dos módulos estão em imagens na página atual. Preencher com o time.",[]],["[[Título do módulo 2]]","",[]],["[[Título do módulo 3]]","",[]],["[[Título do módulo 4]]","",[]],["[[Título do módulo 5]]","",[]],["[[Título do módulo 6]]","",[]]],
  capaz:["Estruturar o seu serviço de consultoria online","Se posicionar para o público certo","Transformar seguidores em clientes pagantes","Definir preço e oferta, e organizar rotina e entrega"],
  mentores:["rafael"],
  oferta:{tipo:"checkout",h2:"Garanta a sua [vaga]",formSub:"Deixe seus dados e o time envia o link de compra pelo WhatsApp.",inclui:["6 módulos em vídeo","Materiais de apoio e planilhas de estrutura","Acesso vitalício, com atualizações"],garantia:"[[Garantia a confirmar]]"},
  faq:[["Preciso ter muitos seguidores?","Não. O método foi pensado para quem está começando com poucos seguidores."],["É um curso teórico?","Não. Cada aula termina com uma ação prática."],["Qual o próximo passo depois do MCO?","Quem quer acompanhamento para executar segue para a Mentoria Scala."]]
},
"academia-360":{
  kicker:"Imersão presencial · 3 dias",
  title:"Três dias para olhar a sua academia [por inteiro]",
  sub:"Imersão no Wenorth Club para donos de academia e estúdio. Da estratégia à operação: números, preço, retenção, equipe, processos, vendas, marketing e organização do salão, com um plano de 90 dias construído a partir dos casos reais dos participantes.",
  chips:["3 dias presenciais","Wenorth Club, Curitiba","Estratégia e operação"],
  cta:"Quero aplicar",
  dores:["Você não sabe ao certo quanto cada aluno dá de margem.","O aluno cancela no terceiro mês e ninguém percebe antes.","A visita chega e ninguém conduz até a matrícula.","Tudo na academia depende de você."],
  tese:"A academia que cresce é a que [conhece os próprios números].",
  oque:"Três dias de conteúdo aplicado à sua academia, com um board em que cada dono leva um caso real para o grupo discutir.",
  passos:[["Diagnóstico","Antes da imersão, você envia os números da academia: matrículas, cancelamentos, ticket e equipe."],["Imersão","Três dias de pilares, mentoria coletiva e board com casos reais."],["Plano de 90 dias","Você volta com as prioridades e o plano, com acompanhamento."]],
  modTitle:"Da estratégia à [operação]",
  modulos:[["Números e indicadores","Os indicadores que o dono precisa acompanhar toda semana.",["Ticket médio","Cancelamentos","Custo por aluno","Ocupação"]],["Precificação e margem","Planos, reajustes e custos.",["Tabela de planos","Margem por serviço"]],["Retenção","Os sinais de cancelamento e como agir antes.",["Recepção do aluno novo","Régua de acompanhamento"]],["Equipe e remuneração","Contratar, treinar e remunerar com metas.",["Metas","Rituais de gestão"]],["Processos","Rotinas de abertura, atendimento e fechamento que não dependem do dono.",["Checklists","Rotina da recepção"]],["Vendas","Da visita à matrícula, conduzida por quem está na recepção.",["Roteiro da visita","Apresentação de planos","Follow-up"]],["Marketing local","O que implementar para atrair alunos do bairro.",["Google","Instagram","Parcerias locais"]],["Organização das máquinas e diferenciais","Layout, fluxo e zonas do salão, e o que faz o aluno escolher a sua academia.",["Zonas de treino","Serviços premium","Experiência do aluno"]],["Plano de 90 dias","Prioridades, prazos e responsáveis.",["Board com casos reais"]]],
  para:{sim:["Donos e sócios de academias e estúdios","[[faixa de faturamento a definir]]","Quem quer aplicar na própria academia, não só assistir"],nao:["Quem procura consultoria individual","Quem ainda não abriu a academia"]},
  entregaveis:["Diagnóstico e painel de indicadores","Tabela de planos e margem","Roteiro de vendas e checklist de processos","Plano de 90 dias com prioridades"],
  oferta:{tipo:"aplicacao",inclui:["3 dias de imersão no Wenorth Club","Diagnóstico antes da imersão","Board com casos reais","Plano de 90 dias","Acompanhamento pós-imersão [[formato a definir]]"]},
  faq:[["É consultoria individual?","Não. É uma imersão em grupo, com os casos de cada participante discutidos no board."],["Posso levar meu sócio?","[[A definir]]"],["E depois da imersão?","Quem quer levar o treinamento para dentro da academia, com a equipe, segue para o Academia Certificada."]]
},
lancamento:{
  kicker:"Imersão presencial · 3 dias",
  title:"Três dias para [gravar e lançar] o seu infoproduto",
  sub:"Turma de 10 a 15 pessoas no estúdio de podcast e no salão do Wenorth Club. Você chega com a ideia e sai com o produto gravado, a página e o plano de lançamento.",
  chips:["3 dias presenciais","Estúdio do Wenorth Club","Turma de 10 a 15 pessoas"],
  cta:"Quero aplicar",
  dores:["O produto está na cabeça há meses e nunca sai do papel.","Gravar em casa não fica com a qualidade que você quer.","Você não sabe como dividir o conteúdo em aulas.","O lançamento não tem data nem plano."],
  tese:"Você não sai com uma ideia melhor. Sai com o [produto gravado].",
  oque:"Uma imersão de produção: roteiro de manhã, gravação à tarde, com o cenário e a estrutura do clube.",
  passos:[["Roteirizar","Estrutura do produto e roteiro de cada aula."],["Gravar","Aulas no estúdio de podcast e execuções no salão."],["Lançar","Página de vendas e calendário de lançamento."]],
  modTitle:"O que acontece nos [três dias]",
  modulos:[["Estrutura do produto","Módulos, aulas e materiais.",[]],["Roteiro","Roteiro de cada aula.",[]],["Gravação no estúdio","Aulas teóricas com câmera e áudio profissionais.",[]],["Gravação no salão","Execuções de exercícios com o clube como cenário.",[]],["Página de vendas","Estrutura e texto.",[]],["Plano de lançamento","Datas, conteúdo e anúncios.",[]]],
  para:{sim:["Quem já tem audiência e clientes","Mentorados e alumni da Mentoria Black","Quem tem a ideia do produto definida"],nao:["Quem ainda não vende nada online: comece pela Next Experience"]},
  entregaveis:["Aulas do produto gravadas","Página de vendas estruturada","Calendário de lançamento","Material de divulgação gravado"],
  oferta:{tipo:"aplicacao",inclui:["3 dias de produção no Wenorth Club","Uso do estúdio de podcast e do salão","Roteiro e estrutura do produto","Página e plano de lançamento"]},
  faq:[["Qual a diferença para a Next Experience?","A Next é para quem está começando no digital. O Sprint é para quem já tem audiência e quer gravar um produto completo."],["Preciso levar equipamento?","Não. A gravação usa a estrutura do clube. [[confirmar]]"]]
},
"academia-certificada":{
  kicker:"Programa híbrido",
  title:"A sua equipe treinada [dentro da sua academia]",
  sub:"Os consultores da Personal Trainer Academy vão até a sua academia para um dia de treinamento com os profissionais. Depois, a equipe faz um treinamento de vendas e ganha cinco pós-graduações de bônus.",
  chips:["Híbrido","1 dia de treinamento na sua academia","Treinamento de vendas"],
  cta:"Quero certificar minha academia",
  dores:["Cada professor atende de um jeito.","A equipe não sabe vender personal nem planos.","Treinar a equipe fora tira gente do salão e custa caro.","O aluno não vê diferença entre a sua academia e a do lado."],
  tese:"O treinamento vai [até a sua academia].",
  oque:"O programa leva a metodologia da Personal Trainer Academy para dentro da sua academia, com a sua equipe.",
  passos:[["Visita","Um consultor vai até a academia para um dia de treinamento com os profissionais."],["Vendas","Treinamento de vendas para a equipe. [[formato a confirmar: online ou presencial]]"],["Formação","Cinco pós-graduações de bônus para os profissionais da academia."]],
  para:{sim:["Donos de academias e estúdios com equipe de professores","Quem quer padronizar o atendimento e a técnica da equipe"],nao:["Quem procura um programa só para o dono: veja o Academia 360"]},
  entregaveis:["Equipe treinada na própria academia","Treinamento de vendas concluído","Cinco pós-graduações para os profissionais","Certificação da academia [[selo e critérios a confirmar]]"],
  oferta:{tipo:"aplicacao",inclui:["1 dia de treinamento na sua academia com um consultor","Treinamento de vendas para a equipe","Bônus: 5 pós-graduações para os profissionais [[regras a confirmar]]","Certificação Academia Certificada [[a confirmar]]"]},
  faq:[["O consultor vai até a minha academia?","Sim. O dia de treinamento acontece na sua academia, com a sua equipe. [[Confirmar cidades atendidas e custo de deslocamento]]"],["Quem recebe as pós-graduações?","Os profissionais da academia. [[Confirmar quantos profissionais e quais pós]]"],["Qual a diferença para o Academia 360?","O Academia 360 acontece no Wenorth Club e é para o dono. No Academia Certificada, o treinamento vai até a academia e é para a equipe."]]
},
ia:{
  kicker:"Imersão presencial · 1 dia",
  title:"Saia com a IA [trabalhando para você]",
  sub:"Um dia prático no Wenorth Club para profissionais da saúde e do fitness e donos de academia. Você chega com as tarefas que mais tomam o seu tempo e sai com assistentes de IA funcionando. Não precisa saber programar.",
  chips:["1 dia presencial","Wenorth Club, Curitiba","Sem conhecimento técnico"],
  cta:"Quero aplicar",
  dores:["Você responde as mesmas perguntas no WhatsApp todos os dias.","Criar conteúdo toma horas da sua semana.","Avaliações, relatórios e planilhas ficam para a noite.","Você sabe que a IA ajuda, mas não sabe por onde começar."],
  tese:"Você sai com a IA [rodando], não com uma lista de ferramentas.",
  oque:"Antes do dia, você responde um diagnóstico rápido. No dia, cada oficina termina com uma solução montada no seu notebook, com um mentor ao lado.",
  passos:[["Diagnóstico","Antes do dia: o mapa das tarefas que mais tomam o seu tempo."],["Oficinas","Fundamentos, ferramentas e montagem dos assistentes, com mentor ao lado."],["Rotina","Você volta com os assistentes funcionando e um plano de 30 dias para usar no dia a dia."]],
  modTitle:"Uma base comum e [duas trilhas]",
  modulos:[["Fundamentos","Como a IA funciona e como pedir o que você precisa.",["Prompts","Cuidados com dados de saúde"]],["Trilha Profissionais","Para personal trainers, nutricionistas, fisioterapeutas e médicos.",["Atendimento no WhatsApp","Anamnese e relatórios","Conteúdo para redes","Acompanhamento de alunos e pacientes"]],["Trilha Academias","Para donos e gestores.",["Atendimento e agendamento de visitas","Reativação de alunos inativos","Relatórios de gestão","Rotinas da equipe"]],["Automação","Conectar a IA às ferramentas que você já usa.",["WhatsApp","Planilhas","Agenda"]]],
  para:{sim:["Personal trainers, nutricionistas, fisioterapeutas e médicos","Donos e gestores de academias e estúdios","Quem não tem conhecimento técnico"],nao:["Quem procura um curso teórico sobre IA"]},
  entregaveis:["Assistente de atendimento configurado","Biblioteca de prompts da sua rotina","Pelo menos uma automação funcionando","Plano de 30 dias de uso"],
  oferta:{tipo:"aplicacao",inclui:["1 dia de oficinas no Wenorth Club","Diagnóstico antes do dia","Mentores ao lado durante as oficinas","Modelos de prompts e automações","Suporte depois do dia [[formato a definir]]"],extra:"Leve notebook e celular."},
  faq:[["Preciso saber programar?","Não. As oficinas foram pensadas para quem só usou IA no básico."],["O que preciso levar?","Notebook e celular."],["E os dados dos meus alunos e pacientes?","Os fundamentos tratam dos cuidados com dados de saúde e privacidade ao usar IA."],["Serve para dono de academia e para profissional?","Sim. A base é comum e, nas oficinas, cada um segue a sua trilha."]]
},
escala:{
  kicker:"Programa híbrido · 8 semanas",
  title:"Mais contatos chegando, [mais clientes fechando]",
  sub:"Implementação de tráfego pago com acompanhamento para profissionais da saúde e do fitness e donos de academia. Ao final, os seus anúncios estão no ar e você sabe quanto custa cada novo cliente.",
  chips:["8 semanas ao vivo","1 dia presencial no Wenorth Club","Verba de anúncios à parte"],
  cta:"Quero aplicar",
  dores:["Os clientes chegam só por indicação.","Você já impulsionou posts e não viu retorno.","Não sabe quanto pode gastar para trazer um cliente.","Os contatos chegam no WhatsApp e ninguém responde a tempo."],
  tese:"Anúncio sem atendimento é [dinheiro perdido].",
  oque:"Oito semanas de encontros ao vivo, com uma tarefa de implementação por semana, e um dia presencial no Wenorth Club para revisar as campanhas com os mentores.",
  passos:[["Estruturar","Conta de anúncios, rastreamento e a oferta que vai para o anúncio."],["Anunciar","Campanhas no Instagram, no Facebook e no Google, com criativos gravados por você."],["Converter","Roteiro de atendimento no WhatsApp e acompanhamento do custo por cliente."]],
  modTitle:"Do anúncio [ao cliente]",
  modulos:[["Oferta e público","Para quem anunciar e o que oferecer.",["Aula experimental","Avaliação","Consultoria"]],["Estrutura","Conta de anúncios, pixel e rastreamento.",["Meta","Google"]],["Criativos","Vídeos e imagens que geram contato, gravados com o celular.",["Roteiros","Ganchos"]],["Campanhas","Configuração, orçamento e otimização.",["Instagram e Facebook","Google"]],["Atendimento","Do contato à matrícula ou ao fechamento.",["Roteiro no WhatsApp","Follow-up"]],["Números","Custo por contato, custo por cliente e retorno.",["Painel semanal"]]],
  para:{sim:["Personal trainers, nutricionistas, fisioterapeutas e médicos","Donos de academias e estúdios","Quem tem verba para investir em anúncios"],nao:["Quem não tem verba para anúncios durante o programa","Quem quer terceirizar o tráfego sem aprender"]},
  entregaveis:["Conta de anúncios e rastreamento configurados","Campanhas no ar","Roteiro de atendimento dos contatos","Painel com o custo por cliente"],
  oferta:{tipo:"aplicacao",inclui:["8 encontros ao vivo, um por semana","1 dia presencial no Wenorth Club","Revisão das campanhas pelos mentores","Modelos de roteiro e de atendimento","Grupo de acompanhamento"]},
  faq:[["Preciso ter verba para anúncios?","Sim. A verba é separada do programa. [[definir verba mínima sugerida]]"],["Serve para academia e para profissional?","Sim. O método é o mesmo; as ofertas e os exemplos mudam para cada caso."],["Qual a diferença para a Mentoria Black?","Na Black, o tráfego pago é uma de seis competências, em 12 meses, para quem já fatura de R$20 mil a R$50 mil por mês no digital. O Escala de Clientes é focado só em tráfego e atendimento, em 8 semanas."]]
},
"ignite-ads":{
  kicker:"Tráfego, funil e CRM · até 6 meses",
  title:"Do clique [ao cliente]",
  sub:"Tráfego, funil e controle de leads em um só sistema. O time do Grupo Wenorth cuida das campanhas no Meta e no Google, cria uma página nova por mês e implanta o CRM PTA para você acompanhar cada lead da entrada até a venda.",
  chips:["Plano trimestral ou semestral","Online, com reunião mensal","Verba de anúncios à parte"],
  cta:"Quero aplicar",
  dores:["Os clientes chegam de forma irregular, muitas vezes só por indicação.","Você investe em anúncios e não sabe exatamente o que deu retorno.","Os leads chegam, mas se perdem no meio do caminho.","Você não sabe em que etapa o cliente desistiu."],
  tese:"O problema não é só o anúncio. [É o sistema.]",
  oque:"Três pilares que trabalham juntos: o tráfego traz a pessoa certa, a página transforma o clique em lead e o CRM acompanha cada lead até a conversa de venda.",
  passos:[["Tráfego pago","Gestão das campanhas no Meta (Instagram e Facebook) e no Google: criação, configuração, monitoramento e otimização contínua, com o Google Meu Negócio implantado logo no início."],["Páginas e funis","Uma página nova por mês e ajustes de funil durante todo o contrato. O que não converte, a gente corrige."],["CRM PTA","Desenvolvido pela PTA a partir da experiência em atendimento ao cliente: cada lead acompanhado da entrada até a venda, sem mensalidade e com treinamento completo."]],
  modTitle:"A jornada, [da implantação à escala]",
  modulos:[["Implantação · até 15 dias","Campanhas, página, CRM e Google Meu Negócio.",[]],["Campanhas no ar · mês 1","Primeiros leads e primeiros dados.",[]],["Otimização · meses 2 e 3","Ajustes nas campanhas e no funil com base nos números.",[]],["Escala · meses 4 a 6","Consolidação, escala e mais previsibilidade.",[]]],
  para:{sim:["Personal trainers, nutricionistas, fisioterapeutas, médicos e donos de academia e estúdio","Quem já fez as primeiras vendas","Quem já tem um roteiro de vendas definido","Quem tem verba para investir em anúncios todo mês","Quem tem alguém para responder os leads rapidamente"],nao:["Quem ainda está validando o produto","Quem quer terceirizar a venda"]},
  mentores:["julio"],
  oferta:{tipo:"aplicacao",inclui:["Gestão de tráfego no Meta e no Google","1 página nova por mês e ajustes de funil","CRM PTA sem mensalidade, com treinamento","Implantação do Google Meu Negócio","Dashboard com atualização diária","Reunião mensal com o Júlio Muniz","Grupo no WhatsApp com resposta em até 24 horas"],extra:"Fica com você: a verba de anúncios, os criativos, o domínio e a hospedagem do site, o atendimento e o fechamento das vendas e o uso do CRM no dia a dia. Nós trazemos os leads e organizamos o processo. A venda é sua."},
  faq:[["O que o time faz e o que fica comigo?","O time cuida do tráfego, das páginas, do CRM e do acompanhamento. Você cuida da verba de anúncios, dos criativos, do domínio e da hospedagem do site e do atendimento e fechamento das vendas."],["A verba de anúncios está incluída?","Não. A verba é paga direto ao Meta e ao Google, separada do programa."],["O CRM tem mensalidade?","Não. O CRM PTA está incluído no programa, com treinamento completo."],["Em quanto tempo as campanhas vão ao ar?","A implantação leva até 15 dias. No primeiro mês, as campanhas já estão no ar trazendo os primeiros leads."],["Qual a diferença para o Escala de Clientes?","No Escala de Clientes você aprende a montar e rodar o seu próprio tráfego em 8 semanas. No Ignite ADS, o time do Grupo Wenorth faz o tráfego, as páginas e o CRM com você."]]
},
"autoridade-medica":{
  kicker:"Programa híbrido · 4 meses",
  title:"Seja o médico que o paciente [encontra e escolhe]",
  sub:"Marketing e produção de conteúdo para médicos: posicionamento, conteúdo que educa o paciente, gravação profissional no estúdio do Wenorth Club e um processo para transformar seguidores em consultas particulares. Tudo dentro das regras de publicidade do CFM.",
  chips:["4 meses","2 dias de gravação no Wenorth Club","Dentro das regras do CFM"],
  cta:"Quero aplicar",
  dores:["Você é referência no consultório, mas na internet quem aparece é outro colega.","Tem receio de publicar algo que vá contra as regras de publicidade do CFM.","Entre consultório, plantão e família, não sobra tempo para gravar.","Os seguidores até chegam, mas não viram consultas particulares."],
  tese:"Conteúdo que educa o paciente [é o que enche a agenda].",
  oque:"Quatro meses de encontros ao vivo, com uma entrega por semana, e dois dias no estúdio do Wenorth Club para gravar de uma vez o conteúdo dos meses seguintes.",
  passos:[["Posicionar","Especialidade, público e a mensagem que faz o paciente certo escolher você."],["Produzir","Linha editorial, roteiros e gravação em lote no estúdio, para postar sem precisar gravar toda semana."],["Converter","Perfil no Google, WhatsApp e secretária preparados para transformar interesse em consulta."]],
  modTitle:"Seis módulos, [do perfil à agenda]",
  modulos:[["Posicionamento médico","Para quem você é a melhor escolha e como dizer isso com ética.",["Nicho","Bio","Promessa sem sensacionalismo"]],["Publicidade médica na prática","O que a Resolução CFM nº 2.336/2023 permite e o que proíbe, com exemplos. [[validar com advogado de direito médico]]",["Preços","Antes e depois","Depoimentos","Bastidores"]],["Linha editorial","Pilares de conteúdo que geram confiança e respondem às dúvidas reais dos pacientes.",["Calendário de 90 dias","Banco de roteiros"]],["Gravação no estúdio","Dois dias no Wenorth Club gravando vídeos, cortes e podcast, com roteiro e direção.",["Estúdio de podcast","Teleprompter","Edição com IA"]],["Canais","Onde o paciente procura médico hoje e como aparecer em cada lugar.",["Instagram","YouTube","Perfil no Google","Busca local"]],["Da audiência à consulta","O caminho do seguidor até a consulta particular.",["WhatsApp","Roteiro da secretária","Retorno e indicação"]]],
  para:{sim:["Médicos de consultório que querem mais pacientes particulares","Quem quer depender menos de convênios e plantões","Especialistas que querem ser referência na sua área ou na sua cidade","Quem nunca gravou e quer começar do jeito certo"],nao:["Quem quer viralizar a qualquer custo ou prometer resultados","Quem não está disposto a aparecer em vídeo","Quem quer terceirizar tudo sem participar"]},
  entregaveis:["Posicionamento e bio revisados","Calendário editorial de 90 dias","Banco de roteiros da sua especialidade","Vídeos gravados no estúdio [[quantidade a definir]]","Perfil no Google otimizado","Roteiro de atendimento para a secretária"],
  oferta:{tipo:"aplicacao",inclui:["Encontros ao vivo semanais durante 4 meses","2 dias de gravação no estúdio do Wenorth Club","Aula com advogado especialista em direito médico [[a definir]]","Revisão do seu perfil e dos seus roteiros pelos mentores","Modelos de roteiro por especialidade","Grupo de acompanhamento"],extra:"Nos dias de gravação, leve a roupa com que você atende e as dúvidas mais comuns dos seus pacientes."},
  faq:[["Posso mostrar preço, antes e depois ou depoimentos?","A Resolução CFM nº 2.336/2023, em vigor desde 2024, mudou o que é permitido. O programa tem um módulo só sobre isso: o que pode, o que não pode e como fazer com segurança. [[validar com advogado de direito médico]]"],["Não tenho tempo para gravar toda semana. Funciona?","Sim. A proposta é gravar em lote: nos dois dias de estúdio você grava o conteúdo de meses."],["Serve para qualquer especialidade?","Sim. Os roteiros e os exemplos são adaptados à sua especialidade nos encontros."],["Preciso ter muitos seguidores?","Não. O foco é atrair o paciente certo, não aumentar o número de seguidores."],["Qual a diferença para o Escala de Clientes?","O Autoridade Médica constrói o seu posicionamento e o seu conteúdo. O Escala de Clientes é focado em anúncios pagos e pode ser o passo seguinte."]]
},
"patrimonio-medico":{
  kicker:"Programa híbrido · 10 semanas",
  title:"Médico ganha bem. [O desafio é o que fica.]",
  sub:"Organização financeira e investimentos para médicos: separar pessoa física e jurídica, pagar o imposto certo, proteger a renda e investir com método para construir patrimônio e independência financeira.",
  chips:["10 semanas ao vivo","1 encontro presencial no Wenorth Club","Sem venda de produtos financeiros"],
  cta:"Quero aplicar",
  dores:["Você ganha bem, mas no fim do mês sobra menos do que deveria.","Não sabe se paga imposto demais nem se a sua PJ está no regime certo.","O dinheiro fica parado na conta ou em produtos que o gerente do banco ofereceu.","Se você parar de atender, a renda para junto."],
  tese:"Renda alta não é patrimônio. [Método é.]",
  oque:"Dez semanas de encontros ao vivo, com uma tarefa prática por semana sobre os seus próprios números, e um encontro presencial no Wenorth Club para fechar o seu plano.",
  passos:[["Organizar","Raio-X das finanças da pessoa física e da PJ, orçamento e reserva de emergência."],["Proteger","Impostos, seguros e previdência: o que reduz o risco e o que só custa caro."],["Investir","Carteira por objetivo e plano de independência financeira com os seus números."]],
  modTitle:"Seis módulos, [da conta ao patrimônio]",
  modulos:[["Raio-X financeiro","Para onde vai o dinheiro, na pessoa física e no consultório.",["Fluxo de caixa","Padrão de vida","Renda de plantões"]],["PF, PJ e impostos","Pró-labore, distribuição de lucros, regimes tributários e as mudanças recentes na tributação de lucros e dividendos. [[validar com contador parceiro]]",["Simples ou Presumido","Carnê-leão","Dividendos"]],["Orçamento e reserva","Quanto gastar, quanto guardar e onde deixar a reserva de emergência.",["Orçamento","Reserva"]],["Proteção da renda","Seguros e previdência para quem depende da própria capacidade de trabalhar.",["Invalidez","Vida","Responsabilidade civil","Previdência"]],["Investimentos","Os fundamentos para investir sem depender do gerente do banco.",["Renda fixa e Tesouro","Fundos","Ações e FIIs","Diversificação"]],["Independência financeira","Quanto você precisa acumular e quanto investir por mês para chegar lá.",["Número da independência","Plano de aportes","Sucessão"]]],
  para:{sim:["Médicos com renda alta e pouco tempo para cuidar do dinheiro","Quem atende como PJ e tem dúvidas sobre impostos","Quem quer começar a investir ou organizar o que já tem","Residentes e recém-formados que querem começar do jeito certo"],nao:["Quem procura dica de ação ou o investimento da moda","Quem quer que alguém administre o dinheiro no seu lugar"]},
  entregaveis:["Raio-X das suas finanças, PF e PJ","Orçamento e reserva de emergência definidos","Checklist tributário para revisar com o seu contador","Mapa de proteção: seguros e previdência","Carteira por objetivo","Plano de independência financeira"],
  oferta:{tipo:"aplicacao",inclui:["10 encontros ao vivo, um por semana","1 encontro presencial no Wenorth Club","Planilhas de orçamento, reserva e independência financeira","Aula com contador especialista em médicos [[a definir]]","Plantão de dúvidas com planejador financeiro certificado [[formato a definir]]","Grupo de acompanhamento"],extra:"Conteúdo educacional. O programa não faz recomendação individual de investimento nem vende produtos financeiros."},
  faq:[["Vocês indicam onde investir?","Não. O programa ensina método e critérios para você decidir. Não há recomendação individual nem venda de produtos financeiros."],["Serve para residentes e recém-formados?","Sim. Começar cedo é uma das maiores vantagens nos investimentos."],["Preciso ter dinheiro investido para participar?","Não. O ponto de partida é organizar a renda que você já tem."],["Substitui o meu contador?","Não. Você sai com um checklist para revisar com ele e entender o que está sendo feito."],["Quem conduz?","[[Definir: planejador financeiro certificado e contador especialista em médicos]]"]]
},
club:{
  kicker:"Comunidade anual · por convite",
  title:"O lugar onde [o mercado] se encontra",
  sub:"Mais de 600 m² em Curitiba onde empresários, influenciadores, professores e marcas do fitness e do wellness treinam, gravam, estudam e fazem negócios.",
  chips:["Anual","Wenorth Club, Curitiba","Apenas por convite"],
  cta:"Pedir convite",
  oque:"O que os membros vivem no clube:",
  passos:[["Business","Mentorias, lançamentos digitais e conexões com outros setores."],["Education","Cursos e imersões."],["Wellness","Treino, conteúdo, podcast e eventos das marcas parceiras."]],
  para:{sim:["Alumni da Mentoria Black","Donos de academias e estúdios","Influenciadores e profissionais da saúde"]},
  stat:["50 mi+","de seguidores somados pela rede de amigos e convidados do clube"],
  oferta:{tipo:"aplicacao",inclui:["Acesso às instalações do clube","Encontros e eventos","Participação em conteúdo e podcast [[a definir]]","Eventos das marcas parceiras"]},
  faq:[["Como recebo um convite?","Por indicação de um membro ou do time. Você também pode pedir pelo formulário."]]
}
};

const prog=document.getElementById("view-prog"), home=document.getElementById("view-home");
const hl=s=>esc(s).replace(/\[\[(.+?)\]\]/g,'<mark class="todo">$1</mark>').replace(/\[(.+?)\]/g,'<em class="hl">$1</em>');
const sec=(cls,inner,id)=>`<section class="band pg-sec ${cls}"${id?` id="${id}"`:""}><div class="wrap">${inner}</div></section>`;
const head=(eb,t,sub)=>`<div class="pg-head"><p class="eyebrow">${esc(eb)}</p><h2>${hl(t)}</h2>${sub?`<p class="muted">${hl(sub)}</p>`:""}</div>`;
const ticks=(arr,x)=>`<ul class="ticks${x?" x":""}">${arr.map(i=>`<li><span>${hl(i)}</span></li>`).join("")}</ul>`;
const roman=["I","II","III","IV","V","VI"];
const SYM='<svg class="rose" viewBox="0 0 355 340" aria-hidden="true"><path d="M0 340 110 0h63l90 283h13L186 0h59l110 340H220L141 92 60 340Z" fill="currentColor"/></svg>';

function formHTML(p,d){
  return `<form class="pg-form" novalidate>
    <div class="field"><label for="pf-nome">Nome</label><input id="pf-nome" autocomplete="name" required></div>
    <div class="two">
      <div class="field"><label for="pf-wpp">WhatsApp</label><input id="pf-wpp" inputmode="tel" autocomplete="tel" required></div>
      <div class="field"><label for="pf-ig">@ do Instagram</label><input id="pf-ig"></div>
    </div>
    <div class="field"><label for="pf-fat">Faturamento mensal</label><select id="pf-fat"><option>Até R$10 mil</option><option>R$10 a 20 mil</option><option>R$20 a 50 mil</option><option>R$50 a 100 mil</option><option>Acima de R$100 mil</option></select></div>
    <button class="btn btn-primary" type="submit" style="justify-content:center">${esc(d.cta)} <span class="arrow">→</span></button>
    <p class="ok" hidden>Recebemos seus dados para ${esc(p.nome)}. Nesta versão de rascunho, o formulário ainda não está ligado ao CRM.</p>
  </form>`;
}

function renderProg(id){
  const p=byId[id], d=D[id];
  let h="";
  h+=`<section class="band dark pg-hero">${SYM}<div class="wrap">
    <p class="crumb"><a href="${L("programas")}">Programas</a> /${esc(FMT_LABEL[p.fmt])} / ${esc(p.nome)}</p>
    ${p.status==="soon"?'<p class="draft">Programa em desenvolvimento · conteúdo, preço e datas a confirmar</p>':""}
    <p class="eyebrow">${esc(d.kicker)}</p>
    <h1>${hl(d.title)}</h1>
    <p class="lead muted">${hl(d.sub)}</p>
    <ul class="pg-chips"><li class="aud-chip">${audLabel(p.aud)}</li>${d.chips.map(c=>`<li>${esc(c)}</li>`).join("")}</ul>
    <div class="ctas"><button class="btn btn-primary" type="button" data-form="${id}">${esc(d.cta)} <span class="arrow">→</span></button></div>
    ${d.facts?`<div class="factbar">${d.facts.map(([k,v])=>`<div><span>${esc(k)}</span><b>${esc(v)}</b></div>`).join("")}</div>`:""}
  </div></section>`;

  if(d.dores) h+=sec("light",head("Você se reconhece?","Se isso [acontece com você]…")+`<div class="dores">${d.dores.map((t,i)=>`<div class="dor"><b>0${i+1}</b><p>${hl(t)}</p></div>`).join("")}</div>${d.tese?`<p class="tese">${hl(d.tese)}</p>`:""}`);

  if(d.passos) h+=sec("light alt",head("Como funciona",d.passos.length===3?"Três etapas, [um resultado]":"O [método]")+(d.oque?`<p class="oque">${hl(d.oque)}</p>`:"")+`<ol class="steps">${d.passos.map(([t,x],i)=>`<li class="step"><span class="n">Etapa ${i+1}</span><h3>${esc(t)}</h3><p>${hl(x)}</p></li>`).join("")}</ol>`);
  else if(d.oque && !d.modulos) h+=sec("light alt",`<p class="oque">${hl(d.oque)}</p>`);

  if(d.temas) h+=sec("light alt",head("Temas",d.temasTitle)+`<div class="tags" style="gap:10px">${d.temas.map(t=>`<span style="font-size:16px;padding:10px 18px">${esc(t)}</span>`).join("")}</div>`);

  if(d.modulos) h+=sec("light",head(p.fmt==="online"?"Módulos":"Conteúdo",d.modTitle)+(d.oque&&!d.passos?`<p class="oque">${hl(d.oque)}</p>`:"")+`<div class="mods">${d.modulos.map(([t,x,tags],i)=>`<div class="mod"><span class="n">${String(i+1).padStart(2,"0")}</span><div><h3>${esc(t)}</h3><p>${hl(x)}</p></div><div class="tags">${(tags||[]).map(g=>`<span>${esc(g)}</span>`).join("")}</div></div>`).join("")}</div>`);

  if(d.capaz) h+=sec("light alt",head("Resultado","Ao final, você será [capaz de]")+`<div class="roman">${d.capaz.map((t,i)=>`<div class="rm"><b>${roman[i]}</b><p>${hl(t)}</p></div>`).join("")}</div>`);

  if(d.docentes) h+=sec("light alt",head("Corpo docente",d.docentesTitle)+`<div class="tags" style="gap:10px">${d.docentes.map(t=>`<span style="font-size:15px;padding:9px 16px">${esc(t)}</span>`).join("")}</div><p class="note">Parte do corpo docente. Os professores variam por curso.</p>`);

  if(d.para) h+=sec("light",head("Para quem é","Feito para [quem]…")+`<div class="cols2"><div class="box"><h3>É para você se</h3>${ticks(d.para.sim)}</div>${d.para.nao?`<div class="box no"><h3>Não é para você se</h3>${ticks(d.para.nao,true)}</div>`:""}</div>`);

  if(d.entregaveis) h+=sec("light alt",head("Entregável","Você sai [com isso pronto]")+`<div class="roman">${d.entregaveis.map((t,i)=>`<div class="rm"><b>${roman[i]}</b><p>${hl(t)}</p></div>`).join("")}</div>`);

  if(d.mentores) h+=sec("light",head("Quem conduz","Mentores")+`<div class="people">${d.mentores.map(k=>{const m=MENT[k];return `<article class="person"><div class="mono" aria-hidden="true">${m.i}</div><h3>${m.n}</h3><p class="role">${m.r}</p></article>`}).join("")}</div>${d.convidados?`<p class="note">${esc(d.convidados)}</p>`:""}<p class="note">Mentores e convidados podem variar a cada turma.</p>`);
  else if(p.status==="soon") h+=sec("light",head("Quem conduz","Mentores")+`<p class="oque"><mark class="todo">Mentores a confirmar</mark></p>`);

  if(d.provas) h+=sec("light alt",head("Resultados","O que mudou [para quem fez]")+`<div class="quotes">${d.provas.map(([b,t,w])=>`<figure class="quote" style="margin:0"><p class="big">${esc(b)}</p><p>${esc(t)}</p><figcaption class="who">${esc(w)}</figcaption></figure>`).join("")}</div><p class="note">Resultados individuais. Dependem da execução de cada profissional.</p>`);
  if(d.stat) h+=sec("light alt",`<div class="stat-line"><b>${esc(d.stat[0])}</b><span>${esc(d.stat[1])}</span></div>`);

  const o=d.oferta;
  if(o){
    let inner="";
    if(o.tipo==="ingressos"){
      inner=`<div class="pg-head"><p class="eyebrow">Ingressos</p><h2>Escolha o seu <em class="hl">ingresso</em></h2><p class="muted">${esc(o.note)}</p></div>
      <div class="tiers">${o.tiers.map(t=>`<div class="tier${t.hot?" hot":""}"><h3>${esc(t.n)}</h3>${ticks(t.i)}<button class="btn ${t.hot?"btn-primary":"btn-ghost"}" type="button" data-form="${id}" data-tier="${esc(t.n)}">Quero o ${esc(t.n)} <span class="arrow">→</span></button></div>`).join("")}</div>`;
    } else {
      inner=`<div class="offer"><div>
        <p class="eyebrow">Inscrição</p>
        <h2>${hl(id==="club"?"Peça o seu [convite]":"Garanta a sua [vaga]")}</h2>
        <p class="price-sub">Preencha seus dados e um especialista do time entra em contato pelo WhatsApp com as datas e as condições da próxima turma.</p>
        <button class="btn btn-primary" type="button" data-form="${id}" style="justify-self:start">${esc(d.cta)} <span class="arrow">→</span></button>
      </div><div>
        <h3 style="color:var(--bone)">O que está incluído</h3>${ticks(o.inclui)}
        ${o.extra?`<p class="price-sub">${esc(o.extra)}</p>`:""}
        ${o.garantia?`<div class="guarantee"><b>Garantia</b>${esc(o.garantia)}</div>`:""}
      </div></div>`;
    }
    h+=`<section class="band dark pg-oferta" id="pg-oferta"><div class="wrap">${inner}</div></section>`;
  }

  if(d.faq) h+=sec("light faq",`<div><p class="eyebrow">Dúvidas</p><h2 style="margin-top:14px">Perguntas <em class="hl">frequentes</em></h2></div><div>${d.faq.map(([q,a])=>`<details><summary>${esc(q)}</summary><p>${hl(a)}</p></details>`).join("")}</div>`);

  const nx=(NEXTS[id]||[]).filter(k=>byId[k]);
  if(nx.length) h+=sec("light alt next-step",head("Próximo passo",`Depois do ${p.nome}, [o caminho continua]`,"Os programas que fazem sentido para quem conclui este.")+`<div class="rail all">${nx.map(k=>cardHTML(byId[k])).join("")}</div>`);

  h+=`<div class="pg-spacer"></div><div class="pg-sticky"><div class="wrap"><span class="nm">${esc(p.nome)}<small>${esc(d.kicker)}</small></span><button class="btn btn-primary" type="button" data-form="${id}">${esc(d.cta)}</button></div></div>`;
  prog.innerHTML=h;
  // a seção de FAQ usa o layout de duas colunas da home
  prog.querySelectorAll("section.faq").forEach(s=>s.classList.add("light"));
}

prog.addEventListener("click",e=>{
  const g=e.target.closest("[data-go]"); if(!g) return;
  const el=document.getElementById(g.dataset.go); if(el) el.scrollIntoView({behavior:"smooth"});
});
prog.addEventListener("submit",e=>{
  e.preventDefault();
  const f=e.target, n=f.querySelector("#pf-nome"), w=f.querySelector("#pf-wpp");
  if(!n.value.trim()){n.focus();return;}
  if(!w.value.trim()){w.focus();return;}
  f.querySelector(".ok").hidden=false;
});

/* ===== Próximo passo: cada programa aponta para os seguintes ===== */
const NEXTS={summit:["mco","academia-360"],biomecanica:["mco","scala"],mco:["next","scala"],next:["scala","escala"],ia:["escala","scala"],lancamento:["black","club"],scala:["black","escala"],black:["lancamento","club"],escala:["ignite-ads","black"],"ignite-ads":["ia","black"],"academia-360":["academia-certificada","escala"],"academia-certificada":["ia","club"],club:["summit"],"autoridade-medica":["escala","patrimonio-medico"],"patrimonio-medico":["autoridade-medica","club"]};

/* ===== Diagnóstico gratuito ===== */
const QS={
  perfil:{q:"Você é…",o:[["personal","Personal, nutricionista ou fisioterapeuta"],["medico","Médico (a)"],["dono","Dono de academia ou estúdio"]]},
  travaMed:{q:"O que mais te trava hoje?",o:[["pacientes","Atrair mais pacientes particulares"],["conteudo","Não sei o que postar nem como gravar"],["regras","Tenho receio das regras de publicidade do CFM"],["sobra","Ganho bem, mas sobra pouco no fim do mês"],["investir","Quero investir melhor e construir patrimônio"],["tempo","Falta tempo na minha rotina"]]},
  vende:{q:"Você já vende online?",o:[["nao","Ainda não"],["ate20","Sim, até R$20 mil por mês"],["mais20","Sim, mais de R$20 mil por mês"]]},
  trava:{q:"O que mais te trava hoje?",o:[["tecnica","Quero evoluir na técnica de treino"],["atrair","Atrair novos clientes"],["consultoria","Montar e vender a consultoria online"],["tempo","Falta tempo na minha rotina"],["escalar","Crescer sem depender da minha agenda"]]},
  travaDono:{q:"O que mais te trava hoje?",o:[["numeros","Não sei ao certo se a academia dá lucro"],["equipe","A equipe não está preparada"],["alunos","Chegam poucos alunos novos"],["processos","Tudo depende de mim"],["tempo","Falta tempo para a gestão"]]}
};
const diag=document.getElementById("diag");
let dA={};
const dSteps=()=>dA.perfil==="dono"?["perfil","travaDono"]:dA.perfil==="medico"?["perfil","travaMed"]:["perfil","vende","trava"];
function dRec(a){
  if(a.perfil==="medico") return {pacientes:["autoridade-medica","escala"],conteudo:["autoridade-medica","ia"],regras:["autoridade-medica","ia"],sobra:["patrimonio-medico","autoridade-medica"],investir:["patrimonio-medico","autoridade-medica"],tempo:["ia","autoridade-medica"]}[a.travaMed];
  if(a.perfil==="dono") return {numeros:["academia-360","academia-certificada"],equipe:["academia-certificada","academia-360"],alunos:["escala","academia-360"],processos:["academia-360","ia"],tempo:["ia","academia-360"]}[a.travaDono];
  const v=a.vende,t=a.trava;
  if(t==="tecnica") return ["biomecanica","mco"];
  if(t==="tempo") return ["ia",v==="nao"?"mco":"scala"];
  if(t==="atrair") return v==="nao"?["next","mco"]:["escala",v==="mais20"?"black":"scala"];
  if(t==="consultoria") return v==="nao"?["mco","scala"]:v==="ate20"?["scala","escala"]:["black","lancamento"];
  return v==="mais20"?["black","lancamento"]:["scala","mco"];
}
function dRender(){
  const steps=dSteps(), i=steps.findIndex(k=>!dA[k]);
  if(i===-1){
    const [a,b]=dRec(dA), pa=byId[a], pb=byId[b];
    diag.innerHTML=`<p class="eyebrow">Indicado para você</p>
      <div class="diag-result">${cardHTML(pa)}<div class="diag-side">
        <p class="muted">Também pode fazer sentido:</p>
        <a class="diag-alt" href="${L("programa-"+b)}"><b>${esc(pb.nome)}</b><span>${esc(pb.desc)}</span></a>
        <form class="diag-form" novalidate>
          <p><b>Receba o diagnóstico no WhatsApp</b></p>
          <div class="field"><label for="d-nome">Nome</label><input id="d-nome" autocomplete="name"></div>
          <div class="field"><label for="d-wpp">WhatsApp</label><input id="d-wpp" inputmode="tel" autocomplete="tel"></div>
          <button class="btn btn-dark" type="submit">Quero receber</button>
          <p class="ok" hidden>Recebemos. Nesta versão de rascunho, o formulário ainda não está ligado ao CRM.</p>
        </form>
        <button class="link" type="button" data-dreset>Refazer o diagnóstico</button>
      </div></div>`;
    return;
  }
  const k=steps[i], q=QS[k];
  diag.innerHTML=`<p class="diag-prog">Pergunta ${i+1} de ${steps.length}</p><h3>${esc(q.q)}</h3>
    <div class="diag-opts">${q.o.map(([v,t])=>`<button type="button" class="diag-opt" data-dk="${k}" data-dv="${v}"><span>${esc(t)}</span><span class="arrow" aria-hidden="true">→</span></button>`).join("")}</div>
    ${i>0?'<button class="link" type="button" data-dback>← Voltar</button>':""}`;
}
diag.addEventListener("click",e=>{
  const o=e.target.closest("[data-dk]");
  if(o){ if(o.dataset.dk==="perfil") dA={}; dA[o.dataset.dk]=o.dataset.dv; dRender(); return; }
  if(e.target.closest("[data-dback]")){ const s=dSteps(); const last=[...s].reverse().find(k=>dA[k]); delete dA[last]; dRender(); return; }
  if(e.target.closest("[data-dreset]")){ dA={}; dRender(); }
});
diag.addEventListener("submit",e=>{
  e.preventDefault();
  const n=diag.querySelector("#d-nome"), w=diag.querySelector("#d-wpp");
  if(!n.value.trim()){n.focus();return;} if(!w.value.trim()){w.focus();return;}
  diag.querySelector(".ok").hidden=false;
});
dRender();

/* ===== Páginas institucionais: O Wenorth e Para marcas ===== */
const page=document.getElementById("view-page");
const cells=arr=>`<div class="cells">${arr.map(([t,x])=>`<div class="cell"><h3>${esc(t)}</h3><p>${hl(x)}</p></div>`).join("")}</div>`;
function heroBlock(k,t,sub,chips,cta){
  return `<section class="band dark pg-hero">${SYM}<div class="wrap">
    <p class="eyebrow">${esc(k)}</p><h1>${hl(t)}</h1><p class="lead muted">${hl(sub)}</p>
    <ul class="pg-chips">${chips.map(c=>`<li>${esc(c)}</li>`).join("")}</ul>
    <div class="ctas">${cta}</div></div></section>`;
}
const ENV=[
  ["Vitrine de parceiros","O túnel de entrada, com produtos em prateleiras iluminadas. Um dos pontos mais fotografados do clube.",["Suplementação","Vestuário","Farmácia de manipulação"]],
  ["Recepção","A primeira impressão de quem chega, com a Gluteus Zone ao fundo.",["Parede de marca"]],
  ["Photo spot","Asa de LED no lounge da entrada: a foto de chegada de cada convidado.",["Naming do photo spot","Asa de LED na cor da marca"]],
  ["Salão multiesportes","Musculação, funcional e Hyrox no salão de pé-direito duplo, onde todo o conteúdo de treino é gravado.",["Leg Day Zone","Functional Training Zone","Pista de sled","Estação de avaliação"]],
  ["Gluteus Zone","A área mais filmada do treino feminino. O letreiro fica atrás de quem grava a execução.",["Naming da Gluteus Zone","Cenário fixo dos conteúdos"]],
  ["Recovery","Banheira de gelo, sauna e botas de compressão. A banheira é o momento que todos filmam.",["Recovery by","Painel atrás da banheira"]],
  ["Estúdio de podcast","A marca atrás de quem está no microfone, em todo corte do podcast.",["Podcast by","Placa na mesa","Painel lateral","Faixa no vidro"]],
  ["North Room","Palco das mentorias, cursos e imersões, também disponível para locação.",["North Room by","Parede de ativação","Tela de abertura"]],
  ["Vestiário","O espelho é o ponto de selfie pós-treino do clube.",["Espelhos by","Cosméticos, higiene e farmácia"]],
  ["Jardim suspenso","Jardim vertical com o nome da marca em letras iluminadas, visto de todo o mezanino.",["Jardim by","Letreiro iluminado"]]
];
function renderPage(k){
  let h="";
  if(k==="sobre"){
    h+=heroBlock("Business · Education · Wellness","O clube de negócios do [fitness e do wellness] no Brasil",
      "Um espaço de mais de 600 m² em Curitiba onde o mercado de fitness e wellness se encontra para treinar, criar conteúdo, gravar podcasts, lançar produtos e fazer negócios. É a casa do grupo Wenorth, que tem a Personal Trainer Academy como principal integrante.",
      ["600 m²+","Curitiba/PR","Apenas por convite"],
      `<a class="btn btn-primary" href="${L("programas")}">Ver os programas <span class="arrow">→</span></a><a class="btn btn-ghost" href="${L("marcas")}">Para marcas</a>`);
    h+=sec("light",head("O que acontece aqui","Um calendário vivo, [o ano inteiro]")+`<div class="journey">
      <div class="jcol"><p class="eyebrow">Business</p>${ticks(["Mentorias com empresários, donos de academias e estúdios e personal trainers do digital","Lançamentos de produtos digitais, gravados e transmitidos do clube","Conexões com empresários de outros setores, como construção, automotivo, aviação e varejo"])}</div>
      <div class="jcol"><p class="eyebrow">Education</p>${ticks(["Cursos e imersões da casa e de empresas convidadas","Aulas com os principais professores e doutores do país"])}</div>
      <div class="jcol"><p class="eyebrow">Wellness</p>${ticks(["Influenciadores, médicos, nutricionistas e fisioterapeutas treinando e produzindo conteúdo","Gravações no estúdio de podcast e no salão","Lançamentos, ativações e encontros das marcas parceiras"])}</div></div>`);
    h+=sec("light alt",head("Quem circula aqui","As pessoas que [movem o setor]")+cells([["Empresários","Donos de academias, estúdios e negócios do setor, e líderes de outros mercados."],["Influenciadores","Do fitness, do wellness, da saúde e do business."],["Professores e doutores","Os principais nomes da ciência do exercício no país."],["Profissionais da saúde","Médicos, nutricionistas e fisioterapeutas."],["Personal trainers","Profissionais que atendem a classe A."],["Marcas parceiras","As empresas que fazem parte do ecossistema."]]));
    h+=sec("light",head("O poder da recomendação","Quem indica [move o mercado]")+`<div class="stat-line"><b>30 mil+</b><span>personal trainers formados pela Personal Trainer Academy em todo o Brasil. Eles atendem, todos os dias, o público de maior renda do país, e esse cliente consome o que o treinador indica.</span></div>`);
    h+=sec("light alt",head("Quem conduz","Quem está à frente [do clube]")+`<div class="people">
      <article class="person"><div class="mono" aria-hidden="true">AA</div><h3>André Albuquerque</h3><p class="role">Mestre em biomecânica e CEO do Wenorth Club. 335 mil seguidores no Instagram e 47 mil no YouTube; a audiência soma 5 milhões de visualizações e 1,8 milhão de contas alcançadas por mês.</p></article>
      <article class="person"><div class="mono" aria-hidden="true">RT</div><h3>Rafael Tonietto</h3><p class="role">Doutor em educação, especialista em vendas no digital e CEO do Wenorth Club. 16 mil seguidores no Instagram.</p></article>
      <article class="person"><div class="mono" aria-hidden="true">PTA</div><h3>Personal Trainer Academy</h3><p class="role">A principal integrante do grupo Wenorth, com 36 pessoas no time. 56 mil seguidores no Instagram e 14 mil no YouTube.</p></article></div>`);
    h+=sec("light",head("O alcance","Uma rede de [50 milhões] de seguidores")+`<div class="roman">
      <div class="rm"><b>8,3 mi</b><p>inscritos no YouTube</p></div>
      <div class="rm"><b>46,2 mi</b><p>seguidores de 94 amigos e convidados</p></div>
      <div class="rm"><b>4,1 mi</b><p>seguidores de 46 professores</p></div>
      <div class="rm"><b>407 mil</b><p>seguidores da gestão: André, Rafael e PTA</p></div></div>
      <div class="tags" style="margin-top:32px;gap:8px">${["Júlio Balestrin · 7 mi","Aurélio Alfieri · 4 mi","Caio Signoretti · 4 mi","Juliane Coura · 4 mi","Zanon Macedo · 3 mi","Roberta Zuniga · 3 mi","Erasmo Viana · 2 mi","Andressa Barberini · 2 mi","Vevê Fit · 2 mi"].map(t=>`<span style="font-size:14px;padding:7px 14px">${esc(t)}</span>`).join("")}</div>
      <p class="note">Dados de 19/09/2026. Nomes citados como amigos e convidados de André Albuquerque e Rafael Tonietto; a presença de cada um depende de agenda e convite.</p>`);
    h+=`<section class="band dark pg-oferta"><div class="wrap"><div class="offer"><div><p class="eyebrow">Venha conhecer</p><h2>Rua Eng. Arthur Bettes, 419 · <em class="hl">Portão, Curitiba/PR</em></h2><p class="price-sub">O acesso ao clube é apenas por convite.</p></div><div><a class="btn btn-primary" href="${L("programa-club")}">Pedir convite <span class="arrow">→</span></a></div></div></div></section>`;
  } else {
    h+=heroBlock("Para marcas","A sua marca ao lado de [quem move o mercado]",
      "No Wenorth Club, a sua marca aparece onde as pessoas treinam, gravam e se fotografam, e chega às mãos de quem indica: personal trainers, profissionais da saúde, influenciadores e empresários do setor.",
      ["Naming de espaços","Mídia espontânea","Eventos e ativações"],
      `<button class="btn btn-primary" type="button" data-go="pg-form">Quero ser parceiro <span class="arrow">→</span></button>`);
    h+=sec("light",head("O que a sua marca vive aqui","Seis formas de [estar presente]")+cells([["Posicionamento","Estar ao lado dos principais professores, doutores e influenciadores do país."],["Venda e retorno","Acesso direto a quem compra e a quem indica: personal trainers, empresários e alunos."],["Eventos e integrações","Lançamentos, encontros e experiências dentro do clube."],["Entrega de produtos","A marca nas mãos de quem forma opinião."],["Ativações e naming","Espaços com o nome da marca, como Recovery by e Gluteus Zone by."],["Conteúdo e mídia espontânea","A marca no enquadramento de quem grava e posta."]]));
    h+=sec("light alt",head("Por que funciona","Onde as pessoas se fotografam, [a sua marca está]","Cada ambiente foi desenhado a partir de uma pergunta: onde as pessoas naturalmente tiram foto e gravam vídeo?")+`<div class="roman">
      <div class="rm"><b>30 mil+</b><p>personal trainers formados, que atendem o público classe A e indicam o que consomem</p></div>
      <div class="rm"><b>50 mi+</b><p>seguidores somados pela rede de amigos e convidados do clube</p></div>
      <div class="rm"><b>600 m²+</b><p>de ambientes pensados para foto, vídeo e podcast</p></div></div>`);
    h+=sec("light",head("Ambientes","Dez espaços, [cada um com dono]")+`<div class="mods">${ENV.map(([t,x,tags],i)=>`<div class="mod"><span class="n">${String(i+1).padStart(2,"0")}</span><div><h3>${esc(t)}</h3><p>${esc(x)}</p></div><div class="tags">${tags.map(g=>`<span>${esc(g)}</span>`).join("")}</div></div>`).join("")}</div><p class="note">Projeto em desenvolvimento. Os ambientes podem mudar até a inauguração.</p>`);
    h+=`<section class="band dark pg-oferta" id="pg-form"><div class="wrap"><div class="offer"><div>
      <p class="eyebrow">Parcerias</p><h2>Vamos montar a presença da <em class="hl">sua marca</em></h2>
      <p class="price-sub">Conte o que a sua marca procura. O time comercial responde com as opções de espaço, ativação e conteúdo.</p>
      <p class="price-sub">Rua Eng. Arthur Bettes, 419 · Portão · Curitiba/PR</p></div><div>
      <form class="pg-form" novalidate>
        <div class="two"><div class="field"><label for="m-nome">Nome</label><input id="m-nome" autocomplete="name" required></div>
        <div class="field"><label for="m-emp">Empresa</label><input id="m-emp" autocomplete="organization"></div></div>
        <div class="two"><div class="field"><label for="m-cargo">Cargo</label><input id="m-cargo"></div>
        <div class="field"><label for="m-wpp">WhatsApp</label><input id="m-wpp" inputmode="tel" autocomplete="tel" required></div></div>
        <div class="field"><label for="m-int">Interesse</label><select id="m-int"><option>Naming de espaço</option><option>Vitrine de parceiros</option><option>Eventos e ativações</option><option>Conteúdo e podcast</option><option>Ainda não sei</option></select></div>
        <button class="btn btn-primary" type="submit" style="justify-content:center">Quero ser parceiro <span class="arrow">→</span></button>
        <p class="ok" hidden>Recebemos. Nesta versão de rascunho, o formulário ainda não está ligado ao CRM.</p>
      </form></div></div></div></section>`;
  }
  page.innerHTML=h;
}
page.addEventListener("click",e=>{
  const g=e.target.closest("[data-go]"); if(!g) return;
  const el=document.getElementById(g.dataset.go); if(el) el.scrollIntoView({behavior:"smooth"});
});
page.addEventListener("submit",e=>{
  e.preventDefault();
  if(e.target.closest(".ap-form")) return; // o formulário de aplicação tem o próprio tratamento
  const f=e.target, req=[...f.querySelectorAll("[required]")].find(i=>!i.value.trim());
  if(req){req.focus();return;}
  f.querySelector(".ok").hidden=false;
});

/* ===== WhatsApp com o nome do programa ===== */
const wa=document.getElementById("wa");
function setWa(nome){
  const t=nome?`Olá! Quero saber mais sobre o programa ${nome}.`:"Olá! Quero ajuda para escolher um programa da Wenorth.";
  wa.href=`https://wa.me/${WA_NUM}?text=${encodeURIComponent(t)}`;
}

/* ===== Formulário em popup (todos os botões de inscrição abrem aqui) ===== */
const modal=document.getElementById("modal"), mForm=document.getElementById("modal-form");
const mProg=document.getElementById("mf-prog"), mTierWrap=document.getElementById("mf-tier-wrap"), mTier=document.getElementById("mf-tier");
mProg.innerHTML='<option value="">Ainda não sei</option>'+P.map(p=>`<option value="${p.id}">${esc(p.nome)}</option>`).join("");
let lastFocus=null;
function setTiers(id,tier){
  const o=D[id]&&D[id].oferta;
  const tiers=o&&o.tipo==="ingressos"?o.tiers.map(t=>t.n):[];
  mTierWrap.hidden=!tiers.length;
  mTier.innerHTML=tiers.map(t=>`<option${t===tier?" selected":""}>${esc(t)}</option>`).join("");
}
function openModal(id,tier){
  lastFocus=document.activeElement;
  const p=id&&byId[id];
  document.getElementById("modal-kicker").textContent=p?"Inscrição":"Fale com um especialista";
  document.getElementById("modal-title").textContent=p?p.nome:"Encontre o programa certo";
  mProg.value=p?id:"";
  setTiers(p?id:"",tier);
  mForm.querySelector(".ok").hidden=true;
  modal.hidden=false; document.body.classList.add("modal-open");
  setTimeout(()=>document.getElementById("mf-nome").focus(),50);
}
function closeModal(){ modal.hidden=true; document.body.classList.remove("modal-open"); if(lastFocus) lastFocus.focus(); }
mProg.addEventListener("change",()=>setTiers(mProg.value));
document.addEventListener("click",e=>{
  const t=e.target.closest("[data-form]");
  if(t){ e.preventDefault(); openModal(t.dataset.form,t.dataset.tier); return; }
  if(e.target.closest("[data-close]")) closeModal();
});
document.addEventListener("keydown",e=>{ if(e.key==="Escape"&&!modal.hidden) closeModal(); });
mForm.addEventListener("submit",e=>{
  e.preventDefault();
  const req=[...mForm.querySelectorAll("[required]")].find(i=>!i.value.trim());
  if(req){req.focus();return;}
  mForm.querySelector(".ok").hidden=false;
});

/* ===== Menu no celular ===== */
const mBtn=document.querySelector(".menu-btn"), mNav=document.getElementById("mnav");
function setMenu(open){ mNav.hidden=!open; mBtn.setAttribute("aria-expanded",open); mBtn.setAttribute("aria-label",open?"Fechar menu":"Abrir menu"); document.body.classList.toggle("menu-open",open); }
mBtn.addEventListener("click",()=>setMenu(mNav.hidden));
mNav.addEventListener("click",e=>{ if(e.target.closest("a")) setMenu(false); });
window.addEventListener("hashchange",()=>setMenu(false));

/* ===== Formulário de aplicação: uma pergunta por vez e agendamento da ligação =====
   A pessoa não vê programa indicado: quem indica é o vendedor. A sugestão do diagnóstico vai só no lead, para o vendedor.
   Ainda não envia para o CRM: o lead montado fica em window.WN_LEAD e passa por enviarLead(). */
const AQ={
  email:{t:"email",hello:true,q:"Qual é o seu e-mail?",ph:"voce@email.com"},
  nome:{t:"text",q:"Qual o seu nome completo?",ph:"Nome e sobrenome",ac:"name"},
  wpp:{t:"tel",q:"E o seu WhatsApp?",hint:"É por ele que o especialista vai falar com você.",ph:"(41) 99999-9999"},
  profissao:{q:"Qual é a sua área?",o:[["personal","Personal trainer"],["nutri","Nutricionista"],["fisio","Fisioterapeuta"],["medico","Médico (a)"],["dono","Dono (a) de academia ou estúdio"]]},
  instagram:{t:"text",q:"Qual o seu @ no Instagram?",hint:"Opcional. Ajuda o especialista a conhecer o seu trabalho.",ph:"@seuperfil",opt:true},
  vende:QS.vende,
  trava:QS.trava,
  fatProf:{q:"Quanto você fatura por mês hoje?",o:[["ate5","Até R$5 mil"],["5a10","De R$5 mil a R$10 mil"],["10a20","De R$10 mil a R$20 mil"],["20a50","De R$20 mil a R$50 mil"],["mais50","Acima de R$50 mil"]]},
  especialidade:{t:"text",q:"Qual a sua especialidade?",ph:"Ex.: dermatologia, ortopedia, clínica geral"},
  momento:{q:"Como você atende hoje?",o:[["residente","Sou residente ou recém-formado"],["consultorio","Tenho consultório particular"],["clinica","Atendo em clínica ou hospital"],["plantao","Vivo principalmente de plantões"]]},
  travaMed:QS.travaMed,
  fatMed:{q:"Quanto você fatura por mês hoje?",o:[["ate20","Até R$20 mil"],["20a50","De R$20 mil a R$50 mil"],["50a100","De R$50 mil a R$100 mil"],["mais100","Acima de R$100 mil"]]},
  negocio:{t:"text",q:"Qual o nome da sua academia ou estúdio?",ph:"Nome do negócio"},
  tipo:{q:"Que tipo de negócio você tem?",o:[["academia","Academia"],["pilates","Estúdio de pilates"],["personal","Estúdio de personal ou funcional"],["box","Box de cross training"],["outro","Outro"]]},
  alunos:{q:"Quantos alunos ativos você tem?",o:[["ate100","Até 100"],["100a300","De 100 a 300"],["300a600","De 300 a 600"],["mais600","Mais de 600"]]},
  fatDono:{q:"Qual o faturamento mensal do negócio?",o:[["ate30","Até R$30 mil"],["30a80","De R$30 mil a R$80 mil"],["80a200","De R$80 mil a R$200 mil"],["mais200","Acima de R$200 mil"]]},
  travaDono:QS.travaDono,
  investimento:{q:"O investimento varia conforme o formato e a duração do programa. Como você gostaria de seguir?",o:[["parcelado","Quero avaliar opções de parcelamento"],["info","Ainda não decidi, quero mais informações"],["avista","Pagamento à vista"]]}
};
const PROF_PERFIL={personal:"personal",nutri:"personal",fisio:"personal",medico:"medico",dono:"dono"};
let aA={}, aPos=0, aOrigem=null;
const aPerfil=()=>PROF_PERFIL[aA.profissao];
function aSteps(){
  const base=["email","nome","wpp","profissao"], fim=["investimento"];
  const p=aPerfil();
  if(p==="medico") return [...base,"especialidade","momento","travaMed","fatMed",...fim];
  if(p==="dono") return [...base,"negocio","tipo","alunos","fatDono","travaDono",...fim];
  if(p==="personal") return [...base,"instagram","vende","trava","fatProf",...fim];
  return [...base,"_","_","_","_",...fim]; // antes da área, a barra mostra um tamanho médio
}
// Indicação: parte do diagnóstico da home e inclui o Ignite ADS para quem já vende
function aRec(a){
  const p=aPerfil();
  let r=dRec({perfil:p,vende:a.vende,trava:a.trava,travaMed:a.travaMed,travaDono:a.travaDono})||[];
  if(p==="personal"&&a.trava==="atrair"&&a.vende==="mais20") r=["ignite-ads","black"];
  if(p==="dono"&&a.travaDono==="alunos") r=["escala","ignite-ads"];
  if(p==="medico"&&a.travaMed==="pacientes"&&(a.momento==="consultorio"||a.momento==="clinica")) r=["autoridade-medica","ignite-ads"];
  // quem veio da página de um programa que serve para o seu perfil vê esse programa primeiro
  if(aOrigem&&byId[aOrigem]&&byId[aOrigem].aud.includes(p)) r=[aOrigem,...r.filter(k=>k!==aOrigem)];
  return r.filter(k=>byId[k]).slice(0,2);
}
const aValid={
  email:v=>/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)||"Digite um e-mail válido.",
  nome:v=>v.trim().split(/\s+/).length>=2||"Digite o nome e o sobrenome.",
  wpp:v=>v.replace(/\D/g,"").length>=10||"Digite o WhatsApp com DDD.",
};
function aParam(k){
  const q=location.search.slice(1)||(location.hash.split("?")[1]||"");
  return new URLSearchParams(q).get(k);
}
function aUtm(){ const o={}; ["utm_source","utm_medium","utm_campaign","utm_content","utm_term"].forEach(k=>{const v=aParam(k); if(v) o[k]=v;}); return o; }
function aLead(){
  const [rec,alt]=aRec(aA);
  const label=(k,v)=>{const q=AQ[k]; return q&&q.o?(q.o.find(o=>o[0]===v)||[,v])[1]:v;};
  const respostas={}; aSteps().forEach(k=>{ if(AQ[k]&&aA[k]!==undefined) respostas[k]=label(k,aA[k]); });
  return {nome:aA.nome,email:aA.email,whatsapp:aA.wpp,perfil:aPerfil(),profissao:label("profissao",aA.profissao),
    sugestao_para_o_vendedor:[rec,alt].filter(Boolean),programa_de_origem:aOrigem,respostas,
    agendamento:aA.agenda||null,origem:aUtm(),pagina:location.href,criado_em:new Date().toISOString()};
}
function enviarLead(lead){
  // Próximo passo: enviar para o CRM aqui (webhook ou API). Por enquanto só guarda e registra.
  window.WN_LEAD=lead; console.info("Lead do formulário de aplicação",lead);
}
function aDias(){
  const out=[], d=new Date(); const sem=["DOM","SEG","TER","QUA","QUI","SEX","SÁB"];
  while(out.length<3){ d.setDate(d.getDate()+1); if(d.getDay()!==0&&d.getDay()!==6) out.push({iso:`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,"0")}-${String(d.getDate()).padStart(2,"0")}`,dia:sem[d.getDay()],data:String(d.getDate()).padStart(2,"0")+"/"+String(d.getMonth()+1).padStart(2,"0")}); }
  return out;
}
const A_HORAS=["09h00","10h00","11h00","14h00","15h00","16h00","17h00","18h00"];
function renderAplicar(){
  const steps=aSteps(), done=aPos>=steps.length;
  const bar=`<div class="ap-bar">${steps.map((_,i)=>`<i class="${i<aPos||done?"on":""}"></i>`).join("")}</div>`;
  const orig=aOrigem&&byId[aOrigem]?` · ${esc(byId[aOrigem].nome)}`:"";
  let h=`<section class="ap"><div class="wrap"><div class="ap-top"><p class="eyebrow">Aplicação${orig}</p><span>${done?"Concluído":`${aPos+1} de ${steps.length}`}</span></div>${bar}`;
  if(done){
    const dias=aDias(), sel=aA.agenda||{}, interesse=aOrigem&&byId[aOrigem]?` sobre o ${byId[aOrigem].nome}`:"";
    h+=`<div class="ap-step"><p class="ap-hello">Obrigado, ${esc(aA.nome.split(" ")[0])}. Recebemos a sua aplicação.</p>
      <p class="ap-intro">Um especialista vai ligar para você para entender o seu momento e indicar o programa certo.</p>
      <div class="ap-side ap-end">
        <div class="ap-sched"><h3>Escolha o melhor horário para a ligação</h3><p class="tz">Horário de Brasília</p>
          <div class="ap-days">${dias.map(d=>`<button type="button" data-adia="${d.iso}" class="${sel.dia===d.iso?"sel":""}"><small>${d.dia}</small>${d.data}</button>`).join("")}</div>
          ${sel.dia?`<div class="ap-slots">${A_HORAS.map(t=>`<button type="button" data-ahora="${t}" class="${sel.hora===t?"sel":""}">${t}</button>`).join("")}</div>`:""}
          ${sel.hora?`<p class="ap-done">Combinado: um especialista liga para você em ${esc(dias.find(d=>d.iso===sel.dia).data)}, às ${esc(sel.hora)}.</p>`:""}
        </div>
        <a class="btn btn-primary" href="https://wa.me/${WA_NUM}?text=${encodeURIComponent(`Olá! Acabei de preencher a aplicação${interesse}. Meu nome é ${aA.nome}.`)}" target="_blank" rel="noopener" style="justify-self:start">Prefiro falar agora no WhatsApp <span class="arrow">→</span></a>
      </div></div>`;
  } else {
    const k=steps[aPos], q=AQ[k], v=aA[k]||"";
    h+=`<div class="ap-step">${aPos>0?'<button class="ap-back" type="button" data-aback>← Voltar</button>':""}`;
    if(q.hello) h+=`<p class="ap-hello">Olá,</p><p class="ap-intro">Precisamos de algumas informações para indicar o programa mais adequado para o seu perfil.</p>`;
    if(k==="investimento") h+=`<p class="ap-hello">Obrigado pelo seu interesse. Você vai receber o contato de um especialista.</p><p class="ap-intro">Para priorizar a sua aplicação, responda só mais uma pergunta.</p>`;
    h+=`<h2>${esc(q.q)}</h2>${q.hint?`<p class="hint">${esc(q.hint)}</p>`:""}`;
    if(q.o){
      h+=`<div class="ap-opts" role="radiogroup">${q.o.map(([ov,t])=>`<button type="button" role="radio" aria-checked="${v===ov}" class="ap-opt${v===ov?" sel":""}" data-ak="${k}" data-av="${ov}">${esc(t)}</button>`).join("")}</div>`;
    } else {
      const inp=`<input class="ap-input" id="ap-in" type="${q.t==="tel"?"tel":q.t}" ${q.t==="tel"?'inputmode="tel" autocomplete="tel"':q.t==="email"?'autocomplete="email"':q.ac?`autocomplete="${q.ac}"`:""} placeholder="${esc(q.ph)}" value="${esc(v)}">`;
      h+=`<form class="ap-form" novalidate data-ak="${k}">${q.t==="tel"?`<div class="ap-tel"><b>+55</b>${inp}</div>`:inp}
        <p class="ap-err" aria-live="polite"></p>
        <button class="btn btn-primary ap-next" type="submit">${q.opt&&!v?"Pular":"Continuar"} <span class="arrow">→</span></button></form>`;
      if(q.hello) h+=`<p class="ap-legal">Ao continuar, você concorda em receber o contato do time Wenorth pelo WhatsApp e por e-mail.</p>`;
    }
    h+=`</div>`;
  }
  page.innerHTML=h+`</div></section>`;
  const inp=page.querySelector("#ap-in"); if(inp) inp.focus({preventScroll:true});
}
function aAvancar(){ aPos++; if(aPos>=aSteps().length) enviarLead(aLead()); renderAplicar(); window.scrollTo(0,0); }
page.addEventListener("click",e=>{
  if(!page.querySelector(".ap")) return;
  const o=e.target.closest("[data-ak][data-av]");
  if(o){
    if(o.dataset.ak==="profissao"&&aA.profissao!==o.dataset.av){ const keep={email:aA.email,nome:aA.nome,wpp:aA.wpp}; aA=keep; }
    aA[o.dataset.ak]=o.dataset.av; aAvancar(); return;
  }
  if(e.target.closest("[data-aback]")){ aPos=Math.max(0,aPos-1); renderAplicar(); return; }
  const d=e.target.closest("[data-adia]"); if(d){ aA.agenda={dia:d.dataset.adia}; renderAplicar(); return; }
  const t=e.target.closest("[data-ahora]"); if(t){ aA.agenda={...aA.agenda,hora:t.dataset.ahora}; enviarLead(aLead()); renderAplicar(); }
});
page.addEventListener("input",e=>{
  if(e.target.id!=="ap-in") return;
  const f=e.target.closest("form"), q=AQ[f.dataset.ak];
  f.querySelector(".ap-err").textContent="";
  if(q.opt) f.querySelector(".ap-next").firstChild.textContent=e.target.value.trim()?"Continuar ":"Pular ";
});
page.addEventListener("submit",e=>{
  const f=e.target.closest(".ap-form"); if(!f) return;
  e.preventDefault();
  const k=f.dataset.ak, v=f.querySelector("#ap-in").value.trim(), ok=aValid[k]?aValid[k](v):(AQ[k].opt||!!v||"Preencha para continuar.");
  if(ok!==true){ f.querySelector(".ap-err").textContent=ok; return; }
  aA[k]=v; aAvancar();
});
function abrirAplicar(){
  const o=aParam("programa"); if(o!==aOrigem){ aOrigem=byId[o]?o:null; aA={}; aPos=0; }
  renderAplicar();
}

/* ===== Rotas ===== */
const PAGES={sobre:"O Wenorth",marcas:"Para marcas",aplicar:"Aplicação"};
function route(){
  const h=(STATIC&&window.WN_ROUTE?window.WN_ROUTE:location.hash.slice(1)).split("?")[0];
  const pid=h.startsWith("programa-")?h.slice(9):null;
  const wasOther=!prog.hidden||!page.hidden;
  prog.hidden=page.hidden=home.hidden=true;
  document.body.classList.remove("has-sticky");
  if(pid && D[pid] && byId[pid]){
    renderProg(pid); prog.hidden=false; document.body.classList.add("has-sticky");
    document.title=byId[pid].nome+" · Wenorth"; setWa(byId[pid].nome); window.scrollTo(0,0);
  } else if(PAGES[h]){
    if(h==="aplicar") abrirAplicar(); else renderPage(h);
    page.hidden=false;
    document.title=PAGES[h]+" · Wenorth"; setWa(null); window.scrollTo(0,0);
  } else {
    prog.innerHTML=""; page.innerHTML=""; home.hidden=false;
    document.title="Wenorth Programas"; setWa(null);
    if(h){const el=document.getElementById(h); if(el) el.scrollIntoView();}
    else if(wasOther) window.scrollTo(0,0);
  }
}
window.addEventListener("hashchange",route);
route();
