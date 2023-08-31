from random import randint
def lista():
  lista=[]
  i=0
  for i in range(15):
    lista.append(randint(0,99))
    i=+1
  print('Lista original:',lista)
  lista.sort()
  print('Lista ordenada de menor a mayor:',lista)





if __name__ =='__main__':
  lista()
