def es_numero_perfecto(num):
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum(divisors) == num

def main():
    cantidad = int(input("Ingrese la cantidad de números perfectos que desea encontrar (máximo 10): "))
    cantidad = min(cantidad, 10)  # Limitar a un máximo de 10 números perfectos
    
    numeros_perfectos_encontrados = 0
    numero_actual = 2
    
    print(f"Los primeros {cantidad} números perfectos son:")
    
    while numeros_perfectos_encontrados < cantidad:
        if es_numero_perfecto(numero_actual):
            print(numero_actual)
            numeros_perfectos_encontrados += 1
        numero_actual += 1

if __name__ == "__main__":
    main()
