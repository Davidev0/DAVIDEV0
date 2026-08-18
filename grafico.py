import matplotlib.pyplot as plt
#DADOS DO EXEMPLO
meses=[
    "Jan",
    "Fev",
    "Mar",
    "Abr",
    "Mai",
    "Jun"

]

vendas = [120, 150, 180, 200, 230, 260]
#Criando grafico de linha
plt.plot(meses, vendas, marker='o', color='#1E5A8A', linewidth=3)
plt.title('Evolução das Vendas', fontsize=14, color='#1E5A8A', weight='bold')
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()