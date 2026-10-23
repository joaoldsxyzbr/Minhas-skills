# Minhas Skills

Coleção portável de skills para fluxos de desenvolvimento, produto, Cloudflare, GitHub e pesquisa aprofundada.

O objetivo é reunir práticas úteis em um pacote revisável e sem mecanismos próprios de telemetria ou rastreamento. As skills são arquivos de instruções; este repositório não instala dependências, não executa código automaticamente e não envia dados para serviços externos.

## Estrutura

- `skills/`: skills próprias, escritas para o formato portável Agent Skills.
- `vendor/superpowers/`: skills selecionadas do projeto Superpowers, preservadas com a licença e a atribuição upstream.
- `vendor/cloudflare/`: skills oficiais selecionadas da Cloudflare, preservadas com a licença e a atribuição upstream.
- `THIRD_PARTY_NOTICES.md`: origem, licenças e escopo do material incorporado.
- `PRIVACY.md`: limites verificáveis da promessa de privacidade.

## Conteúdo planejado

- Fluxos de engenharia: descoberta, planejamento, execução, TDD, depuração sistemática, revisão e verificação.
- Produto e design: pesquisa UX, exploração de alternativas, auditoria e validação visual em instruções próprias.
- Cloudflare: skills oficiais selecionadas para plataforma, Workers e Wrangler.
- GitHub: fluxo original para repositórios, branches, commits e pull requests.
- Pesquisa aprofundada: perguntas, fontes primárias, verificação cruzada e síntese citada.

## Limites da privacidade

“Sem telemetria” significa que este repositório não adiciona analytics, beacons, callbacks ocultos, scripts de rastreamento nem coleta própria de uso. Skills que realizam pesquisa podem orientar o agente a consultar fontes públicas quando isso for necessário para a tarefa. O comportamento do aplicativo de IA, do sistema operacional e de serviços externos fica fora do controle deste repositório; veja [PRIVACY.md](PRIVACY.md).

## Uso

Cada skill fica em uma pasta própria e contém um `SKILL.md`. Copie a pasta desejada para o diretório de skills aceito pelo seu agente. As instruções principais evitam depender de uma plataforma específica; recursos ou comandos específicos são declarados na própria skill.

Consulte [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) antes de redistribuir material de terceiros.
