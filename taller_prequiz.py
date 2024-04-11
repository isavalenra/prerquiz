import numpy as np

matriz = np.random.randint(11, size=(20,30,20,100))

print(f'Matriz: ',matriz)
print(f'dimension de la matriz: ',matriz.ndim)
print(f'tamaño de la matriz:',matriz.size)

b = matriz.copy()

c = b[:,:,:,1]
print(f'diemsnion:',np.ndim(c)) 
print(f'')