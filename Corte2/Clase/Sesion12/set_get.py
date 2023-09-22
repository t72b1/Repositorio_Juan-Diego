class Estudiante:
    def __init__(self):
        self.__nombre=None
        self.__apellido=None
        self.__edad=None
        self.nacionalidad='Colombia'


    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self,apellido:str):
        self.__apellido=apellido
    def getApellido(self):
        return self.__apellido

    def setEdad(self,edad:str):
        if int(edad)>21:
            self.__edad=edad
        else: self.__edad='Menor de edad'
    def getEdad(self):
        return self.__edad


    def entender(self):
        return  'Si, aprendi mucho hoy'
    
    def setlicor(self):
        edad=self.__edad
        if int(edad)>21:
            return 'Puedde beber una pola'
        else:
            return 'Le toco jugo'
    def getLicor(self):
        return self.__licor()

        

def main():
    estudiante=[]
    opc='n'
    while 1:
        est=Estudiante()
        est.setNombre(input('Nombre:'))
        est.setApellido(input('Apellido'))
        est.setEdad(int(input('Edad:')))
        estudiante.append(est)
        opc=input('Desea salir?')
        if opc=='y':
            break
        else:
            print('Invallido')
            
    for i in estudiante:
        print(f'Nombre:{i.getNombre()} {i.getApellido()}\nEdad:{i.getEdad()}\n\n')
        print(est.licor())



if __name__== "__main__":
    main()