# aula 1 - intro seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("visualizacao_de_dados/produtos.csv")

sns.barplot(x="Categoria", y="Quantidade", data=df)
plt.title("Quantidade Total por Categoria")
plt.show()

sns.scatterplot(x="Preço", y="Quantidade", hue="Categoria", data=df)
plt.show()
