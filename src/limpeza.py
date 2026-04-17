import pandas as pd

df = pd.read_csv('data/vendas.csv')

# Remover valores nulos
df = df.dropna()

# Criar coluna de faturamento
df['faturamento'] = df['quantidade'] * df['preco_unitario']

# Remover duplicados
df = df.drop_duplicates()

# Converter data
df['data'] = pd.to_datetime(df['data'])

# Salvar
df.to_csv('data/vendas_limpo.csv', index=False)

print("Dados tratados com sucesso!")