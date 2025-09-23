## Table of Contents

- [Getting Started](#getting-started)
- [Submitting Pull Requests](#submitting-pull-requests)
- [Reporting Issues](#reporting-issues)

## Getting Started

1. **Fork the repository**: Click the "Fork" button at the top right of the repository page.
2. **Clone your fork**: Use the following command to clone your fork to your local machine:
    ```bash
    git clone https://github.com/aieryair/donder.git
    ```

### Prerequisites
1. Git
2. Python
3. MongoDB

### Installing Git

- **Windows**: Download the installer from [git-scm.com](https://git-scm.com/download/win) and follow the installation instructions.

- **Linux**: Use your package manager to install Git. For example on Ubuntu/Debian, run:
    ```bash
    sudo apt update
    sudo apt install git
    ```

### Installing Python

- **Windows**: Download the installer from [python.org](https://www.python.org/downloads/windows/) and follow the installation instructions.
**Make sure to check the box to add Python to your PATH**.

- **Linux**: Use your package manager to install Python. For example on Ubuntu/Debian, run:
    ```bash
    sudo apt update
    sudo apt install python3
    ```

### Installing MongoDB

- **Windows**: Download the installer from [mongodb.com](https://mongodb.com/try/download/community) and follow the installation instructions. Make sure to set up the MongoDB service.

- **Linux**: Follow the official MongoDB installation guide for your specific distribution. For example, on Ubuntu you can run: 
    ```bash
    wget -q0 - https://www.mongodb.org/static/pg
    ```

## Submitting Pull Requests

1. **Create a new branch**: Use a descriptive name for your branch.
    ```bash
    git checkout -b <your-branch>/<your-branch-name>
    ```

2. **Make your changes**: Implement your changes.

3. **Commit your changes**: Write a clear commit message.
    ```bash
    git commit -m "Made these changes for these reasons."
    ```

4. **Push to your fork**: Push your changes to your repository.
    ```bash
    git push origin <your-branch>/<your-branch-name>
    ```

5. **Open a pull request**: Go to the original repository and click on "New Pull Request".

## Reporting Issues 

When reporting an issue, please include:
- A clear and descriptive title.
- Steps to reproduce the issue.
- Any relevant screenshots or logs.