import numpy as np

quantidades = np.array([5, 3, 6])
precos = np.array([120, 150, 135])

soma_total = np.dot(quantidades, precos)

print(f"Soma total: {soma_total}")