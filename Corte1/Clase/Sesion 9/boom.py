def cuenta_atras(num):
    num-=1 #Le resta 1 a la variable
    if num>0: #Pregunta si num es mayor a 0
        print(num)
        cuenta_atras(num)
    else:
        print('Boooooom')
    print('Fin de la función', num)

    



    if __name__=="__main__":
        cuenta_atras(5)