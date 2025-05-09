import numpy as np

#Definimos la matriz inicial
H = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(f"Matriz original: \n{H}")

#Obtenemos las matrices transpuestas
H_T = [H[i].T for i in range(H.shape[0])]
print (f"Plano 1:\n{H_T[0]}")
print (f"Plano 2:\n{H_T[1]}")