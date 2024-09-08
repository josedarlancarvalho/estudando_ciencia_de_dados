import numpy as np

dados = np.array([21.4, 20.6, 22.5, 25.6, 24.6, 23.8])

maior = np.max(dados)
menor = np.min(dados)

print(f"Maior preço {maior}")
print(f"Menor preço {menor}")

variacao_preco = maior - menor

print(f"A variação foi de: {variacao_preco}")