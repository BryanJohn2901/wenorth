/* ===== CONFIGURAÇÃO DA PÁGINA (únicas linhas que mudam) ===== */
  const FORM_ID      = 'form_wenorth';
  const WEBHOOK_URL  = 'https://hook.us1.make.com/bj1q14346ezeybpcqjb9ctea89aoatvn?produto=WENORTH';
  const REDIRECT_URL = 'https://wenorthclub.com.br/obrigado/';
  const CTA_IDS      = ['btn-inscreva-nav', 'btn-inscreva-hero', 'btn-garantir-vaga', 'btn-footer-parceiro', 'btn-cta-menu', 'btn-cta-pagina', 'btn-cta-marcas', 'btn-cta-convite'];

  /* ===== UTMs ===== */
  const UTM_KEYS = ['utm_source', 'utm_term', 'utm_campaign', 'utm_medium', 'utm_content'];

  function getUtms() {
    const params = new URLSearchParams(window.location.search);
    const fromUrl = {};
    let hasAny = false;
    UTM_KEYS.forEach(function (k) {
      fromUrl[k] = params.get(k) || '';
      if (fromUrl[k]) hasAny = true;
    });
    if (hasAny) {
      try { UTM_KEYS.forEach(function (k) { sessionStorage.setItem(k, fromUrl[k]); }); } catch (e) {}
      return fromUrl;
    }
    const stored = {};
    try { UTM_KEYS.forEach(function (k) { stored[k] = sessionStorage.getItem(k) || ''; }); }
    catch (e) { UTM_KEYS.forEach(function (k) { stored[k] = ''; }); }
    return stored;
  }

  function fillHiddenFields() {
    const utms = getUtms();
    UTM_KEYS.forEach(function (k) {
      const el = document.getElementById(k);
      if (el) el.value = utms[k];
    });
    const urlEl = document.getElementById('url');
    if (urlEl) urlEl.value = window.location.href;
  }
  fillHiddenFields();

  function buildRedirect() {
    const target = new URL(REDIRECT_URL, window.location.href);
    UTM_KEYS.forEach(function (k) {
      const v = document.getElementById(k)?.value || '';
      if (v && !target.searchParams.has(k)) target.searchParams.set(k, v);
    });
    return target.toString();
  }

  /* ===== POPUP ===== */
  const popup = document.getElementById('popup-inscricao');

  function abrirPopup() {
    fillHiddenFields();
    popup.classList.remove('hidden');
    popup.classList.add('flex');
    document.body.style.overflow = 'hidden';
    setTimeout(function () { document.getElementById('name')?.focus(); }, 50);
  }
  function fecharPopup() {
    popup.classList.add('hidden');
    popup.classList.remove('flex');
    document.body.style.overflow = '';
  }

  CTA_IDS.forEach(function (id) {
    const btn = document.getElementById(id);
    if (btn) btn.addEventListener('click', function (e) { e.preventDefault(); abrirPopup(); });
  });
  document.getElementById('popup-fechar').addEventListener('click', fecharPopup);
  popup.addEventListener('click', function (e) { if (e.target === popup) fecharPopup(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fecharPopup(); });

  /* ===== TELEFONE ===== */
  const inputTel = document.getElementById('phone');
  const erroTel  = document.getElementById('erro-telefone');

  function digitosTelefone(valor) {
    let d = (valor || '').replace(/\D/g, '');
    if (d.length > 11 && d.startsWith('55')) d = d.slice(2);
    return d;
  }
  inputTel.addEventListener('input', function () {
    this.value = this.value.replace(/\D/g, '');
    erroTel.classList.add('hidden');
  });

  /* ===== ENVIO ===== */
  const form      = document.getElementById(FORM_ID);
  const btnEnviar = document.getElementById('btn-enviar-form');
  const textoBtn  = btnEnviar.textContent;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;

    const digitos = digitosTelefone(inputTel.value);
    if (digitos.length < 10 || digitos.length > 11) {
      erroTel.classList.remove('hidden');
      inputTel.focus();
      return;
    }

    fillHiddenFields();

    const nome     = document.getElementById('name').value.trim();
    const email    = document.getElementById('email').value.trim().toLowerCase();
    const telefone = '+55' + digitos;

    const payload = {
      nome: nome,
      email: email,
      telefone: telefone,
      utm_source: document.getElementById('utm_source')?.value || '',
      utm_term: document.getElementById('utm_term')?.value || '',
      utm_campaign: document.getElementById('utm_campaign')?.value || '',
      utm_medium: document.getElementById('utm_medium')?.value || '',
      utm_content: document.getElementById('utm_content')?.value || '',
      url: document.getElementById('url')?.value || window.location.href
    };

    btnEnviar.disabled = true;
    btnEnviar.textContent = 'Enviando...';

    const controller = new AbortController();
    const timer = setTimeout(function () { controller.abort(); }, 15000);

    fetch(WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      signal: controller.signal
    })
      .then(function (res) {
        clearTimeout(timer);
        if (!res.ok) throw new Error('HTTP ' + res.status);
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: 'lead_enviado', form_id: FORM_ID });
        window.location.href = buildRedirect();
      })
      .catch(function () {
        clearTimeout(timer);
        btnEnviar.disabled = false;
        btnEnviar.textContent = textoBtn;
        alert('Não foi possível enviar. Verifique sua conexão e tente novamente.');
      });
  });

  /* ===== COOKIES (LGPD) ===== */
  const cookieBanner = document.getElementById('aviso-cookies');
  try {
    if (!localStorage.getItem('cookies-lgpd-aceito')) cookieBanner.classList.remove('hidden');
  } catch (e) { cookieBanner.classList.remove('hidden'); }
  function salvarCookies(valor) {
    try { localStorage.setItem('cookies-lgpd-aceito', valor); } catch (e) {}
    cookieBanner.classList.add('hidden');
  }
  document.getElementById('btn-cookies-aceitar').addEventListener('click', function () { salvarCookies('true'); });
  document.getElementById('btn-cookies-recusar').addEventListener('click', function () { salvarCookies('false'); });
