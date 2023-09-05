def buscador(a, b, i=0, posiciones=None):
    if posiciones is None:
        posiciones = []
    
    index = a.find(b, i)
    
    if index == -1:
        return posiciones
    
    posiciones.append(index)
    
    return buscador(a, b, index + 1, posiciones)

if __name__ == '__main__':
    a = input('Ingrese su texto: ')
    b = input('Ingrese la letra o substring que quiere encontrar en el texto: ')
    
    posiciones = buscador(a, b)
    
    if not posiciones:
        print('Esa letra o substring no está en el texto.')
    else:
        print(f'{b} se encuentra en las posiciones: {posiciones}')