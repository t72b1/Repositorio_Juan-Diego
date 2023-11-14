class Articulos:
    def __init__(self,nombre:str, precio:int):
        self.__nombre=nombre
        self.__precio=precio
        
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def getNombre(self):
        return self. __nombre
    
    def setPrecio(self,precio:int):
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    
    
    
    
class IVA0(Articulos):
    def __init__(self, nombre: str, precio: int,iva:float):
         super().__init__(nombre, precio)
         self.iva=iva
    
    def setIVA(self,iva:float):
        self.iva=iva
    def getIVA(self):
        return self.iva
    def bruto(self):
     print(f'Este producto no tiene IVA por lo tanto su precio es {self.getPrecio()}')
    
    
         
        
         
class IVA5(Articulos):
    def __init__(self, nombre: str, precio: int,iva:float):
         super().__init__(nombre, precio)
         self.iva=iva
    
    def setIVA(self,iva:float):
        self.iva=iva
    def getIVA(self):
        return self.iva
    
    def bruto(self):
        porcentaje=self.getIVA()
        sin_iva=self.getPrecio()/(1+porcentaje)
        iva_añade=self.getPrecio()-sin_iva
        print(f'El valor original del producto es  {sin_iva} y el IVA añade {iva_añade}')
        
    

    
class IVA19(Articulos):
    def __init__(self, nombre: str, precio: int,iva:float):
         super().__init__(nombre, precio)
         self.iva=iva
    
    def setIVA(self,iva:float):
        self.iva=iva
    def getIVA(self):
        return self.iva    
    
    def bruto(self):
        porcentaje=self.getIVA()
        sin_iva=self.getPrecio()/(1+porcentaje)
        iva_añade=self.getPrecio()-sin_iva
        print(f'El valor original del producto es  {sin_iva} y el IVA añade {iva_añade}')
        
    
    

def Organizador():
    iva0=[]
    iva5=[]
    iva19=[]
    f=open('Alimentos.txt','rt')
    lines=f.readlines()
    f.close()
    for i in lines:
        a=i.rstrip('\n').split(',')
        if len(a) >= 3:
            alimento= a[1]
            iva = float(a[2])
            if iva==0:
                art1=IVA0("",0,0)
                art1.setNombre(alimento)
                art1.setIVA(iva)
                iva0.append(art1)
            elif iva==0.5:
                art2=IVA5("",0,0)
                art2.setNombre(alimento)
                art2.setIVA(iva)
                iva5.append(art2)
            elif iva==0.19:
                art3=IVA5("",0,0)
                art3.setNombre(alimento)
                art3.setIVA(iva)
                iva19.append(art2)
    return iva0,iva5,iva19
    
    
    
    
       
      
def lista():
      f=open('Alimentos.txt','rt')
      lines=f.readlines()
      f.close()
      for i in lines:
            a=i.rstrip('\n').split(',')
            if len(a) >= 3:
                  print(a[1])
                  



    

def main():
    articulos=[]
    opc='n'
    lista()
    articulo=input('Ingrese el nombre de su alimento basado en esta lista')
    iva=float(input('Ingrese el IVA del producto con base en la lista'))
    precio=int(input('Ingrese el precio del producto'))
    while opc=='n':
        if iva==0:
            art1=IVA0("",0,0)
            art1.setNombre(articulo)
            art1.setPrecio(precio)
            art1.setIVA(iva)
            articulos.append(art1)
            opc=input('Desea saliir? (y/n)')
            if opc.lower() == 'y':
                break
            elif opc.lower() == 'n':
                continue
            else:
                print('Invalido')
                break   

        
        elif iva==0.5:
            art2=IVA5("",0,0)
            art2.setNombre(articulo)
            art2.setPrecio(precio)
            art2.setIVA(iva)
            articulos.append(art2)
            opc=input('Desea saliir? (y/n)')
            if opc.lower() == 'y':
                break
            elif opc.lower() == 'n':
                continue
            else:
                print('Invalido')
                break  
        
        elif iva==0.19:
            art3=IVA19("",0,0)
            art3.setNombre(articulo)
            art3.setPrecio(precio)
            art3.setIVA(iva)
            articulos.append(art3)
            opc=input('Desea saliir? (y/n)')
            if opc.lower() == 'y':
                break
            elif opc.lower() == 'n':
                continue
            else:
                print('Invalido')
                break  

            
        
        
        if opc.lower() == 'y':
            break
        elif opc.lower() == 'n':
            continue
        else:
            print('Invalido')
            break    
    
    print('\n') #Salto de linea por razones esteticas
    for i in articulos:
        print('-----------------------------------')
        print(f'Articulo {i.getNombre()}')
        print(f'iva: {i.getIVA()}')
        print(f'precio:{i.getPrecio()}')
        print('')
        i.bruto()
        print('-------')
        
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

if __name__=='__main__':
    main()
    