# Setup Guide

## Table of content
1. [Installation for Venvat (Windows only)](#installation-for-venvat-windows-only)
    - [Requirements](#requirements)
    - [Installing Python](#installing-python)
    - [Installing pip](#installing-pip)
    - [Installing venvat](#installing-venvat)
    - [Activating Your Virtual Environment](#activating-your-virtual-environment)
    - [Specifying a Custom Virtual Environment](#specifying-a-custom-virtual-environment)
2. [Installation for Venvat Global (Linux and macOS)](#installation-for-venvat-global-linux-and-macos)
3. [Clone repository](#Clone-repository)


## Installation
## Installation for Venvat (Windows only)

### Requirements

Before using **venvat**, ensure the following requirements are met:
- **Python**: This tool requires Python 3.6 or newer. Install Python from [the official website](https://www.python.org/downloads/).
- **Virtual Environment**: You should have a virtual environment already set up in your project. `venvat` is designed to activate these environments, not to create them.

### Installing Python

If you need to install Python, you can download it from the official site:

[https://www.python.org/downloads](https://www.python.org/downloads)

### Installing pip

If `pip` is not installed, you can install it by downloading `get-pip.py`:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Installing venvat

To install `venvat`, run the following command:

```
pip install venvat
```

---

## Activating Your Virtual Environment

Once `venvat` is installed, you can easily activate your virtual environment.

If your virtual environment is named `venv`, you can run:

```
venvat
```

*Important* : Venvat recognise `venv` as default name of the virtual environment

### Specifying a Custom Virtual Environment

If your virtual environment is not named `venv`, you will need to configure it for the first time:

```
venvat --venv your-env-name
```

Resetting your configuration:

```
venvat --reset
```

For more features, you can explore with:

```
venvat --help
```

---

## Installation for Venvat Global (Linux and macOS)

### Requirements

- **Python**: You need Python 3.6 or newer. Install it from [the official website](https://www.python.org/downloads/).
- **pip**: Ensure `pip` is installed. You can follow the same pip installation process as described earlier.

### Installing Venvat Global

To install `venvat` globally, run:

```
pip install venvat
```

Then, activate it based on your shell:

For Bash:
```
source ~/.bashrc
```

For Zsh:
```
source ~/.zshrc
```

Restart your terminal to apply the changes.

Now, `venvat` is available globally.


## Clone repository
1. Clone the repository:
   ```
   git clone https://github.com/Kelocker/venvat.git
   ```