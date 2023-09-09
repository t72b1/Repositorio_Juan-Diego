productos={}


def Organizador():
      f=open('Alimentos.txt','rt')
      lines=f.readlines()
      f.close()
      for i in lines:
            a=i.rstrip('\n').split(',')
            if len(a) >= 3:
                  alimento= a[1]
                  iva = float(a[2])
                  productos[alimento]=iva
      
      
def lista():
      f=open('Alimentos.txt','rt')
      lines=f.readlines()
      f.close()
      for i in lines:
            a=i.rstrip('\n').split(',')
            if len(a) >= 3:
                  print(a[1])
                  



def calculadora(busqueda,valor_neto):
      porcentaje=productos[busqueda]
      
      sin_iva=valor_neto/(1+porcentaje)
      iva_añade=valor_neto-sin_iva
      print(f'El valor original del producto es  {sin_iva} y el IVA añade {iva_añade}')
      
      
def menu():
    while 1:
        busqueda = input('Ingrese el alimento del cual quiere conocer el valor o ingrese "lista" para ver la lista de productos\n(Escriba "salir" para salir): ')
        if busqueda.lower() == 'salir':
            break
        elif busqueda == 'lista':
            lista()
            print('Tenga en cuenta minusculas y mayusculas')
        elif busqueda != 'lista' and busqueda not in productos:
            print('Ingrese un producto válido')
        else:
            valor_neto = float(input('Ingrese el valor neto del producto: '))
            calculadora(busqueda, valor_neto)


if __name__=="__main__":
      Organizador()
      menu()