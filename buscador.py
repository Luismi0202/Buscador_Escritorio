import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import json
import os
import webbrowser
import sys
import subprocess

# ------------------------------
# Utility Functions
# ------------------------------

def install_package(package):
    """
    Installs a Python package using pip if it is not already installed.

    Args:
        package (str): The name of the package to install.
    """
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", package], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{package} installed successfully.")
            try:
                __import__(package)
            except ImportError:
                print(f"Error: Could not import {package} after installation.")
        else:
            print(f"Error installing {package}:\n{result.stderr}")

install_package("requests")
import requests

# ------------------------------
# Configuration and Initialization
# ------------------------------

# File configuration
HISTORY_FILE = "./history.json"
CONFIG_FILE = "./config.json"

# Initialize the configuration file if it does not exist or is empty
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as file:
        json.dump({"serpapi_key": None, "language": "en"}, file)  # Initialize with default values

# Load configuration
try:
    with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
        config = json.load(file)
        if not isinstance(config, dict):
            raise ValueError("The config.json file is not properly formatted.")
except (json.JSONDecodeError, ValueError):
    config = {"serpapi_key": None, "language": "en"}
    with open(CONFIG_FILE, 'w', encoding='utf-8') as file:
        json.dump(config, file)

SERPAPI_KEY = config.get("serpapi_key")
LANGUAGE = config.get("language", "en")  # Default to English if not specified
SERPAPI_URL = "https://serpapi.com/search"

# Load history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
        history = json.load(file)
else:
    history = []

# ------------------------------
# Configuration Management
# ------------------------------

def save_config():
    """
    Saves the current configuration to the config.json file.
    """
    with open(CONFIG_FILE, 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)

def update_api_key(new_key):
    """
    Updates the API key and saves it to the configuration file.

    Args:
        new_key (str): The new API key to save.
    """
    global SERPAPI_KEY
    SERPAPI_KEY = new_key
    config["serpapi_key"] = new_key
    save_config()

def get_api_key():
    """
    Prompts the user for the API key if it is not configured.

    Returns:
        bool: True if the API key is configured, False otherwise.
    """
    global SERPAPI_KEY
    if not SERPAPI_KEY:
        new_key = simpledialog.askstring("API Key", "Enter your SerpAPI key:", parent=root)
        if new_key:
            update_api_key(new_key)
        else:
            messagebox.showerror("Error", "The API key is required to perform searches.")
            return False
    return True

def modify_api_key():
    """
    Allows the user to modify the API key through a dialog.
    """
    new_key = simpledialog.askstring("Modify API Key", "Enter the new SerpAPI key:", parent=root)
    if new_key:
        update_api_key(new_key)
        messagebox.showinfo("Success", "API key updated successfully.")
    else:
        messagebox.showerror("Error", "The API key cannot be empty.")

def modify_language():
    """
    Allows the user to modify the application language.
    """
    global LANGUAGE
    new_language = simpledialog.askstring(
        "Modify Language",
        "Enter the language code ('en' for English, 'es' for Spanish):",
        parent=root
    )
    if new_language in ["en", "es"]:
        LANGUAGE = new_language
        config["language"] = new_language
        save_config()
        messagebox.showinfo(
            "Success" if LANGUAGE == "en" else "Éxito",
            "Language updated successfully. Please restart the application for changes to take effect."
            if LANGUAGE == "en" else
            "Idioma actualizado correctamente. Por favor, reinicie la aplicación para que los cambios tengan efecto."
        )
    else:
        messagebox.showerror(
            "Error",
            "Invalid language code. Use 'en' for English or 'es' for Spanish."
        )

# ------------------------------
# Search Functionality
# ------------------------------

def search(query):
    """
    Performs a search using SerpAPI.

    Args:
        query (str): The search query.

    Returns:
        list: A list of search results, or an empty list if the search fails.
    """
    if not SERPAPI_KEY:
        messagebox.showerror("Error", "The API key is not configured.")
        return []
    
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": 5
    }
    response = requests.get(SERPAPI_URL, params=params)
    if response.status_code == 200:
        return response.json().get("organic_results", [])
    else:
        messagebox.showerror("Error", "Could not retrieve search results.")
        return []

# ------------------------------
# History Management
# ------------------------------

def save_history():
    """
    Saves the search history to the history.json file.
    """
    with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

def clear_history():
    """
    Clears the search history and updates the interface.
    """
    global history
    history = []
    save_history()
    update_history_list()

