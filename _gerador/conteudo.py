"""Conteúdo de todas as páginas do site WeNorth Club.

Fonte principal: "Descritivo do site WeNorth Club" (31/10/2026). Tudo que não está
no descritivo nem na home original vem marcado com F(nota, html).
"""
import re

AMBIENTES = [
    # slug, nome, imagem, descrição do descritivo, chamada, texto (home), presença de marca (home)
    ("vitrine-de-parceiros", "Vitrine de parceiros", "a01",
     "O primeiro corredor de quem entra, com produtos em prateleiras iluminadas.",
     "A vitrine é o primeiro contato de quem entra.",
     "O túnel de entrada expõe os produtos das marcas parceiras em prateleiras iluminadas. É o corredor por onde todos passam e um dos pontos mais fotografados do clube.",
     ["Suplementação", "Vestuário", "Farmácia de manipulação"]),
    ("recepcao", "Recepção", "a02",
     "A assinatura do clube, com a Gluteus Zone ao fundo. É o primeiro enquadramento de quem chega.",
     "A primeira impressão, em wellness.",
     "A recepção apresenta a assinatura do clube e, ao fundo, a Gluteus Zone sob o mezanino. É o primeiro enquadramento de quem chega.",
     ["Parede de marca", "Gluteus Zone ao fundo"]),
    ("photo-spot", "Photo spot do lounge", "a03",
     "Uma asa de LED sobre grade metálica, pensada para a foto de chegada de cada convidado.",
     "Um lugar feito para a foto.",
     "No lounge da entrada, uma asa de LED sobre grade metálica, com o nome da marca acima. É o ponto pensado para a foto de chegada de cada convidado.",
     ["Naming do photo spot", "Asa de LED na cor da marca"]),
    ("salao-multiesportes", "Salão multiesportes", "a04",
     "Musculação, treino funcional e Hyrox sob pé-direito duplo. É onde o conteúdo de treino é gravado. Inclui Leg Day Zone, Functional Training Zone e pista de sled.",
     "Cada área do salão tem nome e dono.",
     "Musculação, treino funcional e Hyrox no mesmo salão de pé-direito duplo, onde todo o conteúdo de treino é gravado. As zonas são setorizadas por pintura e letreiro na parede.",
     ["Leg Day Zone", "Functional Training Zone", "Pista de sled", "Estação de avaliação"]),
    ("gluteus-zone", "Gluteus Zone", "a05",
     "Sob o mezanino, uma parede inteira dedicada às máquinas de glúteo.",
     "A área mais filmada do treino feminino.",
     "Sob o mezanino, uma parede inteira dedicada às máquinas de glúteo. O letreiro fica exatamente atrás de quem grava a execução.",
     ["Naming da Gluteus Zone", "Cenário fixo dos conteúdos"]),
    ("recovery", "Recovery", "a06",
     "Banheira de gelo, sauna e botas de compressão em um ambiente de spa.",
     "O momento que todos filmam: a banheira de gelo.",
     "Banheira de gelo, sauna e botas de compressão num ambiente de spa. A marca fica no painel iluminado atrás da banheira.",
     ["Recovery by", "Sauna", "Compressão"]),
    ("estudio-de-podcast", "Estúdio de podcast", "a07",
     "Gravação com a academia ao fundo.",
     "A marca atrás de quem está no microfone.",
     "O convidado se fotografa sentado de frente para o microfone. A marca aparece na faixa do vidro, na placa da mesa e no painel lateral, com a academia ao fundo.",
     ["Podcast by", "Placa na mesa", "Painel lateral"]),
    ("north-room", "North Room", "a08",
     "Sala de mentorias, pós-graduações e imersões, também disponível para locação por empresas.",
     "Sala de mentorias, cursos e imersões.",
     "Palco das mentorias, pós-graduações e imersões, também disponível para locação por empresas. A parede de ativação é o fundo de toda foto de palestrante e turma.",
     ["North Room by", "Parede de ativação", "Tela de abertura dos eventos"]),
    ("vestiario", "Vestiário", "a09",
     "O espelho é o ponto de selfie pós-treino.",
     "O espelho é o ponto de selfie do clube.",
     "No espelho de corpo inteiro e nos espelhos das pias, a faixa da marca parceira. Aparece em toda foto pós-treino.",
     ["Espelhos by", "Cosméticos, higiene e farmácia"]),
    ("jardim-suspenso", "Jardim suspenso", "a10",
     "Um jardim vertical na parede externa, visto do mezanino e das estações de trabalho.",
     "A marca integrada ao verde.",
     "Na parede externa, um jardim vertical com o nome da marca em letras iluminadas, visível do mezanino e das estações de trabalho.",
     ["Jardim by", "Letreiro iluminado"]),
]

# Textos fictícios por ambiente: uso no dia a dia e oportunidade para a marca.
AMB_FIC = {
    "vitrine-de-parceiros": ("Quem chega para treinar, para uma aula da pós ou para gravar passa obrigatoriamente pelo corredor. A vitrine funciona como um showroom permanente: o produto fica à vista, com luz própria, no caminho de quem consome e de quem indica.",
                             "Para a marca parceira, é presença diária e física, não só digital. O produto é visto, comentado e fotografado por personal trainers, empresários e influenciadores antes mesmo de entrarem no salão."),
    "recepcao": ("A recepção organiza a chegada de alunos, convidados e equipes de gravação. É também onde começa a maior parte dos vídeos de bastidores: a câmera abre na parede de assinatura e segue para dentro do clube.",
                 "A parede de marca da recepção aparece em vídeos de chegada, stories e coberturas de eventos. É o enquadramento que abre a narrativa de quem visita o clube."),
    "photo-spot": ("O lounge é ponto de encontro antes e depois das atividades. O photo spot foi desenhado para a foto de chegada: luz controlada, fundo limpo e um elemento visual que identifica o lugar em qualquer post.",
                   "O naming do photo spot coloca o nome da marca acima da asa de LED, na cor dela. Cada convidado que registra a chegada leva a marca junto para o próprio perfil."),
    "salao-multiesportes": ("O salão concentra a rotina de treino do clube e a maior parte das gravações de conteúdo técnico. A setorização por zonas facilita a produção: cada área tem um cenário reconhecível e um propósito claro.",
                            "Cada zona pode receber o nome de uma marca, com pintura e letreiro na parede. O conteúdo de treino gravado ali carrega esse cenário em cada vídeo publicado."),
    "gluteus-zone": ("A parede de máquinas sob o mezanino reúne em um só ponto os equipamentos mais procurados no treino de membros inferiores. A posição do letreiro foi pensada para aparecer no fundo de quem grava a execução.",
                     "O naming da Gluteus Zone transforma a parede em cenário fixo. Como o conteúdo é gravado sempre do mesmo ângulo, a marca aparece de forma consistente em toda a série de vídeos."),
    "recovery": ("O Recovery reúne recursos de recuperação em um ambiente de spa, separado do ritmo do salão. É o espaço de pausa depois do treino e um dos cenários mais registrados por quem visita o clube.",
                 "O painel iluminado atrás da banheira de gelo é o fundo do momento mais filmado do clube. O formato Recovery by associa a marca a recuperação, bem-estar e cuidado com o corpo."),
    "estudio-de-podcast": ("O estúdio recebe gravações de podcast e entrevistas com a academia ao fundo. O vidro conecta a conversa ao movimento do salão, o que dá contexto a cada episódio.",
                           "A marca aparece na faixa do vidro, na placa da mesa e no painel lateral. É presença em todo corte de vídeo, em todo episódio e em cada foto do convidado no microfone."),
    "north-room": ("A North Room recebe as aulas presenciais das pós-graduações, mentorias, cursos e imersões. Também pode ser reservada por empresas para treinamentos, lançamentos e encontros.",
                   "A parede de ativação fica atrás do palestrante e da turma. O formato North Room by coloca a marca em toda foto de aula, de abertura de evento e de encerramento de turma."),
    "vestiario": ("O vestiário foi desenhado com o mesmo cuidado dos demais ambientes. O espelho de corpo inteiro é o ponto natural da foto pós-treino, e os espelhos das pias completam o cenário.",
                  "A faixa da marca nos espelhos aparece em cada selfie pós-treino. É um ponto natural para marcas de cosméticos, higiene e farmácia, em contato direto com o uso do produto."),
    "jardim-suspenso": ("O jardim vertical fica na parede externa e é visto do mezanino e das estações de trabalho. Traz o verde para dentro da rotina de quem trabalha, estuda ou faz reuniões no clube.",
                        "O nome da marca em letras iluminadas integra o jardim ao cenário. Aparece nas fotos tiradas do mezanino e nas reuniões das estações de trabalho."),
}

POSTS = [
    {"slug": "o-que-e-um-clube-de-negocios-do-fitness", "cat": "business", "img": "hero",
     "titulo": "O que é um clube de negócios do fitness (e por que não é academia)",
     "resumo": "Treino, formação, conteúdo e negócios no mesmo endereço. Entenda o modelo de clube de negócios aplicado ao fitness e ao wellness.",
     "data": "2026-11-04"},
    {"slug": "networking-no-mercado-fitness", "cat": "business", "img": "p-empresarios",
     "titulo": "Networking no mercado fitness: por que densidade vale mais que volume",
     "resumo": "Eventos lotados nem sempre geram negócios. Veja por que ambientes de curadoria criam conexões mais úteis para empresários e profissionais do setor.",
     "data": "2026-11-06"},
    {"slug": "midia-espontanea-em-academias", "cat": "business", "img": "a03",
     "titulo": "Mídia espontânea em academias: como o ambiente vira canal de marca",
     "resumo": "Onde as pessoas tiram foto, a marca aparece. Como pensar ambientes de treino a partir do enquadramento de quem grava e posta.",
     "data": "2026-11-08"},
    {"slug": "pos-graduacao-presencial-em-curitiba", "cat": "education", "img": "a08",
     "titulo": "Pós-graduação presencial em Curitiba: a aula ao lado do salão",
     "resumo": "Aulas presenciais em dois fins de semana por mês, com a prática a poucos passos da sala. O que esse formato acrescenta à formação.",
     "data": "2026-11-10"},
    {"slug": "formacao-perto-da-pratica", "cat": "education", "img": "a04",
     "titulo": "Formação perto da prática: o caminho do conhecimento até o treino",
     "resumo": "Teoria e prática no mesmo endereço. Por que aproximar sala de aula e salão de treino melhora a formação de profissionais da saúde.",
     "data": "2026-11-12"},
    {"slug": "conteudo-com-profundidade-no-fitness", "cat": "wellness", "img": "a07",
     "titulo": "Conteúdo com profundidade no fitness: menos tendência, mais critério",
     "resumo": "Como produzir conteúdo de treino e saúde com critério técnico, gravado por quem treina e ensina, sem cair no clichê.",
     "data": "2026-11-14"},
    {"slug": "recovery-banheira-de-gelo-sauna-e-compressao", "cat": "wellness", "img": "a06",
     "titulo": "Recovery: banheira de gelo, sauna e compressão no mesmo ambiente",
     "resumo": "O que é um espaço de recovery, como ele se encaixa na rotina de treino e por que virou um dos cenários mais filmados do fitness.",
     "data": "2026-11-16"},
    {"slug": "como-nasceu-a-marca-wenorth", "cat": "bastidores", "img": "a02",
     "titulo": "Como nasceu a marca WeNorth: do pentágono ao N que aponta para o Norte",
     "resumo": "A história da construção do símbolo da WeNorth, criado pelo estúdio Discircle, passo a passo.",
     "data": "2026-11-18"},
]

CATS = {
    "business": ("Business", "Negócios, networking, marcas e mídia espontânea no mercado de fitness e wellness."),
    "education": ("Education", "Formação, pós-graduações, cursos e imersões para profissionais da saúde e do fitness."),
    "wellness": ("Wellness", "Treino, recuperação, conteúdo e bem-estar com critério técnico."),
    "bastidores": ("Bastidores", "A construção do WeNorth Club, da marca e do clube."),
}

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
         "setembro", "outubro", "novembro", "dezembro"]


