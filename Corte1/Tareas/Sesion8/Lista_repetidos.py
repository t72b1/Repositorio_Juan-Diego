def lista():
  lista=[]
  x=int(input('Ingrese un numero para añadir a la lista escriba un numero negativo para terminar'))
  while x>-1:
    lista.append(x)
    x=int(input('Ingrese un numero para añadir a la lista escriba un numero negativo para terminar'))
  print('Lista original:',lista)






if __name__ =='__main__':
  lista()
