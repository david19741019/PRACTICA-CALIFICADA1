# Problema 3
def redondear_a_centesimas(valor):
    return round(valor, 2)

def clasificar_cuadrilatero(AB, BC, CD, DA, AC):
    # Redondear a centésimas
    AB, BC, CD, DA, AC = map(redondear_a_centesimas, [AB, BC, CD, DA, AC])

    # Verificar las propiedades para clasificar el cuadrilátero
    if AB == BC == CD == DA:
        return "Cuadrado"
    elif AB == CD and BC == DA:
        return "Rectángulo"
    elif AB == BC == CD and DA == AC and AB != DA:
        return "Rombo"
    elif AB == CD or BC == DA:
        return "Paralelogramo"
    else:
        return "Ninguno"

# Solicitar entrada del usuario
AB = float(input("Ingrese la longitud del lado AB: "))
BC = float(input("Ingrese la longitud del lado BC: "))
CD = float(input("Ingrese la longitud del lado CD: "))
DA = float(input("Ingrese la longitud del lado DA: "))
AC = float(input("Ingrese la longitud de la diagonal AC: "))

# Obtener la clasificación del cuadrilátero
clasificacion = clasificar_cuadrilatero(AB, BC, CD, DA, AC)

# Imprimir el resultado
print(f"El cuadrilátero es clasificado como: {clasificacion}")
