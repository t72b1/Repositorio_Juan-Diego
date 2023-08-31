import math as m
a=int(input('Ingrese el valor de a'))
b=int(input('Ingrese el valor de b'))
c=int(input('Ingrese el valor de c'))

x1=(-b+m.sqrt((b**2)-(4*a*c)))/(2*a)
x2=(-b-m.sqrt((b**2)-(4*a*c)))/(2*a)

print('x1=' ,x1, \
    'x2=' ,x2, '')

#help(math) comando para ayuda en todos los comandos math 