import math as m
a=int(input('Ingrese el valor de a'))
b=int(input('Ingrese el valor de b'))
c=int(input('Ingrese el valor de c'))

r=b**2-4*a*c
if (r>0):
    x1=(-b+m.sqrt(r))/(2*a)
    x2=(-b+m.sqrt(r))/(2*a)
    print('x1=' ,x1, \
    'x2=' ,x2, '')

else:
    r=m.fabs(r)
    x1r=-b/(2*a)
    x1i=m.sqrt(r)/(2*a)
    print('Las soluciones son:\n'\
          ,x1r, '+' ,x1i, 'i\n'
          ,x1r, '-' ,x1i, 'i')



