## Getting Started

### Prerequisites
1. Git
2. Python

### Installing Git

- **Windows**: Download the installer from [git-scm.com](https://git-scm.com/download/win) and follow the installation instructions.

- **Linux**: Use your package manager to install Git. For example on Ubuntu/Debian, run:
    ```bash
    sudo apt update
    sudo apt install git
    ```

### Installing Python

- **Windows**: Download the installer from [python.org](https://www.python.org/downloads/windows/) and follow the installation instructions. **Please make sure to check the box to add Python to your PATH**.

- **Linux**: Use your package manager to install Python. For example on Ubuntu/Debian, run:
    ```bash
    sudo apt update
    sudo apt install python3
    ```

### Installing Flask
Make sure to activate .venv before running pip. Install required packages using ``` pip install ```

**Windows**
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux**
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
