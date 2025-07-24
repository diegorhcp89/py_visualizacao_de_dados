#aula 1 - intro ao plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("visualizacao_de_dados/pessoas.csv")

fig = px.bar(df, x="Cargo", y="Salário", color="Departamento", title="Salário Médio por cargo")
fig.show()

fig = px.scatter(df, x="Salário", y="Localização", color="Cargo", size="Salário", title="Dispersão Salarios por Localização")
fig.show()

fig = px.pie(df, names="Departamento", values="Salário", title="Distribuição de Salário por departamento")
fig.show()
