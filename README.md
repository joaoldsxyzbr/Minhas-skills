# Minhas Skills

Coleção portável de skills para desenvolvimento, produto, Cloudflare, GitHub e pesquisa aprofundada.

O objetivo é reunir práticas úteis em um pacote revisável, sem mecanismos próprios de telemetria ou rastreamento. As skills são instruções em Markdown. O plugin não inclui scripts de execução automática, dependências ou envio próprio de dados para serviços externos. As ferramentas de manutenção em `tools/` e os testes em `tests/` usam somente a biblioteca padrão do Python, podem ser executados manualmente ou pelo CI do GitHub e ficam fora do ZIP gerado pelo validador.

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

## Diretrizes de tecnologia

As skills **não impõem uma lista fixa de linguagens** nem quantidades ímpares de opções, etapas ou especialistas. A escolha deve considerar maturidade, manutenção ativa, estabilidade, segurança, desempenho, adequação à plataforma e custo de manutenção. Preservar a arquitetura existente é preferível a migrar por preferência pessoal.

Priorize APIs e bibliotecas padrão. Dependências externas novas só devem ser propostas quando necessárias e **oficiais**, publicadas e mantidas por empresas, fundações ou organizações reconhecidas. Verifique origem, licença, manutenção, segurança, privacidade e dependências transitivas; popularidade não equivale a caráter oficial. Quando não existir opção oficial adequada, explique o limite ou proponha solução nativa, sem instalar alternativas comunitárias por conveniência.

## Autonomia nas decisões técnicas

O usuário informa **o resultado desejado**; as skills orientam o agente a investigar o contexto, escolher a solução tecnicamente mais adequada e executar o trabalho autorizado, sem exigir conhecimento de programação nem transferir decisões rotineiras ao usuário. Isso inclui linguagem, arquitetura, APIs oficiais, dependências necessárias, organização do código e testes.

O agente deve preservar o escopo e a arquitetura existente quando apropriado, explicar decisões importantes em linguagem simples e verificar os resultados. **Autonomia técnica não é autorização irrestrita**: pedidos apenas de planejamento continuam sendo planejamento, e alterações destrutivas, gastos, permissões, implantação em produção ou mudanças de escopo importantes exigem autorização correspondente.

## Plugin do ChatGPT

O manifesto portátil [plugin.json](plugin.json) e a pasta skills/ deixam o repositório no formato de um plugin somente de skills. Para preparar o ZIP pelo GitHub e conferir a estrutura, siga [PLUGIN_PACKAGE.md](PLUGIN_PACKAGE.md).

Este pacote não inclui apps conectados nem configuração MCP. A instalação e a disponibilidade do upload de plugins dependem do produto e das permissões da conta ou workspace.

## Privacidade

“Sem telemetria” descreve o conteúdo deste repositório: ele não inclui analytics, beacons, callbacks ocultos, scripts de rastreamento ou coleta própria de uso. Skills de pesquisa podem orientar consultas a fontes públicas quando necessário. O comportamento do agente, do sistema operacional e de serviços externos fica fora do controle do repositório. Leia [PRIVACY.md](PRIVACY.md).

## Licenças e origem

Algumas skills e referências foram incorporadas de projetos de terceiros sob suas licenças originais. Consulte [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), [LICENSE-SUPERPOWERS.txt](LICENSE-SUPERPOWERS.txt) e [LICENSE-CLOUDFLARE.txt](LICENSE-CLOUDFLARE.txt).

## Uso

Cada skill fica em uma pasta própria dentro de skills/ e contém SKILL.md. Copie a pasta desejada para o diretório aceito pelo seu agente. Consulte as instruções e referências antes de usar, especialmente em ações remotas ou com efeitos duradouros.


## Roteamento e carregamento

O roteador escolhe um fluxo principal conforme a intenção e acrescenta somente o apoio técnico necessário. As regras compartilhadas são lidas uma vez; referências detalhadas entram apenas quando necessárias. Invocação direta também aplica essas regras. O host decide quais descrições ficam disponíveis e quais skills carrega; o pacote não promete ativação automática infalível.

As skills e seus arquivos auxiliares ficam neste pacote. Documentação oficial pode fornecer evidências e integrações disponíveis podem executar ações autorizadas, sem encaminhamento para skills de outros plugins.

## Auditoria da versão 0.2.2

A [avaliação reproduzível da 0.2.2](https://github.com/joaoldsxyzbr/Minhas-skills/blob/main/docs/quality-0.2.2.md) distingue **24 cenários preparados**, resultados de exercícios independentes e invocações reais de skills no ChatGPT. Os dois novos casos cobrem autonomia técnica e limites de autorização; não estão aprovados antecipadamente. O avaliador local, `tools/evaluate_routing.py`, aceita observações redigidas e rejeita sucesso sem evidência ou versão incorreta.

O [workflow de qualidade](https://github.com/joaoldsxyzbr/Minhas-skills/blob/main/.github/workflows/quality.yml) valida manifesto, links, testes nativos e ZIP em alterações, execução manual e semanalmente na branch principal. **Ele não acessa conversas pessoais, não faz telemetria e não mede a seleção real de skills pelo ChatGPT**. A rotina semanal do ChatGPT é independente desse CI.

## Verificação e empacotamento

Execute manualmente, sem instalar dependências:

```text
python tools/validate.py
python -m unittest discover -s tests -v
python tools/validate.py --archive ../minhas-skills.zip
```

O validador verifica estrutura, referências e limites do pacote; não mede comportamento do modelo. Consulte [a avaliação da versão 0.2.0](https://github.com/joaoldsxyzbr/Minhas-skills/blob/main/docs/quality-0.2.0.md) para os testes comportamentais e suas limitações.
