
def lista():
    lista = []
    x = int(input('Ingrese un número para añadir a la lista. Escriba un número negativo para terminar: '))
    while x >= 0:
        lista.append(x)
        x = int(input('Ingrese un número para añadir a la lista. Escriba un número negativo para terminar: '))
    print('Lista original:', lista)

    lista_sin_duplicados = eliminar_duplicados(lista)
    print('Lista sin duplicados:', lista_sin_duplicados)

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for numero in lista:
        if numero not in lista_sin_duplicados:
            lista_sin_duplicados.append(numero)
    return lista_sin_duplicados


if __name__ == '__main__':
    lista()