# Pacote do plugin Minhas Skills

Este repositório usa o formato portátil Agent Plugins 1.0 para um plugin somente de skills do ChatGPT.

## Estrutura do pacote

O arquivo plugin.json fica na raiz e declara a identidade do plugin. As skills ficam diretamente em skills/<nome-da-skill>/SKILL.md. Cada pasta de skill corresponde ao valor name do frontmatter YAML.

O pacote tem 21 skills. Não inclui mcp.json, .app.json, apps conectados, credenciais, scripts ou hooks. O pacote não precisa desses componentes para oferecer instruções reutilizáveis.

## Gerar o ZIP pelo GitHub

1. Abra o repositório Minhas-skills no GitHub.
2. Escolha Code > Download ZIP.
3. Envie o ZIP pela opção Upload plugin no ChatGPT, se ela estiver disponível para sua conta ou workspace.

O ZIP de código do GitHub coloca o repositório dentro de uma única pasta superior. Esse formato é aceito: o arquivo do plugin fica na raiz dessa pasta e não há outros projetos ao lado.

A opção de upload de plugins e as permissões para usá-la dependem do produto e das configurações do workspace. Se ela não aparecer, o pacote continua disponível para uso com um fluxo de instalação de plugins compatível.

## Verificações antes de atualizar o pacote

- plugin.json válido em UTF-8 e com o schema portátil Agent Plugins 1.0.
- Cada skill em uma pasta imediatamente dentro de skills/.
- Cada SKILL.md com frontmatter YAML, name e description.
- O name do frontmatter igual ao nome da pasta, sem duplicatas.
- Recursos referenciados por uma skill mantidos dentro do pacote.
- Sem arquivos de credenciais, integrações não solicitadas ou artefatos alheios ao plugin.

O GitHub armazena as fontes do pacote. A criação ou instalação do plugin no ChatGPT é uma etapa separada.
