 # problema 2
def construir_numero_cuatro_digitos(n):
    # Verificar los límites
    if 100 <= n <= 999:
        # Extraer los dígitos del número de 3 dígitos
        primer_digito = n // 100
        segundo_digito = (n // 10) % 10
        tercer_digito = n % 10

        # Calcular el dígito de control
        digito_control = (primer_digito + segundo_digito * 3 + tercer_digito * 5) % 7

        # Construir el número de 4 dígitos
        numero_cuatro_digitos = n * 10 + digito_control

        return numero_cuatro_digitos
    else:
        return "El número debe estar entre 100 y 999."

# Solicitar entrada del usuario
numero_tres_digitos = int(input("Ingrese un número de 3 dígitos (entre 100 y 999): "))

# Obtener el número de 4 dígitos y mostrarlo
resultado = construir_numero_cuatro_digitos(numero_tres_digitos)

print(f"El número de 4 dígitos construido es: {resultado}"
