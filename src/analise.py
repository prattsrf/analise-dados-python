import pandas as pd

df = pd.read_csv('data/vendas_limpo.csv')

receita_total = df['faturamento'].sum()
produto_mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()
receita_cidade = df.groupby('cidade')['faturamento'].sum()

# PRINT 
print("=== RELATÓRIO ===")
print(f"Receita total: {receita_total}")
print(f"Produto mais vendido: {produto_mais_vendido}")
print("\nReceita por cidade:")
print(receita_cidade)

# SALVAR EM ARQUIVO 
with open('outputs/relatorio.txt', 'w', encoding='utf-8') as f:
    f.write("=== RELATÓRIO DE VENDAS ===\n\n")
    f.write(f"Receita total: {receita_total}\n")
    f.write(f"Produto mais vendido: {produto_mais_vendido}\n\n")
    f.write("Receita por cidade:\n")
    f.write(receita_cidade.to_string())

print("\nRelatório salvo em outputs/relatorio.txt")