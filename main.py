#importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt 

for i in range(15):

    print(f"\n Experimento {i+1}")

    #inserir os dados de entrada
    x = np.array(list(map(float, input("Digite os dados de entrada do x(separados por espaço): ").split())))
    y = np.array(list(map(float, input("Digite os dados de entrada do y(separados por espaço): ").split())))

    #regressão linear
    z = np.polyfit(x, y, 1)
    a,b = z

    p = np.poly1d(z)

    #grafico
    plt.scatter(x, y)
    plt.plot(x, p(x), "r--")
    
    #equacao da reta
    equacao = f"y = {a:.2f}x + {b:.2f}"
    
    #configuraçao do grafico
    plt.text(min(x), max(y), equacao, bbox=dict(facecolor='white', alpha=0.5))
    plt.title(f"Experimento {i+1}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    #salvar imagem
    plt.savefig(f"Grafico_{i+1}.png")
    
    plt.clf() # Limpa a figura para o próximo experimento
