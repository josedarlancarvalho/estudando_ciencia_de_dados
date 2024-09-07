import numpy as np
import time

lista = list(range(1, 10_000_001))
array = np.array(range(1, 10_000_001))

inicio = time.time()
soma_lista = sum(lista)
fim = time.time()
print(f"Tempo para somar todos os items da lista: {fim - inicio} segundos")
#saida = 0.3912782669067383 segundos


inicio = time.time()
soma_array = np.sum(array)
fim = time.time()
print(f"Tempo para somar todos os itens do array: {fim - inicio} segundos ")
#saida = 0.010294437408447266 segundos