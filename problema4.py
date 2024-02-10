import math

def combinaciones_torres(n):
    # El número total de combinaciones es n factorial (n!)
    return math.factorial(n)

# Ejemplo de uso
n = int(input("Ingrese el tamaño del tablero (n): "))
total_combinaciones = combinaciones_torres(n)

print(f"El número total de combinaciones posibles en un tablero {n}x{n} es: {total_combinaciones}")
