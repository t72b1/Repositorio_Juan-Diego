class Producto:
    def __init__(self, nombre:str, precio:float, cantidad:int):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad=cantidad
#Constructor^        
#Setters y getters        
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    
    def setPrecio(self,precio:float):
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    
    def setCantidad(self,cantidad:int):
        self.__cantidad=cantidad
    def getCantidad(self):
        return self.__cantidad


#metodos
    def obtener_info(self):
        print(f"{self.getNombre()} ${self.getPrecio()} Cantidad: {self.getCantidad()}")
    
    def restar_cantidad(self):
        if (self.getCantidad() > 0):
            self.setCantidad(self.getCantidad()-1)
    
    def verificar_disponibilidad(self):
        if (self.getCantidad()>0):
            print(f'Hay {self.getCantidad} de {self.getNombre} en stock')
        else:
            print(f'No hay unidades disponibles de {self.getNombre}')
            


class Snacks(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, tipo:str):
        super().__init__(nombre, precio, cantidad)
        self.__tipo=tipo
    
    def setTipo(self,tipo:str):
        self.__tipo=tipo
    def getTipo(self):
        return self.__tipo
    
    def obtener_info(self):
        print(f"Nombre: {self.getNombre()} Tipo: {self.getTipo()} ${self.getPrecio()} Cantidad: {self.getCantidad()}")
        
class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, cantidad:int,tamaño:str):
        super().__init__(nombre, precio, cantidad)
        self.__tamaño=tamaño
        
    def setTamaño(self,tamaño:str):
        self.__tamaño=tamaño
    def getTamaño(self):
        return self.__tamaño
    
    def obtener_info(self):
        print(f"Nombre: {self.getNombre()} Tamaño: {self.getTamaño()} ${self.getPrecio()} Cantidad: {self.getCantidad()}")
        





class MaquinaDispensadora():
    def __init__(self,productos=[], total_ventas=0.0):
        self.__productos = productos
        self.__total_ventas = total_ventas
        
    def setProductos(self,productos:list):
        self.__productos=productos
    def getProductos(self):
        return self.__productos
    
    def setTotalVentas(self,total_ventas:int):
        self.__total_ventas=total_ventas
    def getTotalVentas(self):
        return self.__total_ventas


    def agregar_productos(self):
        while True:
            opcion = input("1-Agregar Producto\n2-Salir: ")
            if opcion == "1":
                tipo_producto = input("Ingrese el tipo de producto (Snack/Bebida/Otro): ")
                nombre = input('Ingrese el nombre del producto: ')
                precio = float(input('Ingrese el precio del producto: '))
                cantidad = int(input('Ingrese la cantidad del producto: '))

                if tipo_producto.lower() == 'snack': #Si el producto es un snack lo envia a clase snack
                    tipo = input('Ingrese el tipo de snack: ')
                    producto = Snacks(nombre, precio, cantidad, tipo)
                elif tipo_producto.lower() == 'bebida': #Si es una bebida lo envia a la clase bebida
                    tamaño = input('Ingrese el tamaño de la bebida: ')
                    producto = Bebida(nombre, precio, cantidad, tamaño)
                else:
                    producto=Producto(nombre,precio,cantidad) #Si es otro lo envia a producto
                self.__productos.append(producto)  
                print("Producto agregado exitosamente.")

            elif opcion == "2":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def realizar_venta(self, nombre_producto: str):
        for producto in self.__productos:
            if producto.getNombre() == nombre_producto: #Si el nombre del producto esta registrado
                if producto.getCantidad() > 0: #y es menor a 0
                    producto.restar_cantidad() #le resta cantidad a dicho producto
                    self.__total_ventas += producto.getPrecio() #Y suma el precio al total de ventas
                    print(f"Venta realizada: {producto.getNombre()}") #Imprime el nombre del producto
                    return
                else:
                    print("Producto no disponible.")
                    return
        print("Producto no encontrado.")

    def total_ventas(self):
        return self.__total_ventas #Esto podria funcionar simplemente con el getTotalVentas pero es necesario el metodo


if __name__=="__main__":

    maquina = MaquinaDispensadora()

    while True:
        print("\nMáquina Dispensadora")
        opcion = input("1-Agregar Producto \n2-Realizar Venta\n3-Ver Productos\n4-Ver Total de Ventas\n5-Salir: ")

        if opcion == "1":
            maquina.agregar_productos()
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto para la venta: ")
            maquina.realizar_venta(nombre_producto)
        elif opcion == "3":
            for producto in maquina.getProductos():
                producto.obtener_info()
        elif opcion == "4":
            print(f"Total de Ventas: ${maquina.total_ventas()}")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")