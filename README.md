# Desktop Searcher

This is a Python and Tkinter-based program that allows you to perform Google searches through the SerpAPI, store the search history, and view the results in a graphical interface.

[CLICK TO SEE DOCUMENTATION PAGE!!](https://luismi0202.github.io/Buscador_Escritorio/buscador.html)

## Motivation
This idea came from the thought that it would be better to have a search engine similar to the one in the computer's search bar but using AI to rank the best searches and relying on a better engine than Edge. With this idea in mind, I started coding this program.

## Features
- Perform Google searches using the SerpAPI.
- Display results with clickable links.
- Save search history in a JSON file.
- Allow deletion of individual searches from the history.
- Option to clear the entire history.
- Ability to re-search terms from the history.
- Avoid duplicates in the history by moving a repeated search to the top.
- Support for multiple languages (currently English and Spanish).

## Requirements
### To run the program, you need:
- Python 3.x
- Required modules: `tkinter`, `requests`, `json`, `os`, `webbrowser`
- A SerpAPI API key

## Installation
```bash
# Clone or download this repository
git clone https://github.com/your_user/Desktop_Searcher.git
cd Desktop_Searcher
```

### Configuration
1. Get a SerpAPI key from [SerpAPI](https://serpapi.com/).
2. When you open the program, you will be prompted to enter the API key. You can also modify it later from the interface.

## Deployment
### Option 1: Run from Python
1. Make sure Python is installed on your system.
2. Install the required modules by running:
   ```bash
   pip install requests
   ```
3. Navigate to the project folder and run:
   ```bash
   python searcher.py
   ```

### Option 2: Run the .exe file
1. If you have access to the executable file (`.exe`), simply double-click it to start the application.

## Usage Examples
1. **Perform a search:**
   - Enter a term in the input bar and press "Search."
   - The results will appear in the window with clickable links.

2. **Manage history:**
   - Select a previous search in the history list and press "Re-Search" to repeat it.
   - Use the "Delete Selected" or "Clear History" buttons to manage the history.

3. **Change settings:**
   - Modify the API key or language from the corresponding buttons in the interface.

### Visual Example:
- **Search:** "Python programming"
- **Results:** 
  ```
  Title: Python.org
  Link: https://www.python.org
  Description: The official website of Python programming language.
  ```

## Notes
- If you perform multiple searches for the same term, it will move to the top instead of being duplicated in the history.
- To ensure the links work correctly, make sure you have Internet access.

## Change Log
### Strategy
The development of this project has been based on the following strategic objectives:
1. **Facilitate Google searches from a desktop interface.**
2. **Provide an intuitive and customizable user experience.**
3. **Ensure efficient persistence and management of search history.**

### Changes Made
1. **Support for multiple languages:**
   - Added functionality to switch between English and Spanish.
   - Linked to the strategic objective of customization.

2. **Improved history management:**
   - Implemented functionality to avoid duplicates in the history.
   - Linked to the strategic objective of efficient history management.

3. **Improved graphical interface:**
   - Added buttons to modify the API key and language.
   - Linked to the strategic objective of providing an intuitive experience.
                     |

## License
This project is free to use. You can modify and adapt it according to your needs.
