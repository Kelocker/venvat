<div align="center">

<h1>venvat</h1>

<p align="center">
  <img src="https://drive.google.com/uc?id=134ISLGGnBuv8OT2AsV5lR0nNIHNX38z1" alt="venvat-logo"/>
</p>

<p align="center">
  <a href="./CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat-square" alt="Contributing Badge"/>
  </a>
  <a href="https://github.com/Kelocker/venvat/blob/main/.github/workflows/publish.yml">
    <img src="https://github.com/Kelocker/venvat/actions/workflows/publish.yml/badge.svg" alt="Publish Python Package"/>
  </a>
  <a href="https://github.com/Kelocker/venvat">
    <img src="https://img.shields.io/github/repo-size/Kelocker/venvat.svg?style=flat-square" alt="Repo Size"/>
  </a>
  <a href="https://pepy.tech/project/venvat">
    <img src="https://static.pepy.tech/badge/venvat" alt="Downloads"/>
  </a>
</p>


</div>

---

## Table of Contents

1. [Package Disclaimer](#package-disclaimer)
2. [Limitations](#limitations)
3. [Introduction](#introduction)
4. [Venvat](#venvat)
5. [Global](#global)
6. [Venvat Global](#venvat-global)
7. [Difference between Venvat and Venvat Global](#difference-between-venvat-and-venvat-global)
8. [Installation for Venvat (Windows only)](#installation-for-venvat-windows-only)
    - [Requirements](#requirements)
    - [Installing Python](#installing-python)
    - [Installing pip](#installing-pip)
    - [Installing venvat](#installing-venvat)
    - [Activating Your Virtual Environment](#activating-your-virtual-environment)
    - [Specifying a Custom Virtual Environment](#specifying-a-custom-virtual-environment)
9. [Installation for Venvat Global (Linux and macOS)](#installation-for-venvat-global-linux-and-macos)
    - [Requirements](#requirements-1)
    - [Installing Venvat Global](#installing-venvat-global)
    - [How to Uninstall Venvat Global](#how-to-uninstall-venvat-global)
    - [Configure Venv](#configure-venv)
10. [Security](#security)
11. [Support](#support)
12. [How to Contribute](#how-to-contribute)
13. [Feedback](#feedback)

---

## Package Disclaimer

The `venvat` package is provided "as is" without any warranties, express or implied. While every effort has been made to ensure the functionality and reliability of this package, the authors do not guarantee that it will be free of errors, bugs, or interruptions. By using this package, you agree that the authors will not be held liable for any damages or losses resulting from its use, including but not limited to data loss, system downtime, or any other negative consequences.

This package is intended for educational and development purposes. It is not recommended for use in production environments without proper testing and validation by the user.

Users are solely responsible for determining the suitability of this package for their own use cases and must exercise caution when integrating it into any system. Always ensure you have backups and recovery plans in place before deploying this package in critical environments.

In no event shall the authors or contributors be held liable for any damages arising in any way from the use of this project. Users of this project are solely responsible for compliance with any legal obligations, including but not limited to data privacy and intellectual property rights.

---

## Limitations

1. **Environment Compatibility**: The `venvat` package has been primarily tested on specific operating systems and environments. Compatibility with all versions of Windows or other operating systems is not guaranteed.
2. **Virtual Environment Naming**: The package assumes a certain directory structure for virtual environments. Custom naming conventions or unconventional directory layouts may require additional configuration or modifications to the script.
3. **Error Handling**: While the package includes basic error handling, it may not cover all edge cases. Users are encouraged to review and modify the code as needed to handle their specific scenarios.
4. **Performance**: The package is designed for small to medium-sized projects. Performance in very large projects or in systems with significant load may vary and should be assessed by the user.
5. **Security Considerations**: The package does not include advanced security features. Users should ensure that appropriate security measures are in place when using this package in any environment, especially those involving sensitive data or public-facing systems.
6. **Support and Maintenance**: The `venvat` package is provided with limited support. Users are encouraged to contribute to its development and report any issues via the project's issue tracker. However, there is no guarantee of timely fixes or updates.

By using this package, you agree to these terms and conditions. Learn more in the [LICENSE](https://github.com/Kelocker/venvat/blob/main/LICENSE).

---

## Introduction

Are you tired of typing long commands to activate Python virtual environments? **venvat** simplifies this process with a single command. This tool is designed to streamline the activation of virtual environments, making your workflow more efficient.

---

## Venvat
<p align="center">
  <img src="https://drive.google.com/uc?id=134ISLGGnBuv8OT2AsV5lR0nNIHNX38z1" alt="venvat-logo"/>
</p>

<p align="center">
  <img src="https://drive.google.com/uc?id=1QEo4IYj2iKWTNWk5wDCHkYh535m0Fmqa" alt="venvat-available-windows"/>
</p>

---

## Global
<p align="center">
  <img src="https://drive.google.com/uc?id=1TnDq98b17is2vpmxYAUcfIt2mCJx1pbY" alt="global-environment" />
</p>

We are thrilled to announce that we are contributing to the global environment.

---

## Venvat Global

<p align="center">
  <img src="https://drive.google.com/uc?id=15e8BQvMFsyY1c-AM3S1vnUWQI8GI4u-7" alt="venvat-global-officials-version"/>
</p>

<p align="center">
  <img src="https://drive.google.com/uc?id=1zH_oh-zisr8uPaBiFqWIta_M2UxnRb74" alt="global-venvat-officials-version now available for Linux and macOS"/>
</p>

---

## Difference between Venvat and Venvat Global

| Feature             | Venvat                            | Venvat Global              |
|---------------------|-----------------------------------|----------------------------|
| Downloads           | Downloads every time in a venv    | Download once globally     |
| Supported Platform  | Windows only                      | Linux and macOS            |

---

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

*Optional* To uninstall `venvat` package, run:

```
pip uninstall venvat
```

### How to Uninstall Venvat Global

To remove `venvat` from your shell configuration, run:

```
venvat --remove
```

### Configure Venv

`venvat` assumes your virtual environment is named `venv`. If you're using a different name for your virtual environment, use:

```
venvat --venv your-venv-name
```

---

## Security

For information on how to report security vulnerabilities, please see our [Security Policy](./SECURITY.md).

---

## Support

For questions, issues, or support with `venvat`, please open an issue on the [GitHub issues page](https://github.com/Kelocker/venvat/issues).

---

## How to Contribute

Contributions are welcome! If you'd like to contribute, please fork the repository and create a feature branch. Pull requests are warmly encouraged. For more details, please refer to our [CONTRIBUTING.md](https://github.com/Kelocker/venvat/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/Kelocker/venvat/blob/main/CODE_OF_CONDUCT.md).

---

## Feedback

<p align="center">
  <img src="https://drive.google.com/uc?id=1fbYzARRQkFIe0cx8bqnZHyIZUnllGY6w" />
</p>

We need your feedback! Feel free to share your thoughts and suggestions on the [Discussion page](https://github.com/Kelocker/venvat/discussions).