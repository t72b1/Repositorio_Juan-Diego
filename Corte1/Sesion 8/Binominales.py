import formula_binominales as f
def main():
    n=int(input('Ingrese el numero de elementos en el conjunto'))
    m=int(input('Ingrese el numero de muestras'))
    if n<m:
        print('El numero de elementos tiene que ser mayor que el numero de muestras')
    else:
        C=f.operacion(n,m)
        print(f'Las combinaciones binominales que se pueden dar con {n} elementos organizados en {m} muestras es {C}')






if __name__=='__main__':
    main()