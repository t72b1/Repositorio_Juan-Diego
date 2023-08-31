numero = int(input('Ingrese un numero: '))

if numero==0:
    print('Ningun numero es divisible entre cero')
    
elif numero==1:
    print('1 es divisible por si mismo')

else:
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            
            print(divisor)
    print('Son divisibles de' ,numero ,)