def calcular_porcentaje(valor1, valor2):
    if valor2 == 0:
        return "El segundo valor no puede ser cero."
    porcentaje = (valor1 / valor2) * 100
    return f"{valor1} es el {porcentaje}% de {valor2}"

# Solicitar los valores al usuario
try:
    valor1 = float(input("Ingrese el primer valor: "))
    valor2 = float(input("Ingrese el segundo valor: "))
    resultado = calcular_porcentaje(valor1, valor2)
    print(resultado)
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