def data_br(iso):
    a, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m) - 1]} de {a}"


def gerar(b):
    F, pagina, phero, card, faq_html = b.F, b.pagina, b.phero, b.card, b.faq_html

    def amb_card(a, go="Ver ambiente"):
        slug, nome, img, curto = a[0], a[1], a[2], a[3]
        return card(f"/ambientes/{slug}/", f"/img/{img}.webp", f"{nome}, imagem ilustrativa", "Ambiente", nome, curto, go)

    def amb(slug):
        return next(a for a in AMBIENTES if a[0] == slug)

    def post_card(p):
        return card(f"/blog/{p['slug']}/", f"/img/{p['img']}.webp", p["titulo"], CATS[p["cat"]][0], p["titulo"], p["resumo"], "Ler artigo")

    def posts_de(cat):
        return [p for p in POSTS if p["cat"] == cat]

    # ======================================================================
    # HOME
    # ======================================================================
    b.em_pagina("/")
    main = b.ler("home_main.html")
    main = main.replace('<main id="inicio">', "").replace("</main>", "")
    main = re.sub(r'src="img/([a-z0-9-]+)\.(?:jpg|png)"', r'src="/img/\1.webp"', main)
    main = main.replace('<a class="btn" id="btn-inscreva-hero" href="#marcas">', '<a class="btn" id="btn-inscreva-hero" href="/para-marcas/">')

    def depois(ancora, extra):
        nonlocal main
        assert main.count(ancora) == 1, ancora
        main = main.replace(ancora, ancora + extra)

    depois('<span class="chip">Apenas por convite</span></div>', '\n        <a class="more" href="/o-clube/">Conheça o clube</a>')
    depois('O próximo marco é a inauguração do clube, em fevereiro de 2027.</p>', '\n        <a class="more" href="/quem-somos/">Quem somos</a>')
    depois('<p>Lançamentos, ativações e encontros das marcas.</p></div>\n        </div>\n      </div>',
           '\n      <a class="more" href="/agenda/">Ver a agenda completa</a>')
    depois('<span>As empresas que fazem parte do ecossistema.</span></div></div>\n      </div>',
           '\n      <a class="more" href="/comunidade/">Quem faz parte</a>')
    depois('<span class="cap" style="flex-basis:100%">Audiência de André Albuquerque</span>\n      </div>',
           '\n      <a class="more" href="/quem-somos/">Conheça o grupo WeNorth</a>')
    depois('<div class="benefit"><h3>Mídia espontânea</h3><p>A marca no enquadramento de quem treina, grava e posta.</p></div>\n      </div>',
           '\n      <a class="more" href="/para-marcas/">Ver oportunidades para marcas</a>')
    depois('<p class="cap" style="margin-top:40px">Imagens ilustrativas · projeto em desenvolvimento</p>',
           '\n      <a class="more" href="/ambientes/">Conheça os 10 ambientes</a>')
    depois('<p>Do mesmo pentágono nasce a Estrela, símbolo de destaque, orientação e conquista.</p></div>\n      </div>',
           '\n      <a class="more" href="/a-marca/">A história da marca</a>')
    main = main.replace('<h3>André Albuquerque</h3>', '<h3><a href="/andre-albuquerque/">André Albuquerque</a></h3>')
    main = main.replace('<h3>Rafael Tonietto</h3>', '<h3><a href="/rafael-tonietto/">Rafael Tonietto</a></h3>')
    blog_home = f'''  <section class="band" id="blog">
    <div class="wrap">
      <p class="eyebrow">Blog</p>
      <h2>Ideias sobre negócios, formação e <span class="u">wellness</span>.</h2>
      <div class="cards">
        {"".join(post_card(p) for p in POSTS[:3])}
      </div>
      <a class="more" href="/blog/">Ver todos os artigos</a>
    </div>
  </section>

  <section class="band final" id="contato">'''
    main = main.replace('  <section class="band final" id="contato">', blog_home)
    pagina("/", "WeNorth Club | O clube de negócios do fitness e wellness em Curitiba",
           "O clube de negócios do fitness e wellness no Brasil: Business, Education e Wellness em mais de 600 m² em Curitiba/PR. Inauguração em fevereiro de 2027.",
           main, cta_final=False, prioridade="1.0",
           schema=[{"@type": "WebSite", "@id": b.DOMINIO + "/#site", "name": "WeNorth Club", "url": b.DOMINIO + "/",
                    "inLanguage": "pt-BR", "publisher": {"@id": b.DOMINIO + "/#org"}}])

    # ======================================================================
    # O CLUBE
    # ======================================================================
    url = "/o-clube/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "O clube")]
    faq = [
        ("O WeNorth Club é uma academia?", "Não. O WeNorth Club é um clube de negócios do fitness e wellness. Tem salão de treino, mas também sala de aulas, estúdio de podcast, recovery e estações de trabalho, e reúne empresários, profissionais, influenciadores e marcas."),
        ("Onde fica o WeNorth Club?", "Na Rua Eng. Arthur Bettes, 419, no bairro Portão, em Curitiba/PR."),
        ("Quando o clube inaugura?", "A inauguração está prevista para fevereiro de 2027."),
        ("Como faço para entrar no clube?", "O acesso é feito apenas por convite, para reunir as pessoas certas no mesmo ambiente. " + F("Processo do pedido de convite", "Você pode pedir o seu convite pelo formulário do site, e a equipe entra em contato.")),
        ("Empresas podem alugar espaços do clube?", "Sim. A North Room, sala de mentorias, pós-graduações e imersões, também está disponível para locação por empresas. " + F("Forma de contratar a locação", "Fale com a equipe para conhecer datas e formatos.")),
    ]
    corpo = phero(crumbs, "O clube · Curitiba/PR", 'O clube de negócios do <span class="u">fitness</span> e wellness.',
                  "Mais de 600 m² em Curitiba para treinar, criar conteúdo, gravar podcasts, lançar produtos e fazer negócios.",
                  "/img/clube-northroom.webp",
                  '<a class="btn" id="btn-inscreva-hero" href="/convite/">Pedir convite</a><a class="btn ghost" href="/ambientes/">Ver os ambientes</a>')
    corpo += f'''
  <section class="band paper">
    <div class="wrap two">
      <div>
        <p class="eyebrow">O que é</p>
        <h2>A casa do grupo <span class="u">WeNorth</span>.</h2>
      </div>
      <div class="prose">
        <p>O WeNorth Club é o endereço onde o mercado de fitness e wellness se encontra para treinar, criar conteúdo, gravar podcasts, lançar produtos e fazer negócios.</p>
        <p>WeNorth é o grupo. Ele nasce da força da <a href="https://www.personaltraineracademy.com.br/" target="_blank" rel="noopener">Personal Trainer Academy</a> (PTA), que continua existindo como sua principal integrante. A WeNorth dá nome ao conjunto de empresas e produtos que passou a existir ao redor dela, e o clube é a casa desse grupo.</p>
        <p>O clube não é uma academia. O acesso é feito apenas por convite, para reunir as pessoas certas no mesmo ambiente.</p>
      </div>
    </div>
  </section>

  <section class="band paper" style="padding-top:0">
    <div class="wrap">
      <div class="stats">
        <div><b data-count="600" data-suffix=" m²+">600 m²+</b><span>com salão de pé-direito duplo e mezanino</span></div>
        <div><b>Portão</b><span>Rua Eng. Arthur Bettes, 419, Curitiba/PR</span></div>
        <div><b>Fev. 2027</b><span>inauguração prevista</span></div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <p class="eyebrow">Três pilares</p>
      <h2>Business, Education e <span class="u">Wellness</span>.</h2>
      <p class="lede">O clube funciona com um calendário vivo, o ano inteiro, organizado em três pilares.</p>
      <div class="cards">
        {card("/business/", "/img/p-empresarios.webp", "Empresários em reunião", "Pilar", "Business", "Mentorias de alto nível, lançamentos digitais e conexões além do fitness.")}
        {card("/education/", "/img/a08.webp", "North Room, imagem ilustrativa", "Pilar", "Education", "Pós-graduações, cursos e imersões ao lado do salão de treino.")}
        {card("/wellness/", "/img/a06.webp", "Recovery, imagem ilustrativa", "Pilar", "Wellness", "Treino, conteúdo, podcast e eventos dos parceiros.")}
      </div>
      <a class="more" href="/agenda/">Ver a agenda do clube</a>
    </div>
  </section>

  <section class="band" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">10 ambientes</p>
      <h2>Cada ambiente pensado para ser <span class="u">vivido</span>.</h2>
      <p class="lede">Todos foram desenhados a partir de uma pergunta: onde as pessoas naturalmente tiram foto e gravam vídeo?</p>
      <div class="cards">
        {amb_card(amb("salao-multiesportes"))}{amb_card(amb("north-room"))}{amb_card(amb("recovery"))}
      </div>
      <a class="more" href="/ambientes/">Ver todos os ambientes</a>
    </div>
  </section>

  <section class="band paper">
    <div class="wrap">
      <p class="eyebrow">Perguntas frequentes</p>
      <h2>Sobre o <span class="u">clube</span>.</h2>
{faq_html(faq)}
    </div>
  </section>'''
    pagina(url, "O clube | WeNorth Club, clube de negócios do fitness em Curitiba",
           "Conheça o WeNorth Club: mais de 600 m² em Curitiba com Business, Education e Wellness. Acesso apenas por convite. Inauguração em fevereiro de 2027.",
           corpo, crumbs=crumbs, schema=[b.faq_ld(faq)], og_img="/img/clube-northroom.jpg", prioridade="0.9")

    # ======================================================================
    # AGENDA
    # ======================================================================
    url = "/agenda/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Agenda")]
    corpo = phero(crumbs, "O que acontece aqui", 'Um calendário <span class="u">vivo</span>, o ano inteiro.',
                  "Mentorias, pós-graduações, imersões, gravações e eventos de marcas, organizados em três pilares.",
                  "/img/a04.webp")
    corpo += f'''
  <section class="band">
    <div class="wrap">
      <div class="agenda" style="margin-top:0">
        <div class="col">
          <h3><a href="/business/" style="color:inherit;text-decoration:none">Business</a></h3>
          <div class="item"><b>Mentorias de alto nível</b><p>Encontros com empresários, donos de academias e estúdios e personal trainers do digital.</p></div>
          <div class="item"><b>Lançamentos digitais</b><p>Produtos e serviços digitais gravados e transmitidos do clube.</p></div>
          <div class="item"><b>Conexões além do fitness</b><p>Empresários de construção, automotivo, aviação e varejo convidados a conhecer o clube.</p></div>
        </div>
        <div class="col">
          <h3><a href="/education/" style="color:inherit;text-decoration:none">Education</a></h3>
          <div class="item"><b>Pós-graduações</b><p>Algumas das principais pós-graduações do Brasil, com aulas presenciais em dois fins de semana por mês.</p></div>
          <div class="item"><b>Cursos e imersões</b><p>Formações intensivas da casa e de empresas convidadas.</p></div>
        </div>
        <div class="col">
          <h3><a href="/wellness/" style="color:inherit;text-decoration:none">Wellness</a></h3>
          <div class="item"><b>Treino e conteúdo com influenciadores</b><p>Influenciadores e profissionais da saúde treinando e produzindo no clube.</p></div>
          <div class="item"><b>Conteúdo, podcast e YouTube</b><p>Gravações no estúdio e no salão, com o espaço como cenário.</p></div>
          <div class="item"><b>Eventos dos parceiros</b><p>Lançamentos, ativações e encontros das marcas.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="band paper">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Como funciona</p>
        <h2>Uma agenda com <span class="u">curadoria</span>.</h2>
      </div>
      <div class="prose">
        {F("Funcionamento da agenda e divulgação das datas", "<p>A programação do clube é montada ao longo do ano, combinando turmas de pós-graduação, mentorias, imersões, gravações e eventos de marcas parceiras. Cada atividade tem seu público e seu formato, e todas acontecem no mesmo endereço.</p><p>As datas são comunicadas a membros, alunos e convidados. Para participar de uma atividade ou propor um evento no clube, fale com a equipe.</p>")}
        <p>Para conhecer os programas, eventos e mentorias já abertos do grupo, acesse a página de <a href="/programas/">programas</a>.</p>
      </div>
    </div>
  </section>'''
    pagina(url, "Agenda | Mentorias, pós-graduações e eventos no WeNorth Club",
           "A agenda do WeNorth Club: mentorias de alto nível, lançamentos digitais, pós-graduações, cursos, imersões, gravações e eventos de marcas em Curitiba.",
           corpo, crumbs=crumbs, og_img="/img/a04.jpg", prioridade="0.8")

    # ======================================================================
    # COMUNIDADE
    # ======================================================================
    url = "/comunidade/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Comunidade")]
    pessoas = [("p-empresarios", "Empresários em reunião", "Empresários", "Donos de academias, estúdios e negócios do setor, além de líderes de outros mercados."),
               ("p-influenciadores", "Influenciadora treinando e gravando", "Influenciadores", "Do fitness, do wellness, da saúde e do business."),
               ("p-professores", "Professor dando aula para uma turma", "Professores e doutores", "Nomes da ciência do exercício no país."),
               ("p-saude", "Profissionais da saúde conversando na academia", "Profissionais da saúde", "Médicos, nutricionistas e fisioterapeutas."),
               ("p-personal", "Personal trainer orientando aluna", "Personal trainers", "Profissionais que atendem a classe A."),
               ("p-marcas", "Representantes de marca entregando um produto", "Marcas parceiras", "As empresas que fazem parte do ecossistema.")]
    grade = "\n        ".join(f'<div class="person"><img src="/img/{i}.webp" alt="{a}" loading="lazy" width="1200" height="670"><div><b>{t}</b><span>{d}</span></div></div>' for i, a, t, d in pessoas)
    corpo = phero(crumbs, "Quem está lá", 'As pessoas que movem o fitness e o <span class="u">wellness</span> no Brasil.',
                  "O clube reúne empresários, influenciadores, professores, profissionais da saúde, personal trainers e marcas no mesmo ambiente.",
                  "/img/p-professores.webp", cap=False)
    corpo += f'''
  <section class="band">
    <div class="wrap">
      <p class="eyebrow">Quem circula</p>
      <h2>Seis grupos, um <span class="u">endereço</span>.</h2>
      <div class="people">
        {grade}
      </div>
    </div>
  </section>

  <section class="band paper">
    <div class="wrap">
      <p class="eyebrow">A rede em números</p>
      <h2>Influenciadores, empresários, profissionais e <span class="u">professores</span>.</h2>
      <p class="lede">Somam mais de 50 milhões de seguidores no Instagram.</p>
      <div class="stats">
        <div><b data-count="50" data-suffix=" mi+">50 mi+</b><span>seguidores no Instagram somados pela rede de relacionamento</span></div>
        <div><b data-count="8.3" data-dec="1" data-suffix=" mi">8,3 mi</b><span>inscritos no YouTube somados pela mesma rede</span></div>
        <div><b data-count="94">94</b><span>amigos e convidados: influenciadores, empresários e personal trainers</span></div>
      </div>
      <div class="stats">
        <div><b data-count="46">46</b><span>mestres e doutores no corpo docente das pós-graduações</span></div>
        <div><b data-count="30" data-suffix=" mil+">30 mil+</b><span>alunos em todo o Brasil</span></div>
        <div><b data-count="40">40</b><span>pessoas no time da PTA</span></div>
      </div>
      <p class="cap" style="margin-top:32px">Números de seguidores de 19/09/2026</p>
    </div>
  </section>

  <section class="band">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Curadoria</p>
        <h2>Exclusividade como <span class="u">curadoria</span>.</h2>
      </div>
      <div class="prose">
        <p>O acesso ao clube é feito apenas por convite. A ideia não é criar uma barreira, mas reunir as pessoas certas no mesmo ambiente, para que cada encontro gere formação, conteúdo ou negócio.</p>
        {F("Critérios de quem recebe convite", "<p>Os convites consideram a área de atuação, o momento profissional e o que cada pessoa pode trocar com a comunidade. Profissionais, empresários e marcas interessados podem pedir o convite pelo site.</p>")}
        <p><a href="/convite/">Pedir convite</a> · <a href="/quem-somos/">Quem conduz o clube</a></p>
      </div>
    </div>
  </section>'''
    pagina(url, "Comunidade | Quem faz parte do WeNorth Club",
           "Empresários, influenciadores, professores e doutores, profissionais da saúde, personal trainers e marcas: conheça a comunidade do WeNorth Club.",
           corpo, crumbs=crumbs, og_img="/img/p-professores.jpg", prioridade="0.7")

    # ======================================================================
    # PILARES
    # ======================================================================
    pilares = {
        "business": {
            "eyebrow": "Pilar · Business", "h1": 'Negócios em um ambiente de <span class="u">curadoria</span>.',
            "lede": "Conectar empresários, profissionais e marcas em um ambiente de curadoria.",
            "img": "p-empresarios",
            "itens": [("Mentorias de alto nível", "Encontros com empresários, donos de academias e estúdios e personal trainers do digital."),
                      ("Lançamentos digitais", "Produtos e serviços digitais gravados e transmitidos do clube."),
                      ("Conexões além do fitness", "Empresários de construção, automotivo, aviação e varejo convidados a conhecer o clube.")],
            "fic": "<p>O mercado de fitness e wellness costuma fazer networking em eventos grandes e encontros rápidos. No clube, a lógica é outra: menos pessoas, mais contexto e mais tempo juntos. Mentorias, gravações e lançamentos acontecem no mesmo endereço, e é nesse convívio que as conexões viram negócio.</p><p>Para quem empreende no setor, o Business reúne referências de gestão, vendas e posicionamento digital. Para empresários de outros mercados, é uma porta de entrada para entender o fitness e o wellness de perto.</p>",
            "amb": ["north-room", "estudio-de-podcast", "jardim-suspenso"],
            "titulo": "Business | Mentorias, lançamentos e networking no WeNorth Club",
            "desc": "O pilar Business do WeNorth Club: mentorias de alto nível, lançamentos digitais e conexões com empresários de dentro e fora do fitness, em Curitiba.",
        },
        "education": {
            "eyebrow": "Pilar · Education", "h1": 'A formação perto da <span class="u">prática</span>.',
            "lede": "Levar a formação para perto da prática, com pós-graduações, cursos e imersões ao lado do salão de treino.",
            "img": "a08",
            "itens": [("Pós-graduações", "Algumas das principais pós-graduações do Brasil, com aulas presenciais em dois fins de semana por mês."),
                      ("Cursos e imersões", "Formações intensivas da casa e de empresas convidadas.")],
            "fic": "<p>A North Room recebe as aulas e fica a poucos passos do salão multiesportes. O que é visto na sala pode ser aplicado e observado no treino, no mesmo dia. Essa proximidade é a base do pilar Education.</p><p>A formação parte da autoridade técnica do grupo em biomecânica e formação aplicada, e se estende a cursos e imersões da casa e de empresas convidadas.</p>",
            "amb": ["north-room", "salao-multiesportes", "gluteus-zone"],
            "titulo": "Education | Pós-graduações, cursos e imersões no WeNorth Club",
            "desc": "O pilar Education do WeNorth Club: pós-graduações com aulas presenciais em dois fins de semana por mês, cursos e imersões ao lado do salão de treino.",
        },
        "wellness": {
            "eyebrow": "Pilar · Wellness", "h1": 'Treino, conteúdo e <span class="u">bem-estar</span>.',
            "lede": "Produzir conteúdo com profundidade, gravado por quem treina e ensina no clube.",
            "img": "a06",
            "itens": [("Treino e conteúdo com influenciadores", "Influenciadores e profissionais da saúde treinando e produzindo no clube."),
                      ("Conteúdo, podcast e YouTube", "Gravações no estúdio e no salão, com o espaço como cenário."),
                      ("Eventos dos parceiros", "Lançamentos, ativações e encontros das marcas.")],
            "fic": "<p>No clube, o conteúdo nasce da rotina: quem grava também treina e ensina ali. Por isso o critério técnico vem antes da tendência, e o ambiente é desenhado para servir de cenário sem esforço.</p><p>Salão multiesportes, Gluteus Zone, Recovery e estúdio de podcast formam um circuito completo de produção, do treino à conversa sobre ele.</p>",
            "amb": ["salao-multiesportes", "recovery", "estudio-de-podcast"],
            "titulo": "Wellness | Treino, recovery e conteúdo no WeNorth Club",
            "desc": "O pilar Wellness do WeNorth Club: treino e conteúdo com influenciadores e profissionais da saúde, podcast, YouTube e eventos de marcas em Curitiba.",
        },
    }
    for slug, p in pilares.items():
        url = f"/{slug}/"
        b.em_pagina(url)
        nome = slug.capitalize()
        crumbs = [("/", "Início"), ("/agenda/", "Agenda"), (url, nome)]
        itens = "".join(f'<div class="item"><b>{t}</b><p>{d}</p></div>' for t, d in p["itens"])
        relacionados = posts_de(slug)
        blog = ""
        if relacionados:
            blog = f'''
  <section class="band" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">Do blog</p>
      <h2>Leituras sobre <span class="u">{nome}</span>.</h2>
      <div class="cards">{"".join(post_card(x) for x in relacionados)}</div>
      <a class="more" href="/blog/{slug}/">Ver categoria {nome}</a>
    </div>
  </section>'''
        outros = " · ".join(f'<a href="/{o}/">{o.capitalize()}</a>' for o in pilares if o != slug)
        corpo = phero(crumbs, p["eyebrow"], p["h1"], p["lede"], f"/img/{p['img']}.webp",
                      '<a class="btn" id="btn-inscreva-hero" href="/convite/">Pedir convite</a><a class="btn ghost" href="/agenda/">Ver a agenda</a>',
                      cap=p["img"].startswith("a"))
        corpo += f'''
  <section class="band paper">
    <div class="wrap two">
      <div>
        <p class="eyebrow">O que acontece</p>
        <h2>{nome} no <span class="u">clube</span>.</h2>
      </div>
      <div>
        <div class="agenda" style="margin-top:0;grid-template-columns:1fr;border-color:var(--paper-line)"><div class="col" style="border:0;padding:0">{itens}</div></div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Por que importa</p>
        <h2>Um mercado que anda em <span class="u">partes</span>.</h2>
      </div>
      <div class="prose">
        <p>Hoje o mercado anda em partes: treino sem método, influência sem profundidade e networking sem densidade. O clube reúne tudo em um só endereço.</p>
        {F(f"Texto de aprofundamento do pilar {nome}", p["fic"])}
        <p>Outros pilares: {outros}.</p>
      </div>
    </div>
  </section>

  <section class="band" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">Onde acontece</p>
      <h2>Ambientes do pilar <span class="u">{nome}</span>.</h2>
      <div class="cards">{"".join(amb_card(amb(a)) for a in p["amb"])}</div>
    </div>
  </section>{blog}'''
        pagina(url, p["titulo"], p["desc"], corpo, crumbs=crumbs, og_img=f"/img/{p['img']}.jpg", prioridade="0.8")

    # ======================================================================
    # AMBIENTES
    # ======================================================================
    url = "/ambientes/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Ambientes")]
    corpo = phero(crumbs, "Os espaços do clube · 10 ambientes", 'Onde as pessoas se fotografam, a sua <span class="u">marca</span> está.',
                  "São dez ambientes, cada um pensado para ser vivido. Todos foram desenhados a partir de uma pergunta: onde as pessoas naturalmente tiram foto e gravam vídeo?",
                  "/img/a01.webp")
    corpo += f'''
  <section class="band">
    <div class="wrap">
      <div class="cards" style="margin-top:0">
        {"".join(amb_card(a) for a in AMBIENTES)}
      </div>
      <p class="cap" style="margin-top:40px">Imagens ilustrativas · projeto em desenvolvimento</p>
      <a class="more" href="/para-marcas/">Presença de marca nos ambientes</a>
    </div>
  </section>'''
    lista = {"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": f"{b.DOMINIO}/ambientes/{a[0]}/", "name": a[1]} for i, a in enumerate(AMBIENTES)]}
    pagina(url, "Ambientes | Os 10 espaços do WeNorth Club em Curitiba",
           "Vitrine de parceiros, salão multiesportes, Gluteus Zone, Recovery, estúdio de podcast, North Room e mais: conheça os 10 ambientes do WeNorth Club.",
           corpo, crumbs=crumbs, schema=[lista], og_img="/img/a01.jpg", prioridade="0.9")

    for i, a in enumerate(AMBIENTES):
        slug, nome, img, curto, chamada, texto, chips = a
        url = f"/ambientes/{slug}/"
        b.em_pagina(url)
        crumbs = [("/", "Início"), ("/ambientes/", "Ambientes"), (url, nome)]
        uso, marca = AMB_FIC[slug]
        prox = [AMBIENTES[(i + k) % len(AMBIENTES)] for k in (1, 2, 3)]
        chips_html = "".join(f'<span class="chip">{c}</span>' for c in chips)
        corpo = phero(crumbs, f"Ambiente {i + 1:02d} / 10", nome, curto, f"/img/{img}.webp")
        corpo += f'''
  <section class="band">
    <div class="wrap two">
      <div class="prose">
        <h2 style="margin-top:0">{chamada}</h2>
        <p>{texto}</p>
        {F(f"Como o ambiente {nome} é usado no dia a dia", f"<p>{uso}</p>")}
        <p class="v-label">Presença de marca</p>
        <div class="chips" style="margin-top:12px">{chips_html}</div>
      </div>
      <figure class="figure-wide"><img src="/img/{img}.webp" alt="{nome} do WeNorth Club, imagem ilustrativa" width="1200" height="675" loading="lazy"><figcaption>Imagem ilustrativa · projeto em desenvolvimento</figcaption></figure>
    </div>
  </section>

  <section class="band paper">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Para a marca parceira</p>
        <h2>A marca no <span class="u">enquadramento</span>.</h2>
      </div>
      <div class="prose">
        {F(f"Oportunidade de marca no ambiente {nome}", f"<p>{marca}</p>")}
        <p><a href="/para-marcas/">Ver oportunidades para marcas</a></p>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <p class="eyebrow">Continue o passeio</p>
      <h2>Outros <span class="u">ambientes</span>.</h2>
      <div class="cards">{"".join(amb_card(x) for x in prox)}</div>
      <a class="more" href="/ambientes/">Todos os ambientes</a>
    </div>
  </section>'''
        lugar = {"@type": "Place", "name": f"{nome} · WeNorth Club", "description": f"{curto} {texto}",
                 "image": f"{b.DOMINIO}/img/{img}.jpg", "containedInPlace": {"@id": b.DOMINIO + "/#org"}}
        pagina(url, f"{nome} | Ambientes do WeNorth Club",
               f"{curto} Conheça o ambiente {nome} do WeNorth Club, em Curitiba, e as oportunidades de presença de marca."[:158],
               corpo, crumbs=crumbs, schema=[lugar], og_img=f"/img/{img}.jpg", prioridade="0.6")

    # ======================================================================
    # QUEM SOMOS
    # ======================================================================
    url = "/quem-somos/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Quem somos")]
    corpo = phero(crumbs, "Quem somos", 'Mais saúde para o <span class="u">Brasil</span>.',
                  "WeNorth é o grupo. O WeNorth Club é a casa desse grupo. E a Personal Trainer Academy continua como sua principal integrante.",
                  "/img/hero.webp")
    corpo += '''
  <section class="band paper">
    <div class="wrap two">
      <div>
        <p class="eyebrow">O grupo</p>
        <h2>WeNorth e WeNorth <span class="u">Club</span>.</h2>
      </div>
      <div class="prose">
        <p><strong>WeNorth é o grupo.</strong> Ele nasce da força da Personal Trainer Academy (PTA), que continua existindo como sua principal integrante. A WeNorth dá nome ao conjunto de empresas e produtos que passou a existir ao redor dela.</p>
        <p><strong>WeNorth Club é a casa desse grupo.</strong> É o endereço onde o mercado de fitness e wellness se encontra para treinar, criar conteúdo, gravar podcasts, lançar produtos e fazer negócios.</p>
        <p>O clube não é uma academia. O acesso é feito apenas por convite, para reunir as pessoas certas no mesmo ambiente.</p>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap two">
      <div>
        <p class="eyebrow">A origem</p>
        <h2>Uma missão que precisava de uma <span class="u">casa</span>.</h2>
      </div>
      <div class="prose">
        <p>Em 2020, a PTA assumiu uma missão: mais saúde para o Brasil. O caminho foi formar profissionais notáveis na área da saúde.</p>
        <p>Para levar essa missão mais longe, ela precisava de uma casa, com educação, negócios e bem-estar juntos. Assim nasceu o WeNorth Club.</p>
      </div>
    </div>
  </section>

  <section class="band" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">Por que o clube existe</p>
      <h2>Treino sem método, influência sem <span class="u">profundidade</span>.</h2>
      <p class="lede">Hoje o mercado anda em partes: treino sem método, influência sem profundidade e networking sem densidade. O clube reúne tudo em um só endereço, com três objetivos.</p>
      <div class="steps">
        <div><h3>Formação</h3><p>Levar a formação para perto da prática, com pós-graduações, cursos e imersões ao lado do salão de treino.</p></div>
        <div><h3>Conteúdo</h3><p>Produzir conteúdo com profundidade, gravado por quem treina e ensina ali.</p></div>
        <div><h3>Negócios</h3><p>Conectar empresários, profissionais e marcas em um ambiente de curadoria.</p></div>
      </div>
    </div>
  </section>

  <section class="band paper">
    <div class="wrap">
      <p class="eyebrow">Para onde estamos indo</p>
      <h2>De plataforma de formação a <span class="u">ecossistema</span>.</h2>
      <p class="lede">A WeNorth está deixando de ser uma plataforma de formação para se tornar um ecossistema. Nele, saúde, performance, formação, conteúdo, influência e negócios reforçam uns aos outros.</p>
      <div class="benefits">
        <div class="benefit"><h3>Missão</h3><p>Mais saúde para o Brasil.</p></div>
        <div class="benefit"><h3>Promessa</h3><p>Evoluir em um ambiente que conecta corpo, conhecimento, reputação e oportunidade.</p></div>
        <div class="benefit"><h3>Base</h3><p>A autoridade técnica em biomecânica e formação aplicada, que é o modo como a marca entende o corpo e o movimento.</p></div>
        <div class="benefit"><h3>Próximo marco</h3><p>Inauguração do clube em fevereiro de 2027.</p></div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <p class="eyebrow">Quem conduz</p>
      <h2>Quem <span class="u">conduz</span> o clube.</h2>
      <div class="leaders">
        <article class="leader">
          <img src="/img/andre.webp" alt="Retrato de André Albuquerque" loading="lazy" width="900" height="1489">
          <div class="txt"><h3><a href="/andre-albuquerque/">André Albuquerque</a></h3><p>Mestre em biomecânica · CEO do WeNorth Club</p>
            <div class="nums"><div><b>335 mil</b><span>Instagram</span></div><div><b>47 mil</b><span>YouTube</span></div></div></div>
        </article>
        <article class="leader">
          <img src="/img/rafael.webp" alt="Retrato de Rafael Tonietto" loading="lazy" width="900" height="1489">
          <div class="txt"><h3><a href="/rafael-tonietto/">Rafael Tonietto</a></h3><p>Doutor em educação · Especialista em vendas no digital · CEO do WeNorth Club</p>
            <div class="nums"><div><b>16 mil</b><span>Instagram</span></div></div></div>
        </article>
        <article class="leader pta">
          <div class="logo"><img src="/img/pta.webp" alt="Personal Trainer Academy" loading="lazy"></div>
          <div class="txt"><h3><a href="https://www.personaltraineracademy.com.br/" target="_blank" rel="noopener">Personal Trainer Academy</a></h3><p>Principal integrante do grupo WeNorth, desde 2020</p>
            <div class="nums"><div><b>56 mil</b><span>Instagram</span></div><div><b>14 mil</b><span>YouTube</span></div></div></div>
        </article>
      </div>
      <p class="cap" style="margin-top:28px">Números de seguidores de 19/09/2026</p>
      <a class="more" href="/a-marca/">A história da marca</a>
    </div>
  </section>'''
    pagina(url, "Quem somos | WeNorth, o grupo da Personal Trainer Academy",
           "O WeNorth é o grupo que nasce da Personal Trainer Academy. Conheça a origem, a missão de mais saúde para o Brasil e quem conduz o WeNorth Club.",
           corpo, crumbs=crumbs, schema=[{"@type": "AboutPage", "name": "Quem somos", "url": b.DOMINIO + url, "about": {"@id": b.DOMINIO + "/#org"}}],
           prioridade="0.9")

    # ======================================================================
    # A MARCA
    # ======================================================================
    url = "/a-marca/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), ("/quem-somos/", "Quem somos"), (url, "A marca")]
    cores = [("#000F0F", "Full Black", "Fundo escuro principal"), ("#002828", "Dark Green", "Cor institucional"),
             ("#82E628", "Neon Green", "Só como acento, em cerca de 5% a 10% da área"), ("#7D96A0", "Mid Gray", "Textos de apoio"),
             ("#B4D7D7", "Soft Gray", "Fundo claro principal")]
    swatches = "".join(f'<div class="benefit"><span style="display:block;height:64px;border-radius:4px;background:{h};border:1px solid var(--paper-line);margin-bottom:18px"></span><h3>{n}</h3><p>{h} · {d}</p></div>' for h, n, d in cores)
    corpo = phero(crumbs, "A marca", 'Um <span class="u">N</span> que aponta para o Norte.',
                  "O símbolo da WeNorth é um N em perspectiva, que não apenas representa o Norte, mas aponta para ele.",
                  "/img/a02.webp")
    corpo += f'''
  <section class="band">
    <div class="wrap two">
      <div>
        <p class="eyebrow">A origem do símbolo</p>
        <h2>17h de uma <span class="u">sexta-feira</span>.</h2>
      </div>
      <div class="prose">
        <p>A marca foi criada pelo estúdio Discircle e nasceu às 17h de uma sexta-feira, 24 de julho de 2026.</p>
        <p>O símbolo vem primeiro, e o descritor CLUB fica em peso mais fino. A marca usa as versões com símbolo, sempre em uma única cor da paleta.</p>
      </div>
    </div>
  </section>

  <section class="band paper">
    <div class="wrap">
      <p class="eyebrow">A construção</p>
      <h2>Do pentágono ao <span class="u">N</span>.</h2>
      <div class="benefits">
        <div class="benefit"><h3>01 · O pentágono</h3><p>Tudo começa em um pentágono regular.</p></div>
        <div class="benefit"><h3>02 · Dois pentágonos</h3><p>Duplicado, reduzido e empilhado, ele vira uma forma própria, com dois pentágonos.</p></div>
        <div class="benefit"><h3>03 · Dois trapézios</h3><p>Os dois perdem os vértices inferiores e se tornam dois trapézios.</p></div>
        <div class="benefit"><h3>04 · A malha</h3><p>O cruzamento de 58 linhas anguladas forma a malha estrutural.</p></div>
        <div class="benefit"><h3>05 · O N</h3><p>Dessa malha surge o N, cujo ângulo aponta para o Norte.</p></div>
        <div class="benefit"><h3>A Estrela</h3><p>Do mesmo pentágono nasce a Estrela, símbolo de destaque, orientação e conquista.</p></div>
      </div>
    </div>
  </section>

  <section class="band paper" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">Identidade visual</p>
      <h2>Cores, fonte e <span class="u">tom</span>.</h2>
      <div class="benefits">{swatches}<div class="benefit"><h3>Tipografia</h3><p>Fonte oficial Area Normal. Na web, IBM Plex Sans. Extrabold e Hairline só em logotipos e títulos; Light, Regular e Medium nos demais textos.</p></div></div>
    </div>
  </section>

  <section class="band">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Tom de voz</p>
        <h2>Curadoria, não <span class="u">barreira</span>.</h2>
      </div>
      <div class="prose">
        <p>Frases curtas e afirmativas, com critério técnico e proximidade. Sem clichês fitness, sem tom de academia tradicional e sem wellness genérico.</p>
        <p>A exclusividade deve soar como curadoria, não como barreira de status. A marca não usa branco nem preto puros, nem gradientes ou sombras pesadas.</p>
        <p><a href="/blog/como-nasceu-a-marca-wenorth/">Leia a história completa no blog</a></p>
      </div>
    </div>
  </section>'''
    pagina(url, "A marca | A história do símbolo WeNorth",
           "O símbolo da WeNorth é um N em perspectiva que aponta para o Norte. Conheça a construção da marca, criada pelo estúdio Discircle, e a identidade visual.",
           corpo, crumbs=crumbs, og_img="/img/a02.jpg", prioridade="0.6")

    # ======================================================================
    # PESSOAS
    # ======================================================================
    pessoas = [
        ("andre-albuquerque", "André Albuquerque", "andre", "Mestre em biomecânica · CEO do WeNorth Club",
         '<div class="stats"><div><b data-count="335" data-suffix=" mil">335 mil</b><span>seguidores no Instagram</span></div><div><b data-count="47" data-suffix=" mil">47 mil</b><span>inscritos no YouTube</span></div><div><b data-count="5" data-suffix=" mi">5 mi</b><span>visualizações por mês na audiência</span></div></div><div class="stats"><div><b data-count="1.8" data-dec="1" data-suffix=" mi+">1,8 mi+</b><span>contas alcançadas por mês</span></div><div><b data-count="150" data-suffix=" mil">150 mil</b><span>visualizações por mês no YouTube</span></div><div><b>Biomecânica</b><span>a base técnica da marca</span></div></div>',
         "<p>André Albuquerque é mestre em biomecânica e CEO do WeNorth Club. A autoridade técnica em biomecânica e formação aplicada é a base da marca: o modo como o grupo entende o corpo e o movimento.</p>",
         "<p>No clube, André conduz a frente técnica e de formação, com presença nas pós-graduações, nos conteúdos gravados no salão e no estúdio e nos encontros com profissionais da saúde. Sua audiência digital é uma das bases da rede de relacionamento do clube.</p>",
         "Mestre em biomecânica", [],
         "André Albuquerque | Mestre em biomecânica e CEO do WeNorth Club",
         "André Albuquerque é mestre em biomecânica e CEO do WeNorth Club, com 335 mil seguidores no Instagram e 47 mil inscritos no YouTube."),
        ("rafael-tonietto", "Rafael Tonietto", "rafael", "Doutor em educação · Especialista em vendas no digital · CEO do WeNorth Club",
         '<div class="stats"><div><b data-count="16" data-suffix=" mil">16 mil</b><span>seguidores no Instagram</span></div><div><b>Doutor</b><span>em educação</span></div><div><b>Digital</b><span>especialista em vendas</span></div></div>',
         "<p>Rafael Tonietto é doutor em educação, especialista em vendas no digital e CEO do WeNorth Club.</p>",
         "<p>No clube, Rafael conduz as frentes de negócios e educação: mentorias com empresários e donos de academias, lançamentos digitais gravados e transmitidos do clube e a estrutura de formação do grupo.</p>",
         "Doutor em educação", ["https://rafaeltonietto.com.br/", "https://www.youtube.com/@rafael.tonietto"],
         "Rafael Tonietto | Doutor em educação e CEO do WeNorth Club",
         "Rafael Tonietto é doutor em educação, especialista em vendas no digital e CEO do WeNorth Club, o clube de negócios do fitness e wellness em Curitiba."),
    ]
    for slug, nome, img, papel, stats, bio, bio_fic, cargo_curto, same, titulo, desc in pessoas:
        url = f"/{slug}/"
        b.em_pagina(url)
        crumbs = [("/", "Início"), ("/quem-somos/", "Quem somos"), (url, nome)]
        outro = [p for p in pessoas if p[0] != slug][0]
        corpo = phero(crumbs, "Quem conduz", nome, papel, "/img/hero.webp", cap=False)
        corpo += f'''
  <section class="band">
    <div class="wrap two">
      <figure class="figure-wide figure-tall"><img src="/img/{img}.webp" alt="Retrato de {nome}" width="900" height="1489" loading="lazy"></figure>
      <div class="prose">
        <h2 style="margin-top:0">{cargo_curto}, <span class="u">CEO</span>.</h2>
        {bio}
        {F(f"Atuação de {nome} no dia a dia do clube", bio_fic)}
        <p>Conheça também <a href="/{outro[0]}/">{outro[1]}</a> e a <a href="/quem-somos/">história do grupo WeNorth</a>.</p>
      </div>
    </div>
  </section>

  <section class="band paper">
    <div class="wrap">
      <p class="eyebrow">Em números</p>
      <h2>Presença <span class="u">digital</span>.</h2>
      {stats}
      <p class="cap" style="margin-top:32px">Números de 19/09/2026</p>
    </div>
  </section>'''
        pessoa = {"@type": "Person", "name": nome, "jobTitle": "CEO do WeNorth Club", "description": papel,
                  "image": f"{b.DOMINIO}/img/{img}.jpg", "worksFor": {"@id": b.DOMINIO + "/#org"}, "url": b.DOMINIO + url}
        if same:
            pessoa["sameAs"] = same
        pagina(url, titulo, desc, corpo, crumbs=crumbs, schema=[{"@type": "ProfilePage", "mainEntity": pessoa}],
               og_img=f"/img/{img}.jpg", og_type="profile", prioridade="0.7")

    # ======================================================================
    # PARA MARCAS
    # ======================================================================
    subs = [
        ("naming-e-ativacoes", "Naming e ativações", "Espaços com o nome da marca.", "a05",
         'O nome da marca no <span class="u">ambiente</span>.',
         "<p>Cada ambiente do clube pode receber o nome de uma marca: Recovery by, Gluteus Zone by, Podcast by, North Room by. O nome aparece em letreiro, painel ou parede, no ponto exato em que as pessoas fotografam e gravam.</p><p>Diferente de uma placa em evento, o naming é permanente. A marca passa a fazer parte do cenário e aparece em todo conteúdo produzido ali, por quem treina, ensina, grava ou visita o clube.</p>",
         ["recovery", "gluteus-zone", "photo-spot"],
         "Naming e ativações de marca | WeNorth Club",
         "Naming de ambientes e ativações de marca no WeNorth Club: a marca no letreiro, no painel e no cenário de quem treina, grava e posta, em Curitiba."),
        ("eventos-e-lancamentos", "Eventos e lançamentos", "Lançamentos, encontros e experiências no clube.", "a08",
         'Lançamentos com o público <span class="u">certo</span>.',
         "<p>O clube recebe lançamentos, encontros e experiências de marcas parceiras, com a curadoria de público que um evento aberto não tem: personal trainers, empresários, profissionais da saúde e influenciadores que formam opinião no setor.</p><p>A North Room, o lounge e o salão multiesportes podem ser combinados conforme o formato. A marca também pode entregar produtos diretamente nas mãos de quem forma opinião.</p>",
         ["north-room", "photo-spot", "salao-multiesportes"],
         "Eventos e lançamentos de marcas | WeNorth Club",
         "Lançamentos, encontros e experiências de marca no WeNorth Club, com público de personal trainers, empresários, profissionais da saúde e influenciadores."),
        ("midia-espontanea", "Mídia espontânea", "A marca no enquadramento de quem treina, grava e posta.", "a03",
         'A marca em cada <span class="u">post</span>.',
         "<p>Os ambientes do clube foram desenhados a partir de uma pergunta: onde as pessoas naturalmente tiram foto e gravam vídeo? É ali que a marca parceira aparece, de forma orgânica, no conteúdo de quem visita o clube.</p><p>Cada post publicado por influenciadores, profissionais e convidados carrega o cenário, e com ele a marca. É mídia que não depende de anúncio, gerada pela rotina do clube.</p>",
         ["photo-spot", "vestiario", "estudio-de-podcast"],
         "Mídia espontânea para marcas | WeNorth Club",
         "Mídia espontânea no WeNorth Club: ambientes desenhados para foto e vídeo, com a marca parceira no enquadramento de quem treina, grava e posta."),
    ]
    url = "/para-marcas/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Para marcas")]
    faq = [
        ("Quais são as formas de parceria?", "Posicionamento ao lado dos principais professores, doutores e influenciadores, venda e retorno, eventos e integrações, entrega de produtos, ativações e naming e mídia espontânea."),
        ("O site informa valores e cotas?", F("Política de apresentação de valores", "Não. Valores e formatos de parceria são apresentados em conversa com a equipe, de acordo com o objetivo de cada marca.")),
        ("Que tipo de marca combina com o clube?", F("Perfil de marca parceira", "Marcas ligadas a treino, saúde, nutrição, recuperação, vestuário, tecnologia e bem-estar, além de empresas de outros mercados que queiram falar com o público do fitness e wellness.")),
    ]
    corpo = phero(crumbs, "Para marcas e parceiros", 'O que a sua marca <span class="u">vive</span> aqui.',
                  "Presença física e digital ao lado de quem compra, de quem indica e de quem forma opinião no fitness e wellness.",
                  "/img/p-marcas.webp", '<a class="btn" id="btn-cta-marcas" href="/convite/">Quero ser parceiro</a><a class="btn ghost" href="/ambientes/">Ver os ambientes</a>', cap=False)
    corpo += f'''
  <section class="band paper">
    <div class="wrap">
      <p class="eyebrow">Seis benefícios</p>
      <h2>Por que estar no <span class="u">clube</span>.</h2>
      <div class="benefits">
        <div class="benefit"><h3>Posicionamento</h3><p>Ao lado dos principais professores, doutores e influenciadores do país.</p></div>
        <div class="benefit"><h3>Venda e retorno</h3><p>Acesso direto a quem compra e a quem indica.</p></div>
        <div class="benefit"><h3>Eventos e integrações</h3><p>Lançamentos, encontros e experiências no clube.</p></div>
        <div class="benefit"><h3>Entrega de produtos</h3><p>A marca nas mãos de quem forma opinião.</p></div>
        <div class="benefit"><h3>Ativações e naming</h3><p>Espaços com o nome da marca.</p></div>
        <div class="benefit"><h3>Mídia espontânea</h3><p>A marca no enquadramento de quem treina, grava e posta.</p></div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <p class="eyebrow">Formatos</p>
      <h2>Como a marca <span class="u">aparece</span>.</h2>
      <div class="cards">{"".join(card(f"/para-marcas/{s}/", f"/img/{im}.webp", f"{n}, imagem ilustrativa", "Para marcas", n, d) for s, n, d, im, *_ in subs)}</div>
    </div>
  </section>

  <section class="band" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">Como funciona</p>
      <h2>Do primeiro contato à <span class="u">ativação</span>.</h2>
      {F("Etapas do processo comercial com marcas", '<div class="steps"><div><h3>Conversa</h3><p>A equipe entende o objetivo da marca, o público que ela quer alcançar e o momento do produto.</p></div><div><h3>Proposta</h3><p>Formatos, ambientes e calendário são combinados em uma proposta sob medida.</p></div><div><h3>Ativação</h3><p>A marca entra no clube: naming, eventos, entregas e presença no conteúdo.</p></div></div>')}
    </div>
  </section>

  <section class="band paper">
    <div class="wrap">
      <p class="eyebrow">Perguntas frequentes</p>
      <h2>Parcerias com <span class="u">marcas</span>.</h2>
{faq_html(faq)}
    </div>
  </section>'''
    pagina(url, "Para marcas | Patrocínio, naming e ativações no WeNorth Club",
           "Posicionamento, venda e retorno, eventos, entrega de produtos, naming e mídia espontânea: as oportunidades para marcas no WeNorth Club, em Curitiba.",
           corpo, crumbs=crumbs, schema=[b.faq_ld(faq)], og_img="/img/p-marcas.jpg", prioridade="0.9")

    for slug, nome, curto, img, h2, fic, ambs, titulo, desc in subs:
        url = f"/para-marcas/{slug}/"
        b.em_pagina(url)
        crumbs = [("/", "Início"), ("/para-marcas/", "Para marcas"), (url, nome)]
        outros = " · ".join(f'<a href="/para-marcas/{s}/">{n}</a>' for s, n, *_ in subs if s != slug)
        corpo = phero(crumbs, "Para marcas", nome, curto, f"/img/{img}.webp",
                      '<a class="btn" id="btn-cta-marcas" href="/convite/">Quero ser parceiro</a>')
        corpo += f'''
  <section class="band">
    <div class="wrap two">
      <div>
        <p class="eyebrow">{nome}</p>
        <h2>{h2}</h2>
      </div>
      <div class="prose">
        {F(f"Texto da página {nome}", fic)}
        <p>Outros formatos: {outros}. Ou veja <a href="/para-marcas/">todas as oportunidades para marcas</a>.</p>
      </div>
    </div>
  </section>

  <section class="band" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">Onde acontece</p>
      <h2>Ambientes <span class="u">indicados</span>.</h2>
      <div class="cards">{"".join(amb_card(amb(a)) for a in ambs)}</div>
    </div>
  </section>'''
        pagina(url, titulo, desc, corpo, crumbs=crumbs, og_img=f"/img/{img}.jpg", prioridade="0.7")

    # ======================================================================
    # CONTATO E CONVITE
    # ======================================================================
    url = "/contato/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Contato")]
    corpo = phero(crumbs, "Contato", 'Fale com a <span class="u">equipe</span>.',
                  "Convites, parcerias de marca, locação da North Room e imprensa.", "/img/a02.webp",
                  '<a class="btn" id="btn-cta-pagina" href="/convite/">Pedir convite</a><a class="btn ghost" href="https://wa.me/554188239396" target="_blank" rel="noopener">WhatsApp</a>')
    corpo += f'''
  <section class="band">
    <div class="wrap two">
      <div class="prose">
        <h2 style="margin-top:0">Onde <span class="u">estamos</span>.</h2>
        <p><strong>Endereço</strong><br>Rua Eng. Arthur Bettes, 419<br>Portão · Curitiba/PR</p>
        <p><a href="https://www.google.com/maps/search/?api=1&amp;query=Rua+Eng.+Arthur+Bettes,+419,+Port%C3%A3o,+Curitiba,+PR" target="_blank" rel="noopener">Ver no Google Maps</a></p>
        <p><strong>WhatsApp</strong><br><a href="https://wa.me/554188239396" target="_blank" rel="noopener">(41) 98823-9396</a></p>
        <p><strong>E-mail</strong><br><a href="mailto:contato@ptadigital.com.br">contato@ptadigital.com.br</a></p>
        <p><strong>Inauguração prevista</strong><br>Fevereiro de 2027</p>
      </div>
      <div class="prose">
        <h2 style="margin-top:0">Como podemos <span class="u">ajudar</span>.</h2>
        {F("Assuntos atendidos pela equipe e prazo de resposta", "<ul><li><strong>Convite:</strong> para profissionais, empresários e influenciadores que querem fazer parte do clube.</li><li><strong>Marcas:</strong> parcerias, naming, eventos e ativações.</li><li><strong>Locação:</strong> North Room para treinamentos, imersões e encontros de empresas.</li><li><strong>Imprensa:</strong> entrevistas, pautas e visitas.</li></ul><p>A equipe responde em horário comercial, de segunda a sexta-feira.</p>")}
      </div>
    </div>
  </section>'''
    pagina(url, "Contato | WeNorth Club, Curitiba",
           "Fale com o WeNorth Club: convites, parcerias de marca, locação da North Room e imprensa. Rua Eng. Arthur Bettes, 419, Portão, Curitiba/PR.",
           corpo, crumbs=crumbs, schema=[{"@type": "ContactPage", "name": "Contato", "url": b.DOMINIO + url, "about": {"@id": b.DOMINIO + "/#org"}}],
           og_img="/img/a02.jpg", prioridade="0.8")

    url = "/convite/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Convite")]
    corpo = phero(crumbs, "Acesso apenas por convite", 'Peça o seu <span class="u">convite</span>.',
                  "O acesso ao WeNorth Club é feito apenas por convite, para reunir as pessoas certas no mesmo ambiente.",
                  "/img/a03.webp", '<a class="btn" id="btn-cta-convite" href="#contato">Pedir convite</a>')
    corpo += f'''
  <section class="band">
    <div class="wrap">
      <p class="eyebrow">Como funciona</p>
      <h2>Três <span class="u">passos</span>.</h2>
      {F("Etapas do pedido de convite (quem analisa e como responde)", '<div class="steps"><div><h3>Pedido</h3><p>Preencha nome, e-mail e telefone no formulário. Leva menos de um minuto.</p></div><div><h3>Conversa</h3><p>A equipe entra em contato para entender sua atuação e o que você busca no clube.</p></div><div><h3>Convite</h3><p>Com o perfil alinhado, você recebe o convite e a agenda das próximas atividades.</p></div></div>')}
    </div>
  </section>

  <section class="band paper">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Para quem é</p>
        <h2>Quem move o <span class="u">mercado</span>.</h2>
      </div>
      <div class="prose">
        <ul>
          <li><strong>Empresários:</strong> donos de academias, estúdios e negócios do setor, além de líderes de outros mercados.</li>
          <li><strong>Influenciadores:</strong> do fitness, do wellness, da saúde e do business.</li>
          <li><strong>Professores e doutores:</strong> nomes da ciência do exercício no país.</li>
          <li><strong>Profissionais da saúde:</strong> médicos, nutricionistas e fisioterapeutas.</li>
          <li><strong>Personal trainers:</strong> profissionais que atendem a classe A.</li>
          <li><strong>Marcas parceiras:</strong> as empresas que fazem parte do ecossistema.</li>
        </ul>
        <p>A exclusividade é curadoria, não barreira de status. Saiba mais sobre a <a href="/comunidade/">comunidade</a>.</p>
      </div>
    </div>
  </section>'''
    pagina(url, "Peça seu convite | WeNorth Club",
           "O WeNorth Club tem acesso apenas por convite. Empresários, profissionais da saúde, personal trainers, influenciadores e marcas podem pedir o convite.",
           corpo, crumbs=crumbs, og_img="/img/a03.jpg", prioridade="0.8")

    # ======================================================================
    # BLOG
    # ======================================================================
    textos = textos_blog()
    url = "/blog/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Blog")]
    tags = "".join(f'<a href="/blog/{c}/">{n}</a>' for c, (n, _) in CATS.items())
    corpo = phero(crumbs, "Blog WeNorth Club", 'Negócios, formação e <span class="u">wellness</span>.',
                  "Artigos sobre o mercado de fitness e wellness, a formação de profissionais da saúde e os bastidores do clube.",
                  "/img/a07.webp", cap=False)
    corpo += f'''
  <section class="band">
    <div class="wrap">
      <nav class="tags" aria-label="Categorias" style="margin-top:0">{tags}</nav>
      <div class="cards">{"".join(post_card(p) for p in reversed(POSTS))}</div>
    </div>
  </section>'''
    pagina(url, "Blog | WeNorth Club",
           "Artigos do WeNorth Club sobre negócios no fitness, networking, mídia espontânea, pós-graduação presencial, recovery, conteúdo e bastidores do clube.",
           corpo, crumbs=crumbs, schema=[{"@type": "Blog", "name": "Blog WeNorth Club", "url": b.DOMINIO + url, "publisher": {"@id": b.DOMINIO + "/#org"}}],
           og_img="/img/a07.jpg", prioridade="0.8")

    for c, (nome, desc_cat) in CATS.items():
        url = f"/blog/{c}/"
        b.em_pagina(url)
        crumbs = [("/", "Início"), ("/blog/", "Blog"), (url, nome)]
        atual = ' aria-current="page"'
        tags = "".join(f'<a href="/blog/{x}/"{atual if x == c else ""}>{n}</a>' for x, (n, _) in CATS.items())
        corpo = phero(crumbs, "Blog · Categoria", nome, desc_cat, "/img/a07.webp", cap=False)
        corpo += f'''
  <section class="band">
    <div class="wrap">
      <nav class="tags" aria-label="Categorias" style="margin-top:0">{tags}</nav>
      <div class="cards">{"".join(post_card(p) for p in reversed(posts_de(c)))}</div>
    </div>
  </section>'''
        pagina(url, f"{nome} | Blog WeNorth Club", f"{desc_cat} Artigos do blog do WeNorth Club.", corpo,
               crumbs=crumbs, og_img="/img/a07.jpg", prioridade="0.5")

    for p in POSTS:
        url = f"/blog/{p['slug']}/"
        b.em_pagina(url)
        nome_cat = CATS[p["cat"]][0]
        crumbs = [("/", "Início"), ("/blog/", "Blog"), (f"/blog/{p['cat']}/", nome_cat), (url, p["titulo"])]
        texto = textos[p["slug"]]
        palavras = len(re.sub(r"<[^>]+>", " ", texto).split())
        minutos = max(2, round(palavras / 200))
        rel = [x for x in POSTS if x["slug"] != p["slug"] and x["cat"] == p["cat"]]
        rel += [x for x in POSTS if x["slug"] != p["slug"] and x not in rel]
        artigo = texto if p["slug"] == "como-nasceu-a-marca-wenorth" else F("Artigo completo (texto, autoria e data)", texto)
        corpo = phero(crumbs, f"Blog · {nome_cat}", p["titulo"], p["resumo"], f"/img/{p['img']}.webp", cap=False)
        corpo = corpo.replace("</h1>", f'</h1>\n      <div class="post-meta"><span>Por <b>Equipe WeNorth Club</b></span><span><time datetime="{p["data"]}">{data_br(p["data"])}</time></span><span>{minutos} min de leitura</span></div>', 1)
        corpo += f'''
  <article class="band">
    <div class="wrap">
      <figure class="figure-wide" style="margin-bottom:56px"><img src="/img/{p['img']}.webp" alt="{p['titulo']}" width="1200" height="675"><figcaption>Imagem ilustrativa</figcaption></figure>
      <div class="prose">
        {artigo}
      </div>
    </div>
  </article>

  <section class="band" style="padding-top:0">
    <div class="wrap">
      <p class="eyebrow">Continue lendo</p>
      <h2>Artigos <span class="u">relacionados</span>.</h2>
      <div class="cards">{"".join(post_card(x) for x in rel[:3])}</div>
    </div>
  </section>'''
        art = {"@type": "BlogPosting", "headline": p["titulo"], "description": p["resumo"],
               "image": f"{b.DOMINIO}/img/{p['img']}.jpg", "datePublished": p["data"], "dateModified": p["data"],
               "author": {"@type": "Organization", "name": "Equipe WeNorth Club", "url": b.DOMINIO + "/"},
               "publisher": {"@id": b.DOMINIO + "/#org"}, "mainEntityOfPage": b.DOMINIO + url,
               "articleSection": nome_cat, "inLanguage": "pt-BR", "wordCount": palavras}
        titulo_seo = f"{p['titulo']} | WeNorth Club" if len(p["titulo"]) <= 50 else p["titulo"]
        pagina(url, titulo_seo,
               p["resumo"], corpo, crumbs=crumbs, schema=[art], og_img=f"/img/{p['img']}.jpg", og_type="article", prioridade="0.6")

    # ======================================================================
    # LEGAL, OBRIGADO, 404
    # ======================================================================
    url = "/politica-de-privacidade/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Política de Privacidade")]
    corpo = phero(crumbs, "Legal", "Política de Privacidade", "Como o WeNorth Club coleta, usa e protege os seus dados pessoais, de acordo com a LGPD.", "/img/hero.webp", cap=False)
    corpo += f'''
  <section class="band">
    <div class="wrap">
      <div class="prose">
        {F("Política de Privacidade inteira: precisa de revisão jurídica, razão social e CNPJ do controlador", POLITICA)}
      </div>
    </div>
  </section>'''
    pagina(url, "Política de Privacidade | WeNorth Club",
           "Política de Privacidade do WeNorth Club: quais dados coletamos, para que usamos, cookies, compartilhamento e seus direitos segundo a LGPD.",
           corpo, crumbs=crumbs, cta_final=False, prioridade="0.2")

    url = "/termos-de-uso/"
    b.em_pagina(url)
    crumbs = [("/", "Início"), (url, "Termos de Uso")]
    corpo = phero(crumbs, "Legal", "Termos de Uso", "Condições de uso do site do WeNorth Club.", "/img/hero.webp", cap=False)
    corpo += f'''
  <section class="band">
    <div class="wrap">
      <div class="prose">
        {F("Termos de Uso inteiros: precisam de revisão jurídica", TERMOS)}
      </div>
    </div>
  </section>'''
    pagina(url, "Termos de Uso | WeNorth Club", "Termos de Uso do site do WeNorth Club: conteúdo, imagens ilustrativas, propriedade intelectual, formulários e responsabilidades.",
           corpo, crumbs=crumbs, cta_final=False, prioridade="0.2")

    url = "/obrigado/"
    b.em_pagina(url)
    b.EXTRA_TITULOS[url] = "Obrigado"
    corpo = f'''  <section class="band notfound">
    <div class="wrap">
      <p class="eyebrow">Recebemos o seu contato</p>
      <h1 style="font-size:clamp(40px,6vw,80px);color:var(--white);max-width:16ch">Obrigado. Falamos com você em <span class="u">breve</span>.</h1>
      {F("Mensagem de confirmação e prazo de retorno", '<p class="lede">A equipe do WeNorth Club vai entrar em contato pelo WhatsApp ou e-mail informado.</p>')}
      <div class="ctas" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:38px"><a class="btn" href="/ambientes/">Conhecer os ambientes</a><a class="btn ghost" href="/blog/">Ler o blog</a></div>
    </div>
  </section>'''
    pagina(url, "Obrigado | WeNorth Club", "Recebemos o seu contato. A equipe do WeNorth Club vai falar com você em breve.",
           corpo, noindex=True, cta_final=False)

    url = "/404.html"
    b.em_pagina(url)
    corpo = '''  <section class="band notfound">
    <div class="wrap">
      <p class="eyebrow">Erro 404</p>
      <h1 style="font-size:clamp(40px,6vw,80px);color:var(--white);max-width:16ch">Esta página não está no <span class="u">mapa</span>.</h1>
      <p class="lede">O endereço pode ter mudado. Volte ao início ou conheça o clube.</p>
      <div class="ctas" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:38px"><a class="btn" href="/">Voltar ao início</a><a class="btn ghost" href="/o-clube/">O clube</a><a class="btn ghost" href="/blog/">Blog</a></div>
    </div>
  </section>'''
    pagina(url, "Página não encontrada | WeNorth Club", "A página que você procura não foi encontrada.", corpo, noindex=True, cta_final=False)


