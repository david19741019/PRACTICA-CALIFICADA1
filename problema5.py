# problema 5
Copy code
def es_numero_perfecto(n):
    if n <= 0:
        return False

    suma_divisores = 1  # Inicializamos con 1 porque todo número es divisible por 1
    i = 2  # Comenzamos desde 2 ya que 1 siempre es divisor

    while i * i <= n:
        if n % i == 0:
            suma_divisores += i
            otro_divisor = n // i
            if otro_divisor != i:  # Aseguramos que no contamos el mismo divisor dos veces
                suma_divisores += otro_divisor
        i += 1

    return suma_divisores == n

# Ejemplo de uso
numero = int(input("Ingrese un número positivo: "))
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
