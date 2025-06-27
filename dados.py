import sqlite3
import pandas as pd

def carregar_dados():
    # Caminho completo para o arquivo do banco de dados
    conn = sqlite3.connect('seucaminhoaqui')

    # Extrair dados da tabela Fato_Vendas e dimensões relevantes
    query = """
        SELECT fv."ID_VENDA", fv."Quantidade", fv."Valor_Total", p."Nome_Produto", 
               c."Nome_Cliente", f."Nome_Filial", t."Data_Venda"
        FROM Fato_Vendas fv
        JOIN Dim_Produto p ON fv."ID_PRODUTO" = p."ID_PRODUTO"
        JOIN Dim_Cliente c ON fv."ID_CLIENTE" = c."ID_CLIENTE"
        JOIN Dim_Filial f ON fv."ID_FILIAL" = f."ID_FILIAL"
        JOIN Dim_Tempo t ON fv."ID_TEMPO" = t."ID_TEMPO"
    """
    
    # Ler os dados para um DataFrame
    df = pd.read_sql(query, conn)

    # Fechar a conexão com o banco de dados
    conn.close()
    
    # Verificar todas as filiais distintas
    filiais = df['Nome_Filial'].unique()
    print(f"Filiais disponíveis: {filiais}")
    
    # Retornar o DataFrame
    return df
