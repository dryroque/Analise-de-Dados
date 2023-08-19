import pandas as pd
import plotly.express as px

dados = pd.read_excel("vendas.xlsx")

agrupado = dados.groupby(['loja', 'ano_mes']).preco.sum().to_frame()
agrupado.reset_index(inplace=True)
agrupado['acumulado'] = agrupado.groupby('loja').preco.cumsum()

fig = px.bar(agrupado,
             x='acumulado',
             y='loja',
             color='loja',
             text_auto=True,
             range_x=[0,123000],
             animation_frame='ano_mes')
fig.show()
fig.write_html("grafico_animado.html")