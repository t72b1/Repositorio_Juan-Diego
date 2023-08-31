import math as ma

def operacion(n,m):
    C=(ma.factorial(n)/(ma.factorial(m)*ma.factorial(n-m)))
    return C 



if __name__=='__main__':
    operacion(6,2)