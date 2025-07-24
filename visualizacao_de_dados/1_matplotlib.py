# aula 1 - intro a visualização de dados
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Gráfico de Linha")
plt.show()

categorias = ["A", "B", "C"]
valores = [5, 7, 3]

plt.bar(categorias, valores, color="blue")
plt.title("Gráfico de Barras")
plt.show()

x = [1, 2, 3, 4, 5, 7]
y = [10, 15, 30, 36, 50, 60]

plt.scatter(x, y, color="red")
plt.title("Gráfico de Dispersão")
plt.show()

# aula 2 - fundamentos matplotlib

plt.plot(x, y, label="Linha")
plt.title("Gráfico de Linha com Título")
plt.xlabel("Eixo x")
plt.ylabel("Eixo Y")
plt.legend()
plt.show()

plt.plot(x, y, color="purple", linestyle="--", marker="o")
plt.title("Grafico 2")
plt.grid()
plt.show()
