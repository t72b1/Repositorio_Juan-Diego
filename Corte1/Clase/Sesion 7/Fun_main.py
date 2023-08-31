import Fun_externa
import Fun3
#from Fun3 import suma as s

def main():
    nombre=input('Ingrese su nombre')
    surname=input('Ingrese su apellido')
    print('-----------')
    Fun_externa.matrix(nombre,surname)
    print(f'Ejecutado desde{__name__}')
    print('-----------')
    a=int(input('Ingrese un numero'))
    b=int(input('Ingrese otro numero'))
    print('**********')
    Fun3.suma(a,b)
    print('**********')
    #s()
if __name__=='__main__':
    main()