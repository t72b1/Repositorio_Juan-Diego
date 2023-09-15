#Clase
#Objetos
#Instancias
#Atributos (campos)
#Metodos (Acciones que realiza el objeto)
class Estudiante:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.nacionalidad='Colombia'

    def entender(self):
        return  'Si, aprendi mucho hoy'
        

def main():
    est1=Estudiante()
    est1.nombre='Juan'
    est1.apellido='Picon'
    est1.edad=17

    est2=Estudiante()
    est2.nombre='Roger'
    est2.apellido='Piñeros'
    est2.edad=17
    
    print(f'El estudiante {est1.nombre} {est1.apellido}',\
          f'tiene una edad de {est1.edad}',\
            f'y su nacionalidad es: {est1.nacionalidad}')
    input('Entendio?')
    print(est2.entender())



if __name__== "__main__":
    main()