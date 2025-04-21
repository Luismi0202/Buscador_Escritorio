# Desktop Searcher Wiki

## Table of Contents
1. [Introduction](#introduction)
2. [Installation and Configuration](#installation-and-configuration)
3. [Project Architecture](#project-architecture)
4. [Development Guide](#development-guide)
5. [Contributions](#contributions)
6. [Frequently Asked Questions](#frequently-asked-questions)

---

## Introduction

**Desktop Searcher** is a Python and Tkinter-based application that allows users to perform Google searches using SerpAPI, store search history, and display results in a graphical interface.

- **Objective:** Enable quick and efficient searches directly from the desktop.
- **Technologies Used:**
  - Python 3.x
  - Tkinter for the graphical interface
  - SerpAPI for search functionality
  - JSON for local data storage

---

## Installation and Configuration

### Prerequisites
1. Make sure Python 3.x is installed on your system.
2. Install the required modules:
   ```bash
   pip install requests
   ```

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Luismi0202/Buscador_Escritorio.git
   cd Buscador_Escritorio
   ```
2. Configure the API key:
   - Obtain an API key from [SerpAPI](https://serpapi.com/).
   - When you launch the program for the first time, it will prompt you to enter the key.

3. Run the program:
   ```bash
   python buscador.py
   ```

---

## Project Architecture

### File Structure
```
Buscador_Escritorio/
├── buscador.py            # Main code file
├── config.json            # User configuration
├── history.json           # Search history
├── LICENSE                # MIT License
├── README.md              # General documentation
├── preguntas.md           # Questions and answers
└── Wiki.md                # Technical documentation
```

### Dependencies
- **Tkinter:** For the graphical user interface.
- **Requests:** For making API calls to SerpAPI.
- **JSON:** For managing configuration and search history.

### Data Flow
1. **User Input:** Captured via the graphical interface.
2. **Processing:** Queries are sent to SerpAPI.
3. **Output:** Results are displayed in the interface and stored in the history.

---

## Development Guide

### Setting Up the Environment
1. Install the required dependencies.
2. Customize the `config.json` file for personalized options.

### Adding New Features
1. Create a new development branch:
   ```bash
   git checkout -b feature-name
   ```
2. Implement the functionality in `buscador.py`.
3. Test the changes locally to ensure they work as expected.

### Testing
- Validate the success and failure cases of the main functionalities.
- Test compatibility across different operating systems.

---

## Contributions

### How to Contribute
1. Fork the repository.
2. Make your changes and submit a pull request.
3. Ensure your code adheres to the project's style guidelines.

---

## Frequently Asked Questions

### What should I do if the API key does not work?
Check that the entered key is valid and has the necessary permissions for Google searches via SerpAPI.

### How can I change the application's language?
Use the "Modify Language" button in the graphical interface or edit the `config.json` file directly.

### Where is the search history stored?
The history is saved in the `history.json` file located in the project's root directory.