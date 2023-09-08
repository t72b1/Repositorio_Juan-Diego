festivo={
    'Enero':['1 - año nuevo', '6- reyes magos'], 
    'Febrero': ['No tiene festivos'], 
    'Marzo': ['Dia de San Jose']}
    #El nombre de los meses es la llave, y lo que esta entre los parentesis cuadrados es la informacion

def main():
    mes=input('Ingrese un mes')
    print(festivo[mes]) #Coje la variable mes y la busca la llave en el diccionario y lo imprime







if __name__=='__main__':
    main()
