import Fcn_Tupla

def main():
    a='0'
    pal=''
    while a != 'exit':
        pal+=(f'{a}')
        a=input('Ingrese un dato:')
    Fcn_Tupla.app(pal,i=1)


if __name__=='__main__':
    main()
else:
    Fcn_Tupla.app(7,5,2,'Hola',b=5,c=2,k='hola')