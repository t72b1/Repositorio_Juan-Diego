class Ciudadano:
    def __init__(self):
        self.__nombre=None
        self.__cedula=None
        self.__edad=None

    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def getNombre(self):
        return self. __nombre



    def setCedula(self,cedula:str):
        if isinstance(cedula,int) is True: #insinstance(cedula,int) en este caso pregunta si cedula es un entero
            if cedula>0:
                cedula=str(cedula) #Convierte cedula en string para que funcione la funcion len()
                if len(cedula)>=8 and len(cedula)<=10: #Verifica que la cedula tenga entre 10 a 8 digitos
                    self.__cedula=cedula
                else: 
                    print('Porfavor ingrese una cedula valida')
                    return False
            else:
                print('Porfavor ingrese una cedula valida')
                return False
        else:
            print('Porfavor ingrese una cedula valida')
            return False
        
    def getCedula(self):
        return self.__cedula


    def setEdad(self,edad:int):
        self.__edad=edad
    def getEdad(self):
        return self.__edad
    
    

    def mostrar(self):
         print(f'Nombre:{self.getNombre()}-Edad:{self.getEdad()}-CC:{self.getCedula()}')
         if self.esMayorDeEdad(self.getEdad()) is True:
             print('Es mayor de edad\n')
         elif self.esMayorDeEdad(self.getEdad()) is False:
             print('Es menor de edad\n')
             
             
    def esMayorDeEdad(self,edad:int):
        if edad>=18:
            return True
        elif edad<18 and edad>=0:
            return False
        else:
            return 'No' #Descubri que si le doy devolver 0 tambien cuenta como falso entonces por eso decidi utilizar esto 
        



def main():
    ciudadano=[]
    opc='n'
    while 1:
        cd=Ciudadano()
        cd.setNombre(input('Nombre: '))
        while cd.setCedula(int(input('Cédula: '))) == False:  #Mientras la funcion setCedula devuelva falso vuelve a preguntar por esta
            cd.setCedula(input('Cedula: ')) 
        cd.setEdad(int(input('Edad: ')))  
        while cd.esMayorDeEdad(cd.getEdad()) == 'No': #Llama a la funcion esMayorDeEdad con el paramatero getEdad y mientras sea no da edad invalida y pregunta otravez
            print('Porfavor ingrese una edad valida.')
            cd.setEdad(int(input('Edad: ')))
        ciudadano.append(cd)
        opc=input('Desea salir? (y/n)')
        if opc.lower() == 'y':
            break
        elif opc.lower() == 'n':
            continue
        else:
            print('Invalido')
            break
    print('\n') #Salto de linea por razones esteticas
    for i in ciudadano:
        i.mostrar()
        



if __name__=="__main__":
    main()