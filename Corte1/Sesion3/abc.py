print('Programas disponibles: \n'\
    '1.ABC\n2.IVA\n3.Triangulo')

p=input('Seleccione un programa').lower()

if p=='abc' or p=='1':
    ñ=input('Ingrese una letra del abecedario')
    if ñ == 'a' or ñ == 'e'\
     or ñ == 'i' or ñ == 'o'\
     or ñ == 'u':
        print('',ñ, 'es una vocal')
    else:
        print('',ñ, ' es una consonante')
elif p=='iva' or p=='2':
    t=int(input('Ingrese el tiempo de parqueo en minutos'))
    t=t*139
    iva=t*(19/100)
    t=t+iva
    if t%50!=0:
        t=(t//50)*50+50
        iva=(t)/(1+0.19)
        r=t-iva
        print('Parqueadero' ,iva, 'n\' IVA:''', r)
    else:
        print("El resultado es:", t)
elif p=='triangulo' or p=='3':
    a=int(input('Ingrese la longitud del lado a del triangulo'))
    b=int(input('Ingrese la longitud del lado b del triangulo'))
    c=int(input('Ingrese la longitud del lado c del triangulo'))
    if c<a+b and b<c+a and a<b+c:
        if a==b==c:
            print('Es un triangulo equilatero')
        elif a==b!=c or c==b!=a or c==a!=b:
            print('Es un triangulo de Isoseles')
        else:
            print('Es un triangulo escaleno')
    else:
        print('El triangulo no es posible')

