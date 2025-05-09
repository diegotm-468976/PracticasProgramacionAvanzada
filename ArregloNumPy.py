import numpy as np

#Generamos un arreglo de tamaño 5x4x3 con valores aleatorios entre 0 y 100
arr = np.random.randint(0, 101, size=(5, 4, 3))

#Encontramos el elemento más pequeño en la matriz
min_val = arr.min()

#Encontramos el elemento más grande en la matriz
max_val = arr.max()

#Encontramos la ubicación del elemento más pequeño
minloc = np.where(arr == min_val)

#Encontramos la ubicación del elemento más grande
maxloc = np.where(arr == max_val)

# Print results
print(f"Matriz: \n{arr}")
print(f"El valor más pequeño es: {min_val}")
print(f"El valor más pequeño se encontró {len(minloc[0])} vez/veces")
for i in range(len(minloc[0])):
    print(f"Ubicación {i+1}: ({minloc[0][i]}, {minloc[1][i]}, {minloc[2][i]})")
print(f"El valor más grande es: {max_val}")
print(f"El valor más grande se encontró {len(maxloc[0])} vez/veces")
for i in range(len(maxloc[0])):
    print(f"Ubicación {i+1}: ({maxloc[0][i]}, {maxloc[1][i]}, {maxloc[2][i]})")