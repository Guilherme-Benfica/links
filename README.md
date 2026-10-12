# Links: certificações e simulados

Página estilo Linktree com minhas certificações cloud, links dos simulados na Udemy e conteúdo técnico. HTML, CSS e JavaScript puros, sem dependências nem build.

## Como editar

Quase tudo fica em **`certs.js`**:

- **Link da Udemy:** preencha `udemy: 'https://www.udemy.com/course/...'` na certificação. O card vira um botão "Simulado na Udemy" e sobe para o topo da plataforma.
- **Link do badge no Credly:** preencha `badge: '...'` (usado quando não há link da Udemy).
- **Selo "Novo":** adicione `novo: true` na certificação.
- **Nova certificação:** copie uma linha `{ code: '...', name: '...', udemy: '', badge: '' }` dentro da plataforma.

Em `index.html`, a seção **Conteúdo** tem o Medium comentado: descomente e troque `SEU-USUARIO` quando estiver no ar.

Foto de perfil (opcional): coloque `foto.jpg` na raiz. Sem ela aparecem as iniciais.

## Publicar no GitHub Pages

1. Em **Settings > Pages**, escolha **Deploy from a branch**, branch `main`, pasta `/ (root)`.
2. O link será `https://guilherme-benfica.github.io/links/`.
