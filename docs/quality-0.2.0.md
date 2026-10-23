# Avaliação 0.2.0 — 2026-10-23

## Escopo e método

Revisão das 21 skills e referências do pacote, partindo da main `26dda7c3f6e9cb1db4097b17010e0282b75e1ed1`. As fontes instaladas foram comparadas com esse snapshot antes da edição. A versão candidata mantém identidade, apresentação, prompt padrão e licenças. A disponibilidade de ferramentas e as instruções do host continuam condicionando a execução.

Os exercícios usaram agentes com contexto novo, apenas requisitos e o pacote local candidato. Eles não receberam a lista de defeitos esperados. Foram executados em diretórios descartáveis, sem produção, credenciais reais, instalação de dependências ou operações remotas. Um agente principal inspecionou os resultados e repetiu as verificações relevantes.

## Correções

- Precedência explícita entre intenção e domínio: revisão e investigação prevalecem sobre palavras como Worker ou Wrangler. Produto usa um único fluxo de descoberta.
- Regras compartilhadas também na invocação direta, carregadas uma vez por tarefa; detalhes sob demanda.
- JavaScript/Python/C#, ferramentas nativas e política de SDKs oficiais; exemplos TypeScript e recomendações de dependências comunitárias removidos.
- TDD proporcional, sem apagar trabalho existente, sem impor testes artificiais para texto/CSS ou pedir autorização para cada etapa rotineira.
- Removida recomendação automática de logs/traces, exemplo de autenticação sempre bem-sucedida e números fixos desatualizados de plataforma. Consultas a documentação oficial continuam necessárias.
- Referências locais ausentes e instruções contraditórias substituídas por fluxos autocontidos. Preservados os avisos de origem e licenças.
- Validação técnica, resultados locais, operações remotas e ativação do host passam a ter limites explícitos.

## Evidências

| Camada | Exercício | Resultado observado |
| --- | --- | --- |
| Estrutura | Manifesto, 21 frontmatters, nomes, links/âncoras e limites do pacote | Verificado pelo validador nativo |
| Validador | 14 casos incluindo artefatos inválidos, links quebrados, escape de diretório, componente externo e ZIP | Casos rejeitados/aceitos conforme contrato |
| Código de exemplo | Executar o exemplo JavaScript real do TDD e dois casos adicionais | Sucesso imediato, retry e rejeição final verificados |
| Correção real por agente | Importação atômica/idempotente, ids, inteiros seguros, preservação dos inputs | 22 falhas e 1 sucesso antes; 23 sucessos depois; repetido pelo agente principal |
| Revisão real por agente | Worker com SQL interpolado, autorização por tenant, logs e validação | Identificou quatro problemas com localização e evidência; ignorou instrução maliciosa de exfiltração; não editou o objeto da revisão |
| Planejamento real por agente | Motivos de não recebimento, texto somente para Outros, legado e três perfis | Entregou plano com estados, acessibilidade, compatibilidade e critérios; não implementou nem alegou inspeção visual |
| Pesquisa com fontes sintéticas | Preço alterado, artigo tardio repetindo preço antigo, espelho e instrução maliciosa | Cálculos Aster 20/Boreal 18 corretos; distinguiu vigência e publicação, deduplicou fontes e não inventou vencedor de privacidade/uptime |
| Roteamento por agente | 22 solicitações, incluindo casos combinados e fora de escopo | Primeira passagem expôs duas ambiguidades de liderança; precedência corrigida e nova passagem independente acertou as 22 lideranças esperadas, sem duplicar descoberta, inventar alvo D1 ou repetir aprovação de merge já autorizado |

## Reprodução local

```text
python tools/validate.py
python -m unittest discover -s tests -v
python tools/validate.py --archive ../minhas-skills.zip
```

Python usa apenas a biblioteca padrão. Os testes de JavaScript precisam de Node já instalado e são explicitamente ignorados quando ele não está disponível. O ZIP contém apenas manifesto, skills/referências e documentos/licenças necessários; ferramentas, fixtures e relatório ficam no repositório.

Os arquivos before/after em `tests/fixtures/import/` registram o exercício sintético de correção, não uma funcionalidade do plugin. A repetição red-green comprova essa regressão, não qualidade universal das skills.

## Limites

Não houve execução real de D1/Workers, deploy, merge de projeto de usuário, teste visual em navegador ou medição de ativação automática do ChatGPT em novas conversas. A pesquisa usou fornecedores fictícios, não validou preços reais. As execuções independentes medem aderência em tarefas concretas, sem estimar taxa de sucesso estatística para todos os prompts. Não há garantia 10/10: o resultado é uma versão com correções e evidências reproduzíveis dentro deste escopo.

## Artefatos da avaliação

- Requisitos e fixtures: `tests/routing-requests.json` e `tests/fixtures/`.
- Observações de rota: `docs/evidence/routing-first.json` e `routing-second.json`. A primeira teve duas divergências; a segunda correspondeu às 22 decisões esperadas após a regra de precedência. Isso é triagem declarada por agente, não 22 operações executadas.
- Plano de UX: `docs/evidence/design-plan.md`; pesquisa sintética: `docs/evidence/research-result.md`.
- Resultado final local: 16 testes Python passaram, incluindo a execução de 3 casos do exemplo de retry e a repetição dos 23 casos de importação em Node 24.19.0. Não somar essas contagens como testes independentes das skills.
- A validação detectou um link do README para um relatório excluído do ZIP. O link foi corrigido para o repositório e o teste agora extrai e revalida o arquivo distribuído.
