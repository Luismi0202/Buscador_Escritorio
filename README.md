# Buscador_Escritorio
Buscador de Escritorio con Python

Este es un sencillo buscador de escritorio creado con Python y Tkinter. Permite ingresar una consulta y abrir el navegador predeterminado con los resultados de búsqueda en Google.

# 🎯Objetivo

Mi objetivo con este proyecto es crear un navegador pequeño que se ejecute en cuanto se encienda el ordenador (falta por hacer un ejecutable que se ponga como aplicación de arranque) y así podamos buscar las cosas fácilmente sin tener que estar dentro del propio navegador.

# 📌 Requisitos

Este proyecto utiliza bibliotecas estándar de Python, por lo que no es necesario instalar paquetes adicionales.

Python 3.x

Tkinter (incluido en Python)

webbrowser (incluido en Python)

# 🚀 Instalación y Uso

Clona este repositorio o descarga el archivo buscador.py.

Asegúrate de tener Python instalado.

Ejecuta el script con el siguiente comando:

python buscador.py

Aparecerá una ventana con un campo de búsqueda.

Escribe la consulta y presiona Enter o el botón "Buscar".

Se abrirá el navegador con los resultados de Google.

# 📜 Código Principal

import tkinter as tk
import webbrowser

def buscar():
    query = entry.get()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

**Crear la ventana**
root = tk.Tk()
root.title("Buscador de Escritorio")
root.geometry("400x100")

**Campo de entrada**
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", lambda event: buscar())  # Buscar al presionar Enter

**Botón de búsqueda**
btn = tk.Button(root, text="Buscar", command=buscar)
btn.pack()

**Ejecutar la aplicación**
root.mainloop()

# 🎯 Funcionalidades

Interfaz simple con Tkinter.

Busca en Google automáticamente.

Se abre el navegador predeterminado.

Presiona Enter o el botón "Buscar" para ejecutar la búsqueda.

