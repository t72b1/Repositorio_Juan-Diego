
#Archivos de Texto:

#.txt Bloc de notas
#.XML Internet
#.json
#.props
#.conf
#.sql
#srt


def lectura():#readlines()
    f=open('Corte2/Clase/Sesion10/matrizAsignacion.txt','rt')
    line=f.readlines()
    f.close()
    for i in line: #Busca elemento por elemento y lo guarda en I y lo imprime
        a=i.rstrip('\n').split(',') #Quita los saltos de texto y las comas 
        print(f'{a}=>{int(a[0])+int(a[1])}') #Suma las 2 primeras posiciones de cada linea y lo imprime al mismo tiempo 

def lectura2():#readline()
    f=open('Corte2/Clase/Sesion10/matrizAsignacion.txt','rt')
    line=f.readline()
    while line!='': #Mientras line sea diferente de vacio"
        print(line) #imprimir linea
        opc=input('Presione enter') #Pide presionar enter
        line=f.readline()#Lee la siguiente linea
    f.close()
    print('Finalizo la lectura')


def lectura3():#read()
    f=open('Corte2/Clase/Sesion10/matrizAsignacion.txt','rt')
    line=f.read()
    f.close() #Cierra el archivo pero este se queda guardado en la memoria
    print(line,len(line)) #Imprime la lista y la cantidad de caractares
    print('----------------------')
    a=line.split('\n') #Quita los saltos de linea y lo vuelve lista
    for i in a: #Va por cada posicion de a
        b=i.split(',') #Quita las comas de cada variable
        print(b) #Imprime dicha posicion
    






if __name__== "__main__":
    #lectura()
    #lectura2()
    lectura3()

    