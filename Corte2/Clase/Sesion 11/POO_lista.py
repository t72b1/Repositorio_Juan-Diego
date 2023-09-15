class Estudiante:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.nacionalidad='Colombia'

    def entender(self):
        return  'Si, aprendi mucho hoy'
        

def main():
    estudiante=[]
    while 1:
        estudiante.append(Estudiante()) 
        



if __name__== "__main__":
    main()