def delete_search():
    """
    Deletes a specific search from the history based on the user's selection.
    """
    selection = history_list.curselection()
    if selection:
        index = selection[0]
        del history[index]
        save_history()
        update_history_list()

def update_history_list():
    """
    Updates the history list displayed in the interface.
    """
    history_list.delete(0, tk.END)
    for item in history:
        history_list.insert(tk.END, item['query'])

# ------------------------------
# GUI Event Handlers
# ------------------------------

def on_search():
    """
    Handles the search action triggered by the user.
    """
    query = entry.get().strip()
    if not query:
        return
    
    global history
    history = [item for item in history if item['query'] != query]
    
    results = search(query)
    display_results(results)
    
    history.insert(0, {"query": query, "results": results})
    save_history()
    update_history_list()

def display_results(results):
    """
    Displays the search results in the text area.

    Args:
        results (list): A list of search results.
    """
    text_area.delete(1.0, tk.END)
    if not results:
        text_area.insert(tk.END, "No results found.\n" if LANGUAGE == "en" else "No se encontraron resultados.\n")
        return
    
    for result in results:
        title = result.get("title", "No title" if LANGUAGE == "en" else "Sin título")
        link = result.get("link", "#")
        snippet = result.get("snippet", "No description available." if LANGUAGE == "en" else "Sin descripción disponible.")
        text_area.insert(tk.END, f"Title: {title}\n" if LANGUAGE == "en" else f"Título: {title}\n")
        text_area.insert(tk.END, "Link: " if LANGUAGE == "en" else "Enlace: ", "normal")
        text_area.insert(tk.END, link, ("link", link))
        text_area.insert(tk.END, "\n")
        text_area.insert(tk.END, f"Description: {snippet}\n" if LANGUAGE == "en" else f"Descripción: {snippet}\n")
        text_area.insert(tk.END, "-" * 50 + "\n")

def on_link_click(event):
    """
    Opens a link in the browser when clicked.

    Args:
        event: The click event.
    """
    widget = event.widget
    index = widget.index(f"@{event.x},{event.y}")
    for tag in widget.tag_names(index):
        if tag.startswith("http"):
            webbrowser.open(tag)
            break

def on_history_select():
    """
    Handles the selection of a previous search from the history list.
    """
    selection = history_list.curselection()
    if selection:
        index = selection[0]
        query = history[index]['query']
        entry.delete(0, tk.END)
        entry.insert(0, query)

def repeat_search():
    """
    Repeats a search for a term selected from the history list.
    """
    on_history_select()
    on_search()

# ------------------------------
# Main Function
# ------------------------------

def main():
    """
    Main function to initialize and run the application.
    """
    global root, entry, history_list, text_area

    root = tk.Tk()
    root.title("Multi-Engine Search" if LANGUAGE == "en" else "Buscador Multimotor")
    root.geometry("800x600")

    if not get_api_key():
        root.destroy()
        sys.exit()

    frame = tk.Frame(root)
    frame.pack(pady=10)

    entry = tk.Entry(frame, width=50)
    entry.pack(side=tk.LEFT, padx=5)

    search_button = tk.Button(frame, text="Search" if LANGUAGE == "en" else "Buscar", command=on_search)
    search_button.pack(side=tk.LEFT)

    modify_key_button = tk.Button(frame, text="Modify API Key" if LANGUAGE == "en" else "Modificar Clave API", command=modify_api_key)
    modify_key_button.pack(side=tk.LEFT, padx=5)

    modify_language_button = tk.Button(frame, text="Modify Language" if LANGUAGE == "en" else "Modificar Idioma", command=modify_language)
    modify_language_button.pack(side=tk.LEFT, padx=5)

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

    clear_history_button = tk.Button(button_frame, text="Clear History" if LANGUAGE == "en" else "Vaciar Historial", command=clear_history)
    clear_history_button.pack(fill=tk.X)

    delete_search_button = tk.Button(button_frame, text="Delete Selected" if LANGUAGE == "en" else "Eliminar Seleccionado", command=delete_search)
    delete_search_button.pack(fill=tk.X)

    repeat_search_button = tk.Button(button_frame, text="Repeat Search" if LANGUAGE == "en" else "Volver a Buscar", command=repeat_search)
    repeat_search_button.pack(fill=tk.X)

    update_history_list()

    root.mainloop()

# ------------------------------
# Entry Point
# ------------------------------

if __name__ == "__main__":
    main()