# ==========================================================================
# Textos longos
# ==========================================================================
POLITICA = """<p><em>Última atualização: 18 de novembro de 2026.</em></p>
<p>Esta Política de Privacidade explica como o WeNorth Club trata os dados pessoais de quem visita este site e preenche os formulários, de acordo com a Lei Geral de Proteção de Dados (Lei 13.709/2018, LGPD).</p>
<h2>1. Quem é o controlador</h2>
<p>O controlador dos dados é o WeNorth Club, integrante do grupo WeNorth, com endereço na Rua Eng. Arthur Bettes, 419, Portão, Curitiba/PR. Contato do encarregado (DPO): <a href="mailto:contato@ptadigital.com.br">contato@ptadigital.com.br</a>.</p>
<h2>2. Dados que coletamos</h2>
<ul><li><strong>Dados informados por você:</strong> nome, e-mail e telefone, quando você preenche o formulário de convite ou de parceria.</li><li><strong>Dados de origem da visita:</strong> parâmetros de campanha (UTMs) e o endereço da página em que o formulário foi enviado.</li><li><strong>Dados de navegação:</strong> informações técnicas coletadas por cookies, como páginas visitadas e tipo de dispositivo.</li></ul>
<h2>3. Para que usamos os dados</h2>
<ul><li>Responder ao seu pedido de convite, parceria ou contato.</li><li>Enviar informações sobre o clube, eventos e programas, quando você autorizar.</li><li>Entender quais canais e campanhas trazem visitantes, para melhorar a comunicação.</li><li>Cumprir obrigações legais.</li></ul>
<h2>4. Base legal</h2>
<p>Tratamos os dados com base no seu consentimento, na execução de procedimentos preliminares a um contrato solicitados por você e no legítimo interesse do WeNorth Club, sempre respeitando seus direitos.</p>
<h2>5. Compartilhamento</h2>
<p>Os dados podem ser compartilhados com empresas do grupo WeNorth, como a Personal Trainer Academy, e com fornecedores que nos ajudam a operar o site e o atendimento, como ferramentas de automação e de CRM. Não vendemos dados pessoais.</p>
<h2>6. Cookies</h2>
<p>Usamos cookies para o funcionamento do site e para medir a navegação. Você pode aceitar ou recusar no aviso exibido na primeira visita e pode apagar os cookies a qualquer momento nas configurações do navegador.</p>
<h2>7. Por quanto tempo guardamos</h2>
<p>Mantemos os dados pelo tempo necessário para atender à finalidade da coleta ou para cumprir obrigações legais. Depois disso, eles são excluídos ou anonimizados.</p>
<h2>8. Seus direitos</h2>
<p>Você pode pedir a confirmação do tratamento, o acesso, a correção, a anonimização, a portabilidade e a exclusão dos seus dados, além de revogar o consentimento. Basta escrever para <a href="mailto:contato@ptadigital.com.br">contato@ptadigital.com.br</a>.</p>
<h2>9. Segurança</h2>
<p>Adotamos medidas técnicas e administrativas para proteger os dados contra acesso não autorizado, perda ou alteração.</p>
<h2>10. Alterações</h2>
<p>Esta política pode ser atualizada. A data da última versão fica sempre no topo da página.</p>"""

