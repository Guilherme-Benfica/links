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
- `site.js`: botões PT / EN de cada curso e aviso de idioma
- `img/`: capas dos cursos (WebP), selos, foto e imagens de compartilhamento (`og-pt.jpg`, `og-en.jpg`)
- `fonts/`: Bricolage Grotesque e Instrument Sans (SIL Open Font License)
- `favicon.svg`

## SEO

Cada idioma tem a própria URL, com `hreflang`, `canonical`, Open Graph e dados estruturados (Course, Person e FAQ). Para indexar mais rápido, envie `https://guilherme-benfica.github.io/links/sitemap.xml` no Google Search Console.

## Segurança

Medidas aplicadas no projeto, com o item correspondente do OWASP entre parênteses:

| Risco | Como é tratado |
|---|---|
| Script malicioso / XSS (Injection) | Content Security Policy: o navegador só executa o script do próprio site (`site.js`). Não há JavaScript inline, `eval` nem script de terceiros. Os textos são escapados com `html.escape` ao gerar as páginas |
| Bibliotecas e CDNs de terceiros (Vulnerable and Outdated Components) | Nenhuma dependência externa: fontes, imagens e script ficam no próprio repositório, então não há código de terceiros que possa ser trocado ou comprometido |
| Recursos de outra origem (Software and Data Integrity Failures) | A política só permite carregar script, estilo, fonte e imagem do próprio site (`'self'`) |
| Reverse tabnabbing | Todo link que abre em nova aba usa `rel="noopener"`, então a página aberta não consegue controlar a aba de origem |
| Vazamento pelo referrer (Security Misconfiguration) | `strict-origin-when-cross-origin`: sites externos recebem só o domínio, nunca o caminho completo |
| Tráfego sem criptografia (Cryptographic Failures) | Servido só por HTTPS pelo GitHub Pages, com `upgrade-insecure-requests` |
| Envio de dados para fora | `form-action 'none'` e `connect-src` bloqueado: a página não envia dados para lugar nenhum |
| Privacidade (LGPD) | Sem cookies, analytics ou rastreadores. O `localStorage` guarda só se o aviso de idioma foi fechado |
| Segredos no repositório | Não há segredos: cupons e códigos de indicação da Udemy são públicos por natureza |

Não se aplicam ao escopo atual: senhas e autenticação (não há login), injeção de SQL (não há banco de dados), CSRF (não há formulário nem sessão), upload de arquivos e SSRF (não há servidor).

Limitação conhecida: o GitHub Pages não permite configurar cabeçalhos HTTP, então a política vai na tag `<meta>`. Nesse formato, `frame-ancestors` (proteção contra clickjacking) não tem efeito. O risco é baixo porque a página não tem nenhuma ação sensível.

## Publicar no GitHub Pages

Em **Settings > Pages**: **Deploy from a branch**, branch `main`, pasta `/ (root)`.
