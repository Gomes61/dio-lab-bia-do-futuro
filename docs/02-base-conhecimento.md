# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Qual a funcionalidade do MAR? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores ou seja dar continuidade ao atendimento eficientemente |
| `perfil_investidor.json` | JSON | Personalizar as explicaçações sobre as dúvidas e necessidade de aprendizado do usuário |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles posssam ser ensinados ao cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essaas informações de forma didática |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não, todos os produtos foram mantidos, pois foram vistos como importantes para ensino e busca das pessoas. 

---

## Estratégia de Integração

### Como os dados são carregados?
> ```python
> import pandas as pd
> import json
>
> #CSVs
> historico = pd.read_csv('data/historico_atendimento.csv')
> transcacoes = pd.read_csv('data/transacoes.csv')
>
> #JSONs
> with open('data/perfil_investidor.json", 'r', encoding='utf-8' as f:
>      perfil = json.load(f)
>
> with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
>      produtos = json.load(f)
> ```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
