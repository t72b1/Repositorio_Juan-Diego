n = int(input('Ingrese un número: '))
a = int(input('Ingrese otro número: '))
resultado = 0
i = 0 
if a < 0:
    while i >a: 
        resultado -= n
        i -= 1
else:
    while i < a:
        resultado += n
        i += 1
print('El producto es:', resultado)
