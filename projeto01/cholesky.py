import numpy as np
import math

def transposta(n, mat):
    return [[mat[j][i] for j in range(n)] for i in range(n)]
        
def simetrica(n, mat):
    for i in range(n):
        for j in range(i, n):
            if mat[i][j] != mat[j][i]:
                return False
            
    return True

def definida_positiva(mat):
    autovalores = np.linalg.eigvals(mat)

    return np.all(autovalores > 0)

def cholesky(n, mat):
    G = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                soma_diag = sum(G[i][k] ** 2 for k in range(j))
                valor = mat[i][i] - soma_diag
                if valor <= 0:
                    raise ValueError("matriz não definida positiva")
                G[i][j] = math.sqrt(valor)

            else:
                soma_n_diag = sum(G[i][k] * G[j][k] for k in range(j))
                if G[j][j] == 0:
                    raise ZeroDivisionError("divisão por zero em G[j][j]")
                G[i][j] = (mat[i][j] - soma_n_diag) / G[j][j]

    return G
    
mat1 = [
    [4, 6],
    [6, 13]
]

mat2 = [
    [4, 6],
    [4, 13]
]

# mat2_t = transposta(2, mat2)
# for linha in mat2_t:
#     print(linha)
# print(simetrica(2, mat1))
# print(simetrica(2, mat2))
# print(definida_positiva(mat1))

if simetrica(2, mat1):
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")

if definida_positiva(2, mat1):
    print("A matriz é definida positiva.")
else:
    print("A matriz não é definida positiva.")

G = cholesky(2, mat1)
for linha in G:
    print(linha)

