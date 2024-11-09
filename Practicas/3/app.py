import tkinter as tk
from math_operations import sumar, restar, multplicar, dividir

# Función para realizar la operación seleccionada
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    
    if operation == 'Suma':
        result = sumar(num1, num2)
    elif operation == 'Resta':
        result = restar(num1, num2)
    elif operation == 'Multiplicación':
        result = multplicar(num1, num2)
    elif operation == 'División':
        result = dividir(num1, num2)
    else:
        result = "Operación no válida"
    
    result_label.config(text=f"Resultado: {result}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Operaciones Matemáticas")

# Variables de entrada
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

# Menú desplegable para seleccionar la operación
operation_var = tk.StringVar(root)
operation_var.set("Suma")  # Operación predeterminada

operation_menu = tk.OptionMenu(root, operation_var, "Suma", "Resta", "Multiplicación", "División")

# Botón para calcular
calculate_button = tk.Button(root, text="Calcular", command=calculate)

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="Resultado: ")

# Colocación de elementos en la ventana
tk.Label(root, text="Número 1:").pack()
entry_num1.pack()
tk.Label(root, text="Número 2:").pack()
entry_num2.pack()
operation_menu.pack()
calculate_button.pack()
result_label.pack()

# Ejecutar la aplicación
root.mainloop()
