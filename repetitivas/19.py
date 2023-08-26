import random
import tkinter as tk

def generar_numeros():
    numeros = []
    for _ in range(20):
        numeros.append(random.randint(1, 100))
    return numeros

def actualizar_panel():
    numeros = generar_numeros()
    resultado.config(text=numeros)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Panel de Números Aleatorios")

# Crear etiqueta para mostrar números
resultado = tk.Label(ventana, text="", font=("Helvetica", 16))
resultado.pack(padx=20, pady=20)

# Crear botón para generar nuevos números
boton_generar = tk.Button(ventana, text="Generar Números Aleatorios", command=actualizar_panel)
boton_generar.pack()

ventana.mainloop()
