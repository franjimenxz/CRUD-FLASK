#En consola hacer el porcentaje de dos números.

def porcentaje(a,b):
    valor=((a/b)*100)
    return f"{a} es el {valor}% de {b}"

numero1=int(input("Ingrese primer valor"))
numero2=int(input("Ingrese segundo valor"))
resultado = porcentaje(numero1,numero2)

print(resultado)