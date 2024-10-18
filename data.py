import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dados  # Importa o arquivo dados.py

# Carregar os dados do banco de dados
df = dados.carregar_dados()

# Converter a coluna 'Data_Venda' para o tipo datetime
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])

# Cálculos dos KPIs
vendas_totais = df['Valor_Total'].sum()
vendas_totais_por_mes = df.groupby(df['Data_Venda'].dt.to_period('M'))['Valor_Total'].sum()
vendas_por_filial = df.groupby('Nome_Filial')['Valor_Total'].sum()
quantidade_por_produto = df.groupby('Nome_Produto')['Quantidade'].sum()
numero_total_vendas = df['ID_VENDA'].nunique()
vendas_por_cliente = df.groupby('Nome_Cliente')['Valor_Total'].sum()
numero_vendas_por_cliente = df.groupby('Nome_Cliente')['ID_VENDA'].nunique()
vendas_por_produto_valor = df.groupby('Nome_Produto')['Valor_Total'].sum()
quantidade_por_filial = df.groupby('Nome_Filial')['Quantidade'].sum()
vendas_totais_por_mes_shift = vendas_totais_por_mes.shift(1)
crescimento_vendas = (vendas_totais_por_mes - vendas_totais_por_mes_shift) / vendas_totais_por_mes_shift * 100
contribuicao_por_filial = (vendas_por_filial / vendas_totais) * 100

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do Dash
app.layout = html.Div([
    html.H1("KPIs de Vendas"),

    html.Div([
        html.H3(f"Vendas Totais: R$ {vendas_totais:,.2f}"),
        html.H3(f"Número Total de Vendas: {numero_total_vendas}"),
    ]),

    html.Div([
        html.H3("Vendas Totais por Mês:"),
        dcc.Graph(
            figure={
                'data': [
                    go.Bar(
                        x=vendas_totais_por_mes.index.astype(str),
                        y=vendas_totais_por_mes,
                        name='Vendas Totais por Mês'
                    )
                ],
                'layout': go.Layout(title='Vendas Totais por Mês', xaxis={'title': 'Mês'}, yaxis={'title': 'Valor Total'})
            }
        )
    ]),

    html.Div([
        html.H3("Vendas por Filial:"),
        dcc.Graph(
            figure={
                'data': [
                    go.Pie(
                        labels=vendas_por_filial.index,
                        values=vendas_por_filial,
                        name='Vendas por Filial'
                    )
                ],
                'layout': go.Layout(title='Vendas por Filial')
            }
        )
    ]),

    html.Div([
        html.H3("Crescimento das Vendas (em % por mês):"),
        dcc.Graph(
            figure={
                'data': [
                    go.Scatter(
                        x=crescimento_vendas.index.astype(str),
                        y=crescimento_vendas,
                        mode='lines+markers',
                        name='Crescimento das Vendas'
                    )
                ],
                'layout': go.Layout(title='Crescimento das Vendas (%)', xaxis={'title': 'Mês'}, yaxis={'title': 'Crescimento (%)'})
            }
        )
    ]),

    html.Div([
        html.H3("Quantidade Vendida por Produto:"),
        dcc.Graph(
            figure={
                'data': [
                    go.Bar(
                        x=quantidade_por_produto.index,
                        y=quantidade_por_produto,
                        name='Quantidade Vendida por Produto'
                    )
                ],
                'layout': go.Layout(title='Quantidade Vendida por Produto', xaxis={'title': 'Produto'}, yaxis={'title': 'Quantidade'})
            }
        )
    ]),

    html.Div([
        html.H3("Percentual de Contribuição de Cada Filial nas Vendas Totais:"),
        dcc.Graph(
            figure={
                'data': [
                    go.Pie(
                        labels=contribuicao_por_filial.index,
                        values=contribuicao_por_filial,
                        name='Contribuição por Filial'
                    )
                ],
                'layout': go.Layout(title='Contribuição de Cada Filial nas Vendas Totais')
            }
        )
    ])
])

# Executar o app
if __name__ == '__main__':
    app.run_server(debug=True)
