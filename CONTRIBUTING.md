## Getting Started

### Prerequisites
1. Git
2. Python
3. SQLite

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

### Installing SQLite

- **Linux**: Use your package manager to install SQLite. For example on Ubuntu.Debian, run:
    ```bash
    sudo apt update
    sudo apt install sqlite3
    sudo apt install libsqlite3-dev
    ```
    Verify your SQLite installation by running (It should output the SQLite version number):
    ```bash
    sqlite3 --version
    ```