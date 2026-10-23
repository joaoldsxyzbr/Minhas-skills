# Minhas Skills

Coleção portável de skills para desenvolvimento, produto, Cloudflare, GitHub e pesquisa aprofundada.

O objetivo é reunir práticas úteis em um pacote revisável, sem mecanismos próprios de telemetria ou rastreamento. As skills são instruções em Markdown; este repositório não adiciona scripts de execução automática, dependências ou envio próprio de dados para serviços externos.

## Conteúdo

### Engenharia e colaboração
- brainstorming, writing-plans, executing-plans, test-driven-development, systematic-debugging e verification-before-completion.
- using-git-worktrees, code-review, finishing-branch e skill-authoring-audit.

### Produto e design
- product-design funciona como roteador para product-design-ideation, product-design-audit e product-design-implementation-qa.

### Cloudflare, GitHub e pesquisa
- Cloudflare: cloudflare-platform, cloudflare-d1, wrangler e workers-best-practices.
- GitHub: github-workflows.
- Pesquisa aprofundada: deep-research.
- using-minhas-skills direciona tarefas para o fluxo mais específico.

## Plugin do ChatGPT

O manifesto portátil [plugin.json](plugin.json) e a pasta skills/ deixam o repositório no formato de um plugin somente de skills. Para preparar o ZIP pelo GitHub e conferir a estrutura, siga [PLUGIN_PACKAGE.md](PLUGIN_PACKAGE.md).

Este pacote não inclui apps conectados nem configuração MCP. A instalação e a disponibilidade do upload de plugins dependem do produto e das permissões da conta ou workspace.

## Privacidade

“Sem telemetria” descreve o conteúdo deste repositório: ele não inclui analytics, beacons, callbacks ocultos, scripts de rastreamento ou coleta própria de uso. Skills de pesquisa podem orientar consultas a fontes públicas quando necessário. O comportamento do agente, do sistema operacional e de serviços externos fica fora do controle do repositório. Leia [PRIVACY.md](PRIVACY.md).

## Licenças e origem

Algumas skills e referências foram incorporadas de projetos de terceiros sob suas licenças originais. Consulte [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), [LICENSE-SUPERPOWERS.txt](LICENSE-SUPERPOWERS.txt) e [LICENSE-CLOUDFLARE.txt](LICENSE-CLOUDFLARE.txt).

## Uso

Cada skill fica em uma pasta própria dentro de skills/ e contém SKILL.md. Copie a pasta desejada para o diretório aceito pelo seu agente. Consulte as instruções e referências antes de usar, especialmente em ações remotas ou com efeitos duradouros.
