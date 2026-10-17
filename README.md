# Simulados AWS: Guilherme Benfica

Página dos meus simulados AWS na Udemy, em português e inglês. HTML e CSS estáticos, sem dependências nem frameworks.

- Português: `https://guilherme-benfica.github.io/links/`
- Inglês: `https://guilherme-benfica.github.io/links/en/`

## Como editar

Textos, cursos e links ficam em **`tools/build_pages.py`**:

- **Cursos e links da Udemy:** lista `COURSES` (um link para cada idioma).
- **Textos da página:** dicionário `TEXT` (`pt` e `en`).

Depois de editar, gere as páginas de novo:

```
python3 tools/build_pages.py
```

Isso reescreve `index.html`, `en/index.html` e `sitemap.xml`. Se mudar `style.css` ou alguma imagem, aumente `VERSION` no script para o navegador não usar a versão antiga em cache.

## Estrutura

- `style.css`: visual das duas páginas
- `img/`: capas dos cursos (WebP), selos, foto e imagens de compartilhamento (`og-pt.jpg`, `og-en.jpg`)
- `fonts/`: Bricolage Grotesque e Instrument Sans (SIL Open Font License)
- `favicon.svg`

## SEO

Cada idioma tem a própria URL, com `hreflang`, `canonical`, Open Graph e dados estruturados (Course, Person e FAQ). Para indexar mais rápido, envie `https://guilherme-benfica.github.io/links/sitemap.xml` no Google Search Console.

## Publicar no GitHub Pages

Em **Settings > Pages**: **Deploy from a branch**, branch `main`, pasta `/ (root)`.
