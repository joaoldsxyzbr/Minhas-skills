# Privacidade e ausência de telemetria

Este repositório fornece instruções em Markdown. Na versão atual, ele não contém aplicação, serviço remoto, analytics, pixels, beacons, rastreamento, atualização automática ou coleta própria de uso.

## O que as skills fazem

- Leem os arquivos de projeto necessários à tarefa.
- Podem orientar consultas a documentação e fontes públicas quando a tarefa exigir informação atual.
- Podem usar ferramentas disponíveis no ambiente do agente, mas não incluem credenciais nem iniciam chamadas de rede por conta própria.
- Não enviam conversas, arquivos ou métricas para os mantenedores deste repositório.

## O que não é controlado aqui

O aplicativo de IA, o sistema operacional, extensões, plugins, ferramentas de pesquisa e serviços acessados podem ter seus próprios registros, políticas e fluxos de dados. As instruções deste repositório não conseguem inspecionar nem alterar esses componentes.

## Auditoria

Antes de aceitar uma atualização, revise o diff. Skills novas devem ser texto por padrão. Scripts, hooks, binários, workflows com acesso a dados externos e dependências precisam de justificativa explícita e revisão separada. Não aceite telemetria ou rastreamento ocultos.
