import tkinter as tk
from tkinter import messagebox, scrolledtext
import json
import os
import webbrowser
import requests

# Configuración del archivo de historial
HISTORY_FILE = "./historial.json"
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
        history = json.load(file)
else:
    history = []

# Configuración de SerpAPI
SERPAPI_KEY = "<TU_CLAVE_DE_SERPAPI>"
SERPAPI_URL = "https://serpapi.com/search"

def search(query):
    """Realiza una búsqueda real usando SerpAPI."""
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": 5
    }
    response = requests.get(SERPAPI_URL, params=params)
    if response.status_code == 200:
        results = response.json().get("organic_results", [])
        return results
    else:
        messagebox.showerror("Error", "No se pudieron obtener los resultados de búsqueda.")
        return []

def save_history():
    """Guarda el historial en un archivo JSON."""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

def clear_history():
    """Limpia el historial de búsquedas."""
    global history
    history = []
    save_history()
    update_history_list()

def delete_search():
    """Elimina una búsqueda específica del historial."""
    selection = history_list.curselection()
    if selection:
        index = selection[0]
        del history[index]
        save_history()
        update_history_list()

def update_history_list():
    """Actualiza la lista del historial en la interfaz."""
    history_list.delete(0, tk.END)
    for item in history:
        history_list.insert(tk.END, item['query'])

def on_search():
    """Maneja la acción de búsqueda."""
    query = entry.get().strip()
    if not query:
        return
    
    # Si la búsqueda ya está en el historial, se elimina
    global history
    history = [item for item in history if item['query'] != query]
    
    results = search(query)
    display_results(results)
    
    # Se agrega la nueva búsqueda al principio
    history.insert(0, {"query": query, "results": results})
    save_history()
    update_history_list()

def display_results(results):
    """Muestra los resultados en el área de texto."""
    text_area.delete(1.0, tk.END)
    if not results:
        text_area.insert(tk.END, "No se encontraron resultados.\n")
        return
    
    for result in results:
        title = result.get("title", "Sin título")
        link = result.get("link", "#")
        snippet = result.get("snippet", "Sin descripción disponible.")
        text_area.insert(tk.END, f"Título: {title}\n")
        text_area.insert(tk.END, "Enlace: ", "normal")
        text_area.insert(tk.END, link, ("link", link))
        text_area.insert(tk.END, "\n")
        text_area.insert(tk.END, f"Descripción: {snippet}\n")
        text_area.insert(tk.END, "-" * 50 + "\n")

def on_link_click(event):
    """Abre el enlace en el navegador."""
    widget = event.widget
    index = widget.index(f"@{event.x},{event.y}")
    for tag in widget.tag_names(index):
        if tag.startswith("http"):
            webbrowser.open(tag)
            break

def on_history_select():
    """Maneja la selección de una búsqueda previa."""
    selection = history_list.curselection()
    if selection:
        index = selection[0]
        query = history[index]['query']
        entry.delete(0, tk.END)
        entry.insert(0, query)

def repeat_search():
    """Realiza la búsqueda de un término seleccionado del historial."""
    on_history_select()
    on_search()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Buscador Multimotor")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(frame, text="Buscar", command=on_search)
search_button.pack(side=tk.LEFT)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=20)
text_area.pack(padx=10, pady=10)
text_area.tag_config("link", foreground="blue", underline=1)
text_area.tag_bind("link", "<Button-1>", on_link_click)

history_frame = tk.Frame(root)
history_frame.pack(pady=10)

history_list = tk.Listbox(history_frame, width=50, height=10)
history_list.pack(side=tk.LEFT, padx=5)

button_frame = tk.Frame(history_frame)
button_frame.pack(side=tk.LEFT)

clear_history_button = tk.Button(button_frame, text="Vaciar Historial", command=clear_history)
clear_history_button.pack(fill=tk.X)

delete_search_button = tk.Button(button_frame, text="Eliminar Seleccionado", command=delete_search)
delete_search_button.pack(fill=tk.X)

repeat_search_button = tk.Button(button_frame, text="Volver a Buscar", command=repeat_search)
repeat_search_button.pack(fill=tk.X)

update_history_list()

root.mainloop()
