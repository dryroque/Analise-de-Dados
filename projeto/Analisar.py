import pandas as pd
import plotly.express as px
import pyautogui
import pyperclip

dados = pd.read_excel("vendas.xlsx")

#ANALISE EXPLORATORIA
#listar primeiras linhas
dados.head()
print(dados.head())

#listar as ultimas linhas
dados.tail()

#tamanho da tabela de dados
dados.shape

#tipos de dados
dados.dtypes

#ESTATISTICAS
#gerando estatisticas
dados.describe()

#ANALISES
#total de vendas por loja
dados.loja.value_counts()

#total de pedidos por tamanho
dados.tamanho.value_counts()

#total de vendas por forma de pagamento
dados.forma_pagamento.value_counts()

#AGRUPAMENTO DE DADOS
#faturamento por loja
fl = dados.groupby("loja").preco.sum()
print(fl)

#faturamento medio por loja
dados.groupby("loja").preco.mean()

#faturamento por estado
dados.groupby("estado").preco.sum()

#faturamento medio por estado
dados.groupby("estado").preco.mean()

#faturamento por estadoe cidade
#criando um arquivo excel
dados.groupby(["estado", "cidade"]).preco.sum().to_excel("Faturamento-estado-cidade.xlsx")
dados.groupby(["estado", "cidade"]).preco.sum().to_frame()

#faturamento medio por cidade e estado
dados.groupby(["estado", "cidade"]).preco.mean().to_frame()

#VISUALIZACAO DE ESTADO
#criando graficos
gl = px.histogram(dados, x="loja", y="preco", text_auto=True, color="estado")
print(gl)

#criando graficos
grafico = px.histogram(dados, x="loja", y="preco", text_auto=True, color="forma_pagamento")
grafico.show()
grafico.write_html("Grafico-forma-pagamento.html")

grafico = px.histogram(dados, x="estado", y="preco", text_auto=True, color="forma_pagamento")
grafico.show()

#LISTAS (ESTRUTURA DE DADOS)
#estrutura de repeticao
lista_colunas = ["loja", "cidade", "estado", "regiao", "tamanho", "local_consumo"]
for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna, y="preco", text_auto=True, color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"Grafico-{coluna}.html")