TERMOS = """<p><em>Última atualização: 18 de novembro de 2026.</em></p>
<p>Ao acessar o site do WeNorth Club, você concorda com estes Termos de Uso.</p>
<h2>1. Sobre o site</h2>
<p>Este site apresenta o WeNorth Club, o clube de negócios do fitness e wellness em Curitiba/PR, com inauguração prevista para fevereiro de 2027. O conteúdo é informativo e pode ser alterado sem aviso.</p>
<h2>2. Imagens ilustrativas</h2>
<p>As imagens dos ambientes são ilustrativas e representam um projeto em desenvolvimento. O resultado final pode ser diferente.</p>
<h2>3. Acesso ao clube</h2>
<p>O acesso ao WeNorth Club é feito apenas por convite. O envio de um formulário não garante convite, parceria ou vaga em qualquer atividade.</p>
<h2>4. Propriedade intelectual</h2>
<p>Marcas, logotipos, textos e imagens deste site pertencem ao grupo WeNorth ou a seus licenciantes. Não é permitido copiar ou usar esse material sem autorização.</p>
<h2>5. Formulários</h2>
<p>Ao preencher um formulário, você declara que as informações são verdadeiras. O tratamento dos dados segue a <a href="/politica-de-privacidade/">Política de Privacidade</a>.</p>
<h2>6. Links externos</h2>
<p>O site pode ter links para outros sites. O WeNorth Club não é responsável pelo conteúdo nem pelas práticas de privacidade desses sites.</p>
<h2>7. Contato</h2>
<p>Dúvidas sobre estes termos: <a href="mailto:contato@ptadigital.com.br">contato@ptadigital.com.br</a>.</p>"""


