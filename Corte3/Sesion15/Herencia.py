class Deportista():
    def __int__(self,nombre:str,edad:int,documento:str):
        self.__nombre:nombre
        self.__edad:edad
        self.__documento:documento
    
    #-----------Setters--------------
    def setNombre(self,nombre:str):
         self.__nombre=nombre
    def getNombre(self):
         return self.__nombre
    
    def setEdad(self,edad:int):
        self.__edad=edad
    def getEdad(self):
        return self.__edad

    def setDocumento(self,documento:str):
        self.__documento=documento
    def getDocumento(self):
        return self.__documento
    
    #-----------Getters--------------
    def getNombre(self):
         return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getDocumento(self):
        return self.__documento
    

class Futbolista(Deportista):
    def __init__(self, nombre:str, edad: int, documento: str, nombre_equipo:str, goles:int) -> None:
        super().__init__(nombre, edad, documento)
        self.nombre_equipo=nombre_equipo
        self.goles=goles

    #-----------Setters--------------
    def setNombreEquipo(self,nombre_equipo:str):
        self.nombre_equipo=nombre_equipo
    
    def setGoles(self,goles:int):
        self.goles=goles
    #-----------Getters--------------
    def getNombreEquipo(self):
        return self.nombre_equipo
    def getGoles(self):
        return self.goles
    

    #-----------Metodos-------------
    def patear(self):
        return f'El jugador {self.getNombre()} acaba de anotar un gol'
    


class Tenista(Deportista):
    def __init__(self, nombre:str, edad: int, documento: str, set_ganados:int, ace:int):
        super().__init__(nombre, edad, documento)
        self.set_ganados=set_ganados
        self.ace=ace
    #-----------Setters--------------
    def setSetGanados(self,set_ganados:int):
        self.set_ganados=set_ganados
    
    def setAce(self,ace:int):
        self.ace=ace

    #-----------Getters--------------
    def getSetGanados(self):
        return self.set_ganados
    
    def getAce(self):
        return self.ace
    
    #-----------Meodos-------------
    def Ace(self):
        return f'El {self.getNombre()} acaba de hace un punto'



def main():
    jugador1=Futbolista('Radamel Falcao Garcia',35,'1234231511','Colombia',34)
    jugador2=Tenista('Roger Federer',42,'1341242141',6,12)
    jugador3=Deportista('Magnus Carlsen',32,'151514145')


    print(jugador2.Ace())
    print(jugador1.patear())






if __name__=='__main__':
    main()
