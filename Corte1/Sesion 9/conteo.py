def conteo(num):
    if num>0:
        num=-1
        conteo(num)
    print(num)
    




if __name__=='__main__':
    n=int(input('Ingrese el numero hasta que desea contar'))
    conteo(n)