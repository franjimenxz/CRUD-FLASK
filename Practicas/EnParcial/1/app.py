# app_consola.py

from biblioteca import contar_palabras, contar_caracteres, contar_lineas

def main():
    print("Procesador de Strings")
    print("=====================")
    
    # Solicitar al usuario que ingrese un texto
    texto = input("Ingresa un texto:\n")
    
    # Procesar el texto utilizando las funciones de la biblioteca
    palabras = contar_palabras(texto)
    caracteres = contar_caracteres(texto)
    lineas = contar_lineas(texto)
    
    # Mostrar los resultados
    print("\nResultados:")
    print(f"Cantidad de palabras: {palabras}")
    print(f"Cantidad de caracteres: {caracteres}")
    print(f"Cantidad de líneas: {lineas}")

if __name__ == "__main__":
    main()
