from random import randint


def generador(num,lista=[]):
  if num>0:
    lista.append(randint(0,99))
    return generador(num-1,lista)
  else:
    print('Lista original:',lista)
    a=max(lista)
    print('El mayor numero de la lista es:',a)





if __name__ =='__main__':
  x=int(input('Ingrese que el tamaño de la lista'))
  generador(x)