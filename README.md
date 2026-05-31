## ToDo Code
[![Flet](https://img.shields.io/badge/Flet-0.85.2-orange)](https://flet.dev)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

This code was created as a learning exercise to help me understand and become comfortable with Flet. It follows the structure and concepts 
from [this](https://flet.dev/docs/tutorials/todo) tutorial.

## Prerequisites

- Python **3.10** or higher
  
## Compile to executable

1. Clone the repository:
```bash
git clone https://github.com/lieserl-git/ToDo.git
cd ToDo
```
2. Install Dependencies:
```bash
pip install flet pyinstaller
```
3. Build command: This command creates a standalone executable in the dist folder
```bash
pyinstaller --onefile --windowed --name "ToDoApp" main.py
```

