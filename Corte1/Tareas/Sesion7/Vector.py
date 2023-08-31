import math

def main():
    x_inicio = float(input('Ingrese la coordenada x del punto de inicio: '))
    y_inicio = float(input('Ingrese la coordenada y del punto de inicio: '))
    x_final = float(input('Ingrese la coordenada x del punto final: '))
    y_final = float(input('Ingrese la coordenada y del punto final: '))
    
    m = modulo(x_final - x_inicio, y_final - y_inicio)
    ang = angulo(x_final - x_inicio, y_final - y_inicio)
    comp = componentes(m, ang)
    
    print(f'La magnitud del vector definido por los puntos ({x_inicio}, {y_inicio}) y ({x_final}, {y_final}) es {m}')
    print(f'Sus componentes son: {comp}')


def modulo(x, y):
    m = math.sqrt(x ** 2 + y ** 2) #Calcula la magnitud del vector con base a sus coordendas de origen y fin del vector
    return m

def angulo(cx, cy):
    theta = math.atan2(cy, cx)  #Calcula el angulo del vector
    return theta

def componentes(m, theta):
    cx = m * math.cos(theta)
    cy = m * math.sin(theta)
    return (cx, cy)

if __name__ == "__main__":
    main()
