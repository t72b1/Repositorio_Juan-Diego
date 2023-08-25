
def agregar(milista):
    num=int(input('Que desea agregar'))
    milista.append(num)
    print(milista)
    return

def main(opc):
    print('Seleccione una opcion:\n',\
          '1. Append')

    opc=input('Selecccion:')

    if opc=='1':
        agregar(milista)




if __name__=='__name__':
     milista=[2,3,4]
     main(opc,milista)