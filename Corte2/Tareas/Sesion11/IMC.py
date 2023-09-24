class Personas:
    def __init__(self):
        self.nombre=None
        self.estatura=None
        self.peso=None


    def masaCorporal(self):
      imc=self.peso/self.estatura**2
      return  round(imc,2)

def main():
    persona=[]
    p1=Personas()
    p1.nombre='Pedro Caceres'
    p1.estatura=1.88
    p1.peso=97

    p2=Personas()
    p2.nombre='Maria Pérez'
    p2.estatura=1.60
    p2.peso=47

    p3=Personas()
    p3.nombre='Julian Dominguez'
    p3.estatura=1.58
    p3.peso=58

    p4=Personas()
    p4.nombre='Jessica Fuentes'
    p4.estatura=1.70
    p4.peso=73

    persona.extend([p1,p2,p3,p4])
    for i in persona:
        print(f'Nombre: {i.nombre}\nEstatura:{i.estatura}\nPeso: {i.peso}\nIMC:{i.masaCorporal()}\n\n')






if __name__== "__main__":
    main()