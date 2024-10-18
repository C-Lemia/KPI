import dados  # Importa o arquivo dados.py
import pandas as pd

# Carregar os dados do banco de dados
df = dados.carregar_dados()

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Converter a coluna 'Data_Venda' para o tipo datetime
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])

# Vendas Totais (soma de todas as vendas)
vendas_totais = df['Valor_Total'].sum()
print("Vendas Totais:", vendas_totais)

# Calcular as vendas totais por mês
vendas_totais_por_mes = df.groupby(df['Data_Venda'].dt.to_period('M'))['Valor_Total'].sum()
print("\nVendas Totais por Mês:")
print(vendas_totais_por_mes)

# Vendas por Região (Filial)
vendas_por_filial = df.groupby('Nome_Filial')['Valor_Total'].sum()
print("\nVendas por Região (Filial):")
print(vendas_por_filial)

# Quantidade Vendida por Produto
quantidade_por_produto = df.groupby('Nome_Produto')['Quantidade'].sum()
print("\nQuantidade Vendida por Produto:")
print(quantidade_por_produto)

# Número Total de Vendas (Transações)
numero_total_vendas = df['ID_VENDA'].nunique()
print("\nNúmero Total de Vendas (Transações):", numero_total_vendas)

# Vendas por cliente
vendas_por_cliente = df.groupby('Nome_Cliente')['Valor_Total'].sum()
print("\nVendas por Cliente:")
print(vendas_por_cliente)

# Número de Vendas por Cliente
numero_vendas_por_cliente = df.groupby('Nome_Cliente')['ID_VENDA'].nunique()
print("\nNúmero de Vendas por Cliente:")
print(numero_vendas_por_cliente)

# Valor vendas por produto
vendas_por_produto_valor = df.groupby('Nome_Produto')['Valor_Total'].sum()
print("\nVendas por Produto (Em Valor):")
print(vendas_por_produto_valor)

# Número de Produtos Vendidos por Filial
quantidade_por_filial = df.groupby('Nome_Filial')['Quantidade'].sum()
print("\nQuantidade de Produtos Vendidos por Filial:")
print(quantidade_por_filial)

# Crescimento das vendas
vendas_totais_por_mes_shift = vendas_totais_por_mes.shift(1)
crescimento_vendas = (vendas_totais_por_mes - vendas_totais_por_mes_shift) / vendas_totais_por_mes_shift * 100
print("\nCrescimento das Vendas (em % por mês):")
print(crescimento_vendas)

# Percentual de Contribuição de Cada Filial nas Vendas Totais
contribuicao_por_filial = (df.groupby('Nome_Filial')['Valor_Total'].sum() / vendas_totais) * 100
print("\nPercentual de Contribuição de Cada Filial nas Vendas Totais:")
print(contribuicao_por_filial)
