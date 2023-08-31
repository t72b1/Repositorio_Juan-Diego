def Matrices(filas,columnas):
    matriz=[] #Se crea la matriz vacia
    for i in range(filas): #I recorre desde 0 hasta el numero de filas
        matriz.append([]) #append agrega un numero 
        for j in range(columnas):
            num=int(input(f'ingrese el numero en la posicion [{i},{j}]:'))
            matriz[i].append(num)
    for i in matriz:
        print(i)


if __name__=='__main__':
    filas=int(input('ingrese el numero de filas:'))
    columnas=int(input('Ingrese el numero de columnas:'))
    Matrices(filas,columnas)