def textos_blog():
    return {
        "o-que-e-um-clube-de-negocios-do-fitness": """
<p>O mercado de fitness e wellness cresceu, mas cresceu em partes. Há treino sem método, influência sem profundidade e networking sem densidade. Cada peça existe, mas em lugares diferentes, com pessoas diferentes, sem conversa entre elas.</p>
<p>Um clube de negócios do fitness nasce para juntar essas peças em um só endereço. Não é uma academia com uma sala de reunião ao lado. É um espaço desenhado para que formação, conteúdo e negócios aconteçam juntos, todos os dias.</p>
<h2>A diferença para uma academia</h2>
<p>A academia é organizada em torno do treino do aluno. O clube de negócios é organizado em torno das pessoas que movem o mercado: empresários, personal trainers, professores, profissionais da saúde, influenciadores e marcas.</p>
<p>O treino continua lá, com salão, equipamentos e áreas de recuperação. Mas ele divide o espaço com uma sala de aulas, um estúdio de podcast, estações de trabalho e ambientes pensados para foto e vídeo. O treino vira também conteúdo, aula e ponto de encontro.</p>
<h2>Os três pilares</h2>
<h3>Business</h3>
<p>Mentorias, lançamentos digitais e encontros com empresários de dentro e de fora do setor. O objetivo é gerar negócios entre pessoas que, em outro contexto, dificilmente estariam na mesma sala.</p>
<h3>Education</h3>
<p>Pós-graduações, cursos e imersões ao lado do salão de treino. A teoria fica a poucos passos da prática.</p>
<h3>Wellness</h3>
<p>Treino, recuperação e conteúdo com profundidade, produzido por quem treina e ensina no próprio clube.</p>
<h2>Por que o acesso é por convite</h2>
<p>Um clube de negócios depende de densidade. Se qualquer pessoa entra, o ambiente vira um evento aberto, com muito volume e pouca troca. O convite funciona como curadoria: reúne as pessoas certas no mesmo ambiente. Não é uma barreira de status, é uma forma de garantir que cada encontro tenha valor.</p>
<h2>O que esperar de um clube como esse</h2>
<ul><li>Uma agenda viva, com atividades ao longo do ano inteiro.</li><li>Ambientes que funcionam como cenário para conteúdo.</li><li>Acesso a referências técnicas e de gestão do setor.</li><li>Conexões com marcas que querem falar com quem forma opinião.</li></ul>
<p>O <a href="/o-clube/">WeNorth Club</a> é o primeiro clube de negócios do fitness e wellness no Brasil, com mais de 600 m² em Curitiba e inauguração prevista para fevereiro de 2027. Para fazer parte, <a href="/convite/">peça o seu convite</a>.</p>""",

        "networking-no-mercado-fitness": """
<p>Quem trabalha no fitness conhece o roteiro: feiras cheias, palestras em auditórios grandes, trocas rápidas de contato e pouca continuidade depois. O volume é alto. A densidade, nem sempre.</p>
<h2>Volume não é o mesmo que conexão</h2>
<p>Conhecer muitas pessoas em pouco tempo dá a sensação de networking. Mas negócio nasce de contexto: entender o que o outro faz, onde ele quer chegar e o que vocês podem construir juntos. Isso exige tempo e repetição, coisas que um evento de um dia raramente oferece.</p>
<h2>O que é densidade</h2>
<p>Densidade é a proporção de encontros que geram algo útil. Um ambiente denso tem menos pessoas, mas pessoas mais alinhadas, que se encontram com frequência e em situações diferentes: numa aula, num treino, numa gravação, num lançamento.</p>
<h2>Como criar um ambiente de curadoria</h2>
<ul><li><strong>Selecionar quem participa.</strong> O acesso por convite garante que as pessoas na sala tenham algo a trocar.</li><li><strong>Misturar perfis.</strong> Empresários, profissionais da saúde, influenciadores e marcas enxergam o mercado de lugares diferentes. É no cruzamento que surgem as ideias.</li><li><strong>Criar rotina.</strong> Uma agenda contínua transforma contatos em relações.</li><li><strong>Dar motivo para estar junto.</strong> Formação, conteúdo e eventos são a desculpa. O negócio vem depois.</li></ul>
<h2>Conexões além do fitness</h2>
<p>Parte das melhores oportunidades está fora do setor. Empresários de construção, automotivo, aviação e varejo têm experiência em gestão, expansão e marca que pode ser aplicada ao fitness. E muitos deles querem entender esse mercado de perto.</p>
<p>No <a href="/business/">pilar Business</a> do WeNorth Club, esses encontros fazem parte da agenda. Para participar, <a href="/convite/">peça o seu convite</a>.</p>""",

        "midia-espontanea-em-academias": """
<p>Toda academia é fotografada. A questão é onde. Quem treina registra a chegada, o exercício, a recuperação e o espelho do vestiário. Esses momentos se repetem todos os dias e geram uma quantidade enorme de conteúdo publicado por alunos, profissionais e influenciadores.</p>
<p>Mídia espontânea é a presença de marca que aparece nesse conteúdo sem que ninguém precise anunciar. E ela começa no projeto do ambiente.</p>
<h2>Comece pela pergunta certa</h2>
<p>Em vez de perguntar onde cabe uma placa, a pergunta é: <strong>onde as pessoas naturalmente tiram foto e gravam vídeo?</strong> A resposta mostra os pontos de maior visibilidade, e é ali que a marca deve estar.</p>
<h2>Os pontos que mais aparecem</h2>
<ul><li><strong>A chegada.</strong> Recepção e photo spot são o primeiro enquadramento de quem entra.</li><li><strong>A execução.</strong> A parede atrás de quem grava o exercício aparece em todo vídeo de treino.</li><li><strong>A recuperação.</strong> A banheira de gelo virou um dos momentos mais filmados do fitness.</li><li><strong>O espelho.</strong> A selfie pós-treino é quase um ritual.</li><li><strong>A conversa.</strong> Em um estúdio de podcast, a marca fica atrás de quem está no microfone.</li></ul>
<h2>Naming: o ambiente com nome de marca</h2>
<p>O formato mais forte de mídia espontânea é o naming, quando o ambiente recebe o nome da marca. Recovery by, Gluteus Zone by, Podcast by. O nome deixa de ser um anúncio e passa a fazer parte do lugar.</p>
<h2>Por que funciona</h2>
<p>Porque é orgânico. A marca aparece no conteúdo de quem tem audiência, num contexto real de uso, e isso se repete a cada visita. Não depende de campanha nem de verba de mídia.</p>
<p>Os <a href="/ambientes/">dez ambientes do WeNorth Club</a> foram desenhados com essa lógica. Veja as <a href="/para-marcas/midia-espontanea/">oportunidades de mídia espontânea para marcas</a>.</p>""",

        "pos-graduacao-presencial-em-curitiba": """
<p>A pós-graduação a distância facilitou o acesso à formação. Mas, em áreas como treinamento, biomecânica e saúde, há conteúdos que ganham outra dimensão quando vistos de perto, com o movimento acontecendo na frente do aluno.</p>
<h2>O formato: dois fins de semana por mês</h2>
<p>As pós-graduações do WeNorth Club têm aulas presenciais em dois fins de semana por mês. O formato permite que o profissional mantenha a rotina de atendimentos durante a semana e concentre a formação em encontros intensivos.</p>
<h2>A sala ao lado do salão</h2>
<p>A North Room, onde acontecem as aulas, fica a poucos passos do salão multiesportes. O que é discutido na sala pode ser demonstrado, testado e observado no treino, no mesmo dia. A formação deixa de ser só teórica e fica perto da prática.</p>
<h2>O que o formato presencial acrescenta</h2>
<ul><li><strong>Demonstração real.</strong> Técnica, ajustes e progressões vistos ao vivo.</li><li><strong>Turma e networking.</strong> Colegas de diferentes cidades e perfis, convivendo nos mesmos fins de semana.</li><li><strong>Acesso a referências.</strong> Professores, mestres e doutores no mesmo ambiente.</li><li><strong>Contexto de mercado.</strong> As aulas acontecem dentro de um clube de negócios, ao lado de empresários e marcas do setor.</li></ul>
<h2>Para quem é</h2>
<p>Para personal trainers, profissionais de educação física e da saúde que querem aprofundar a formação técnica e, ao mesmo tempo, estar perto de quem move o mercado.</p>
<p>Conheça o <a href="/education/">pilar Education</a> e os <a href="/programas/">programas do grupo WeNorth</a>.</p>""",

        "formacao-perto-da-pratica": """
<p>Existe uma distância conhecida entre o que se aprende em sala e o que se aplica no treino. O profissional estuda o conceito, mas só vai testá-lo semanas depois, sozinho, com o aluno. Nesse intervalo, parte do conhecimento se perde.</p>
<h2>Encurtar a distância</h2>
<p>Levar a formação para perto da prática significa encurtar esse caminho. Quando a sala de aula fica ao lado do salão de treino, o conceito pode ser visto, executado e corrigido no mesmo dia, com orientação.</p>
<h2>O papel da biomecânica</h2>
<p>A biomecânica é a forma como o grupo WeNorth entende o corpo e o movimento. Ela dá critério técnico às decisões de treino: por que um exercício, por que uma amplitude, por que uma progressão. É uma disciplina que se aprende melhor observando o movimento real.</p>
<h2>Como aplicar na rotina profissional</h2>
<ul><li><strong>Estude com o movimento à vista.</strong> Sempre que possível, ligue a teoria a uma execução concreta.</li><li><strong>Teste cedo.</strong> Aplique o que aprendeu na mesma semana, com alunos reais.</li><li><strong>Registre.</strong> Grave execuções e compare antes e depois.</li><li><strong>Troque com colegas.</strong> A discussão de casos acelera o aprendizado.</li></ul>
<h2>Formação e conteúdo</h2>
<p>Quando a formação acontece perto da prática, ela também gera conteúdo com profundidade. O profissional que ensina e treina no mesmo lugar tem o que mostrar, e com critério.</p>
<p>Saiba mais sobre o <a href="/education/">pilar Education</a> do WeNorth Club e a <a href="/ambientes/north-room/">North Room</a>.</p>""",

        "conteudo-com-profundidade-no-fitness": """
<p>O fitness é um dos temas mais publicados nas redes. Isso trouxe alcance para muitos profissionais, mas também uma onda de conteúdo raso: dicas sem contexto, tendências que somem em semanas e promessas que não se sustentam.</p>
<h2>O que é conteúdo com profundidade</h2>
<p>É o conteúdo que parte de critério técnico, explica o porquê e respeita quem assiste. Não precisa ser longo nem complicado. Precisa ser verdadeiro e útil.</p>
<h2>Quem grava deveria treinar e ensinar</h2>
<p>O conteúdo mais consistente costuma vir de quem vive o assunto. Quem treina, atende alunos e ensina outros profissionais tem repertório para ir além da tendência, porque testa, observa e corrige todos os dias.</p>
<h2>Cinco cuidados para produzir com critério</h2>
<ol><li><strong>Comece pela pergunta do público.</strong> O conteúdo responde a uma dúvida real?</li><li><strong>Mostre o contexto.</strong> Para quem serve, quando faz sentido, quando não faz.</li><li><strong>Evite o clichê.</strong> Frases de efeito envelhecem rápido.</li><li><strong>Use o ambiente a favor.</strong> Um cenário bem pensado dá credibilidade sem distrair.</li><li><strong>Converse com quem sabe.</strong> Podcasts e entrevistas com especialistas aprofundam o tema.</li></ol>
<h2>O ambiente como cenário</h2>
<p>No WeNorth Club, o salão, a Gluteus Zone, o Recovery e o estúdio de podcast foram desenhados para servir de cenário. O espaço ajuda a contar a história, e quem grava pode se concentrar no que importa: o conteúdo.</p>
<p>Conheça o <a href="/wellness/">pilar Wellness</a> e o <a href="/ambientes/estudio-de-podcast/">estúdio de podcast</a> do clube.</p>""",

        "recovery-banheira-de-gelo-sauna-e-compressao": """
<p>A recuperação deixou de ser um detalhe da rotina de treino e passou a ocupar espaço próprio. Em muitos clubes e centros de treinamento, ela ganhou um ambiente dedicado: o recovery.</p>
<h2>O que é um espaço de recovery</h2>
<p>É um ambiente que reúne recursos usados na rotina de recuperação, separado do ritmo do salão. No WeNorth Club, o Recovery tem banheira de gelo, sauna e botas de compressão, em um ambiente de spa.</p>
<h2>Os recursos</h2>
<h3>Banheira de gelo</h3>
<p>A imersão em água fria é um dos recursos mais conhecidos de recuperação e virou também um dos momentos mais filmados do fitness.</p>
<h3>Sauna</h3>
<p>O calor seco faz parte de rotinas de relaxamento e bem-estar em muitas culturas e costuma ser usado depois do treino.</p>
<h3>Botas de compressão</h3>
<p>Equipamentos de compressão pneumática são usados em rotinas de recuperação de membros inferiores.</p>
<p><strong>Importante:</strong> cada recurso tem indicações e cuidados. Antes de incluir qualquer um deles na rotina, converse com um profissional da saúde.</p>
<h2>Por que o recovery virou cenário</h2>
<p>Porque é visual. A banheira de gelo, o vapor da sauna e o ambiente de spa contrastam com o salão de treino e criam um momento fácil de registrar. Não por acaso, o painel atrás da banheira é um dos pontos de maior visibilidade de marca no clube.</p>
<p>Veja o ambiente <a href="/ambientes/recovery/">Recovery</a> e o <a href="/wellness/">pilar Wellness</a> do WeNorth Club.</p>""",

        "como-nasceu-a-marca-wenorth": """
<p>O símbolo da WeNorth é um N em perspectiva. Ele não apenas representa o Norte: ele aponta para ele.</p>
<p>A marca foi criada pelo estúdio Discircle e nasceu às 17h de uma sexta-feira, 24 de julho de 2026.</p>
<h2>A construção, passo a passo</h2>
<ol><li><strong>Tudo começa em um pentágono regular.</strong></li><li><strong>Duplicado, reduzido e empilhado,</strong> ele vira uma forma própria, com dois pentágonos.</li><li><strong>Os dois perdem os vértices inferiores</strong> e se tornam dois trapézios.</li><li><strong>O cruzamento de 58 linhas anguladas</strong> forma a malha estrutural.</li><li><strong>Dessa malha surge o N,</strong> cujo ângulo aponta para o Norte.</li></ol>
<h2>A Estrela</h2>
<p>Do mesmo pentágono nasce a Estrela, símbolo de destaque, orientação e conquista.</p>
<h2>Como a marca é usada</h2>
<p>A marca prefere as versões com símbolo, sempre em uma única cor da paleta. O símbolo vem primeiro, e o descritor CLUB fica em peso mais fino.</p>
<p>A paleta parte do Full Black (#000F0F) e do Dark Green (#002828), com o Soft Gray (#B4D7D7) como fundo claro e o Neon Green (#82E628) como acento, em cerca de 5% a 10% da área. A marca não usa branco nem preto puros, nem gradientes ou sombras pesadas.</p>
<h2>WeNorth e WeNorth Club</h2>
<p>WeNorth é o grupo, que nasce da força da Personal Trainer Academy. O WeNorth Club é a casa desse grupo, em Curitiba, com inauguração prevista para fevereiro de 2027.</p>
<p>Veja a <a href="/a-marca/">página da marca</a> e conheça <a href="/quem-somos/">quem somos</a>.</p>""",
    }
