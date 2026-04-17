# Análise de Dados de Vendas

Esse projeto foi desenvolvido como prática de análise de dados utilizando Python. A ideia foi simular um cenário simples de vendas, passando pelas etapas de tratamento dos dados e geração de algumas métricas básicas.

## O que foi feito

Comecei com um conjunto de dados em CSV contendo informações de pedidos, como produto, cidade, quantidade e preço. A partir disso:

- Fiz a limpeza dos dados (remoção de valores nulos e duplicados)
- Criei uma coluna de faturamento com base na quantidade e preço
- Trabalhei com datas para possibilitar análises ao longo do tempo
- Gereis métricas como receita total e produto mais vendido
- Organizei os resultados em um relatório automático

## Tecnologias utilizadas

- Python
- Pandas

## Como executar

1. Instalar as dependências:
pip install pandas

2. Rodar o tratamento dos dados:
python src/limpeza.py

3. Gerar análise:
python src/analise.py

## Observações

Esse projeto foi importante pra entender melhor como funciona o fluxo de análise de dados na prática, desde a preparação até a extração de insights. Pretendo evoluir ele futuramente com visualizações e dashboards.