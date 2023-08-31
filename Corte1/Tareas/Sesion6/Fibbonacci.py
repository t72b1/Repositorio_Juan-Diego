n = int(input('Ingrese la cantidad de numeros que quiere ver de la secuencia: '))
resultado = 0
i = 0 
if n <= 0:
    print('Ingrese un numero entero positivo')
else:
    a=0
    b=1
    print('La secuencia de Fibonacci es:\n',a,)
    for i in range(n - 1):
        print('' ,b,)
        a, b = b, a + b