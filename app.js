(function () {
  'use strict';

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  function certCard(provider, cert) {
    var href = cert.udemy || cert.badge || '';
    var node = el(href ? 'a' : 'div', 'cert' + (cert.udemy ? ' has-udemy' : ''));
    if (href) {
      node.href = href;
      node.target = '_blank';
      node.rel = 'noopener noreferrer';
    }

    var top = el('div', 'cert-top');
    top.appendChild(el('span', 'cert-code', cert.code));
    if (cert.novo) top.appendChild(el('span', 'tag', 'Novo'));
    node.appendChild(top);

    node.appendChild(el('div', 'cert-name', cert.name));

    if (cert.udemy) {
      node.appendChild(el('span', 'cta', 'Simulado na Udemy →'));
      node.setAttribute('aria-label', cert.code + ' ' + cert.name + ' — abrir simulado na Udemy');
    } else if (cert.badge) {
      node.appendChild(el('span', 'cta ghost', 'Ver badge →'));
    }
    return node;
  }

  function providerSection(provider) {
    var section = el('section', 'provider ' + provider.id);
    section.id = provider.id;

    var head = el('div', 'provider-head');
    var titles = el('div');
    titles.appendChild(el('h2', null, provider.name));
    if (provider.tagline) titles.appendChild(el('p', 'tagline', provider.tagline));
    head.appendChild(titles);
    head.appendChild(el('span', 'count', provider.certs.length + 'x'));
    section.appendChild(head);

    var sorted = provider.certs.slice().sort(function (a, b) {
      return (b.udemy ? 1 : 0) - (a.udemy ? 1 : 0);
    });

    var grid = el('div', 'grid');
    sorted.forEach(function (c) { grid.appendChild(certCard(provider, c)); });
    section.appendChild(grid);
    return section;
  }

  var total = 0, simulados = 0;
  PROVIDERS.forEach(function (p) {
    total += p.certs.length;
    p.certs.forEach(function (c) { if (c.udemy) simulados++; });
  });

  // Estatísticas do topo
  var stats = document.getElementById('stats');
  if (stats) {
    function stat(n, label) {
      var s = el('div', 'stat');
      s.appendChild(el('strong', null, String(n)));
      s.appendChild(el('span', null, label));
      return s;
    }
    stats.appendChild(stat(total, 'certificações'));
    stats.appendChild(stat(PROVIDERS.length, 'plataformas'));
    stats.appendChild(simulados > 0
      ? stat(simulados, simulados === 1 ? 'simulado na Udemy' : 'simulados na Udemy')
      : stat('Em breve', 'simulados na Udemy'));
  }

  // Navegação por plataforma
  var nav = document.getElementById('nav');
  if (nav) {
    PROVIDERS.forEach(function (p) {
      var a = el('a', 'chip ' + p.id, p.name);
      a.href = '#' + p.id;
      nav.appendChild(a);
    });
  }

  // Seções por plataforma
  var root = document.getElementById('providers');
  if (root) {
    PROVIDERS.forEach(function (p) { root.appendChild(providerSection(p)); });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  var linkedin = document.getElementById('btn-linkedin');
  if (linkedin) linkedin.href = PROFILE.linkedin;
  var credly = document.getElementById('btn-credly');
  if (credly) credly.href = PROFILE.credly;
})();
