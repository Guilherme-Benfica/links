/* Comportamento da página: botões PT / EN de cada curso e aviso de idioma. */
'use strict';
(function () {
  document.querySelectorAll('.card').forEach(function (card) {
    var group = card.querySelector('.clang'), link = card.querySelector('h3 a'),
        img = card.querySelector('.card-media img'), label = card.querySelector('.btn-label');
    group.hidden = false;
    group.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var l = btn.getAttribute('data-set');
        group.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        link.href = card.getAttribute('data-href-' + l);
        link.setAttribute('aria-label', card.getAttribute('data-aria-' + l));
        img.src = card.getAttribute('data-img-' + l);
        label.textContent = card.getAttribute('data-btn-' + l);
      });
    });
  });
})();
(function () {
  var hint = document.getElementById('hint'), key = 'links-hint-closed';
  var pageLang = hint.getAttribute('data-lang');
  var nav = (navigator.languages && navigator.languages[0]) || navigator.language || '';
  var wantsPt = /^pt/i.test(nav);
  var closed = false;
  try { closed = localStorage.getItem(key) === '1'; } catch (e) {}
  if (!closed && ((pageLang === 'pt' && nav && !wantsPt) || (pageLang === 'en' && wantsPt))) hint.hidden = false;
  document.getElementById('hint-close').addEventListener('click', function () {
    hint.hidden = true;
    try { localStorage.setItem(key, '1'); } catch (e) {}
  });
})();
