n=float(input('Ingrese la nota'))

#if(0<=n<=5)
if (n>0 and n<=5):                          
 if n>=3.0: 
    print('Aprueva')
 else:
    print('Reprobo')
else:
  print('La nota es invalida')