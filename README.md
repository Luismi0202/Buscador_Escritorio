# Buscador de Escritorio

Este es un programa basado en Python y Tkinter que permite realizar búsquedas en Google a través de la API de SerpAPI, almacenar el historial de búsquedas y visualizar los resultados en una interfaz gráfica.

## Características
- 🔍 Realiza búsquedas en Google usando la API de SerpAPI.
- 📌 Muestra los resultados con enlaces clickeables.
- 📂 Guarda el historial de búsquedas en un archivo JSON.
- 🗑️ Permite eliminar búsquedas individuales del historial.
- 🚀 Opción para vaciar todo el historial.
- 🔄 Posibilidad de volver a buscar términos del historial.
- 🚫 Evita duplicados en el historial, moviendo una búsqueda repetida al primer lugar.

## Requisitos
### Para ejecutar el programa, necesitas:
- Python 3.x
- Módulos necesarios: `tkinter`, `requests`, `json`, `os`, `webbrowser`
- Una clave de API de SerpAPI

## Instalación
```bash
# Clona o descarga este repositorio
git clone https://github.com/tu_usuario/Buscador_Escritorio.git
cd buscador-multimotor
```

### Configuración
1. Obtén una clave de SerpAPI en [SerpAPI](https://serpapi.com/) 
2. Cuando abras el programa, se te pedirá una API

## Uso
Puedes abrir el archivo ejectuable .exe que se encuentra en la carpeta principal o si tienes el módulo de python instalado, puedes ejecutar en terminal el archivo buscador.py que se encuentra en la carpeta "código"

Para ejecutar el código con py:
``python
python buscador.py (desde la carpeta código en terminal)
``

El .exe simplemente se ejecutará dándole doble click.

1. Escribe un término de búsqueda en la barra de entrada y presiona "Buscar".
2. Los resultados aparecerán en la ventana con enlaces clickeables.
3. Puedes seleccionar búsquedas anteriores en la lista de historial y repetirlas.
4. Usa los botones "Eliminar Seleccionado" o "Vaciar Historial" según sea necesario.

## Notas
- ⚠️ Si realizas varias búsquedas del mismo término, este se moverá al inicio en lugar de duplicarse en el historial.
- 🌐 Para que los enlaces funcionen correctamente, asegúrate de tener acceso a Internet.

## Licencia
Este proyecto es de uso libre. Puedes modificarlo y adaptarlo según tus necesidades.



