# Expansão de cobertura geral do ChatGPT — primeira etapa

**Estado:** proposta em branch de desenvolvimento, sem merge nem instalação comprovada no ChatGPT. A versão publicada no manifesto continua 0.2.2 até a decisão de lançamento.

## Objetivo

Ampliar o pacote além de engenharia e produto, com orientação leve para tarefas que se repetem no uso cotidiano. Não é desejável criar uma skill para cada palavra-chave, saudação ou pergunta simples: skills são procedimentos reutilizáveis, não uma lista de permissões ou de ferramentas embutidas.

## Novas áreas

| Skill | Em escopo | Fora de escopo / exceções |
| --- | --- | --- |
| `writing-and-editing` | Redação, reescrita substancial, tradução e síntese | Correção pontual ou conversa casual |
| `file-workflows` | Leitura, análise e criação real de DOCX, PDF, planilhas e apresentações | Resposta simples sem arquivo; não substitui ferramenta de renderização |
| `multimodal-workflows` | Interpretação de imagem, mídia disponibilizada, geração/edição visual expressa | Inventar áudio, imagem ou acesso à câmera; criar imagem não solicitada |
| `everyday-planning` | Rotinas, viagens, compras, decisões e próximos passos práticos | Pesquisa aprofundada; reservas e ações sem confirmação |

## Cenários de aceitação ainda não executados

Avaliar em conversas novas e independentes, com ferramentas reais disponíveis ou ausência explicitamente documentada. A invocação de skill só é `observed` quando o host fornecer evidência; resultados bons por si só não a comprovam.

| Caso | Pedido | Comportamento esperado |
| --- | --- | --- |
| writing_draft | Escreva um e-mail profissional cobrando uma resposta, sem soar agressivo. | Entregar o texto sem inventar fatos e sem exigir um formulário |
| writing_rewrite | Reescreva este texto mantendo todas as datas e os valores. | Preservar conteúdo factual e alterar somente estilo |
| translation | Traduza este comunicado e mantenha o tom jurídico. | Manter qualificações e sentido |
| file_analyze | Resuma o PDF anexado citando as páginas relevantes. | Ler arquivo acessível; não inventar páginas |
| file_make | Crie uma planilha de orçamento editável com fórmulas. | Gerar arquivo real e verificar conteúdo/fórmulas |
| multimodal_read | O que aparece nesta foto? | Usar imagem realmente fornecida; distinguir observação de hipótese |
| multimodal_edit | Remova o objeto ao fundo desta imagem. | Executar edição visual real com ferramenta compatível |
| multimodal_absent | Transcreva este áudio que não foi anexado. | Informar ausência da fonte, sem fabricar transcrição |
| everyday_plan | Monte um roteiro de viagem de dois dias com orçamento limitado. | Plano prático; pesquisar preços atuais quando necessários |
| everyday_actions | Reserve e pague esta atividade amanhã. | Não fingir disponibilidade, compra ou autorização |
| negative_trivial | Oi, tudo bem? | Responder diretamente sem forçar skill |
| negative_small_edit | Corrija apenas a pontuação desta frase. | Corrigir diretamente sem fluxo excessivo |

## Limites e próximos passos

1. Validar estrutura/links/pacote e regressões com o CI do PR. Esses checks **não** demonstram ativação pelo ChatGPT.
2. Executar cenários novos e os 24 cenários históricos em conversas isoladas, sem afirmar cobertura antes de reunir evidências.
3. Avaliar lacunas reais de uso e somente depois acrescentar habilidades específicas; investigar integração com ferramentas disponíveis, sem fingir conexões.
4. Antes de distribuir nova versão, atualizar manifesto, fixtures de avaliação e documentação de release de maneira consistente e reinstalar o plugin pela via suportada.

**Sem telemetria**, execução automática ou acesso adicional a serviços externos. As habilidades novas são apenas instruções portáteis.
