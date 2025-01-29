import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser
import subprocess
import sys
import json
import os

# Verificar e instalar pyperclip si no están disponibles
def instalar_paquete(paquete):
    try:
        __import__(paquete)
    except ImportError:
        print(f"Instalando {paquete}...")
        resultado = subprocess.run([sys.executable, "-m", "pip", "install", paquete], capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"{paquete} instalado correctamente.")
            try:
                __import__(paquete)
            except ImportError:
                print(f"Error: No se pudo importar {paquete} después de instalarlo.")
        else:
            print(f"Error al instalar {paquete}:\n{resultado.stderr}")

instalar_paquete("pyperclip")

import pyperclip

# Ruta del archivo de historial
HISTORIAL_FILE = "./historial.json"

# Motores de búsqueda
motores = {
    "Google": "https://www.google.com/search?q=",
    "Imágenes": "https://www.google.com/search?tbm=isch&q=",
    "Noticias": "https://www.google.com/search?tbm=nws&q=",
    "YouTube": "https://www.youtube.com/results?search_query="
}

# Cargar historial desde archivo
def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        try:
            with open(HISTORIAL_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("historial", [])
        except json.JSONDecodeError:
            return []
    return []

# Guardar historial en archivo
def guardar_historial():
    with open(HISTORIAL_FILE, "w", encoding="utf-8") as file:
        json.dump({"historial": historial}, file, ensure_ascii=False, indent=4)

# Función para buscar
def buscar():
    query = entry.get().strip()
    if query:
        motor = motores[combo_motores.get()]
        url = f"{motor}{query}"
        webbrowser.open(url)

        historial.insert(0, query)
        lista_historial.insert(0, query)
        guardar_historial()

# Función para limpiar entrada
def limpiar():
    entry.delete(0, tk.END)

# Función para copiar enlace al portapapeles
def copiar_enlace():
    query = entry.get().strip()
    if query:
        url = f"{motores[combo_motores.get()]}{query}"
        pyperclip.copy(url)
        messagebox.showinfo("Copiado", "Enlace copiado al portapapeles.")

# Función para vaciar historial
def vaciar_historial():
    global historial
    historial = []  # Vaciar la lista en memoria
    lista_historial.delete(0, tk.END)  # Limpiar la lista visible
    guardar_historial()  # Guardar el archivo vacío

# Función para eliminar la selección del historial
def eliminar_seleccion():
    seleccionados = lista_historial.curselection()
    if seleccionados:
        for index in reversed(seleccionados):
            # Eliminar el elemento de la lista visible
            lista_historial.delete(index)
            # Eliminar el elemento de la lista en memoria
            historial.pop(index)
        guardar_historial()  # Guardar los cambios en el archivo

# Crear ventana
root = tk.Tk()
root.title("DeskBrowser")
root.geometry("450x400")
root.resizable(False, False)

# Estilos
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 12))

# Entrada de búsqueda
entry = ttk.Entry(root, width=40, font=("Arial", 12))
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
entry.bind("<Return>", lambda event: buscar())

# Selector de motor de búsqueda
combo_motores = ttk.Combobox(root, values=list(motores.keys()), state="readonly")
combo_motores.set("Google")
combo_motores.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="ew")

# Botones
btn_buscar = ttk.Button(root, text="Buscar", command=buscar)
btn_buscar.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

btn_limpiar = ttk.Button(root, text="Limpiar", command=limpiar)
btn_limpiar.grid(row=2, column=1, padx=6, pady=6, sticky="ew")

btn_copiar = ttk.Button(root, text="Copiar enlace", command=copiar_enlace)
btn_copiar.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Botón para vaciar historial
btn_vaciar = ttk.Button(root, text="Vaciar historial", command=vaciar_historial)
btn_vaciar.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Botón para eliminar la selección del historial
btn_eliminar_seleccion = ttk.Button(root, text="Eliminar selección", command=eliminar_seleccion)
btn_eliminar_seleccion.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Historial de búsquedas
historial_label = tk.Label(root, text="Historial", font=("Arial", 10, "bold"))
historial_label.grid(row=7, column=0, columnspan=2, pady=(5, 0))

# Lista de historial con selección múltiple
lista_historial = tk.Listbox(root, height=5, selectmode=tk.MULTIPLE)
lista_historial.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Cargar historial previo
historial = cargar_historial()
for busqueda in historial:
    lista_historial.insert(tk.END, busqueda)

root.mainloop()
