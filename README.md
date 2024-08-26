<div align="center">

<h1>venvat</h1>

<p align="center">
  <img src="https://drive.google.com/uc?id=120eoXcHEWwuY0Wj5hsAZqMBOayuo8eIk" />
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
</p>

</div>

- - -

## Table of Contents

1. [Package Disclaimer](#package-disclaimer)
2. [Limitations](#limitations)
3. [Introduction](#introduction)
4. [Installation](#installation)
    - [Requirements](#requirements)
    - [Installing Python](#installing-python)
    - [Installing pip](#installing-pip)
    - [Installing venvat](#installing-venvat)
5. [Activating Your Virtual Environment](#activating-your-virtual-environment)
    - [Specifying a Custom Virtual Environment](#specifying-a-custom-virtual-environment)
6. [Security](#security)
6. [Support](#support)
7. [How to Contribute](#how-to-contribute)

- - -

## Package Disclaimer
The `venvat` package is provided "as is" without any warranties, express or implied. While every effort has been made to ensure the functionality and reliability of this package, the authors do not guarantee that it will be free of errors, bugs, or interruptions. By using this package, you agree that the authors will not be held liable for any damages or losses resulting from its use, including but not limited to data loss, system downtime, or any other negative consequences.

This package is intended for educational and development purposes. It is not recommended for use in production environments without proper testing and validation by the user.

Users are solely responsible for determining the suitability of this package for their own use cases and must exercise caution when integrating it into any system. Always ensure you have backups and recovery plans in place before deploying this package in critical environments.

In no event shall the authors or contributors be held liable for any damages arising in any way from the use of this project. Users of this project are solely responsible for compliance with any legal obligations, including but not limited to data privacy and intellectual property rights.

## Limitations

1. **Environment Compatibility**: The `venvat` package has been primarily tested on specific operating systems and environments. Compatibility with all versions of Windows or other operating systems is not guaranteed.

2. **Virtual Environment Naming**: The package assumes a certain directory structure for virtual environments. Custom naming conventions or unconventional directory layouts may require additional configuration or modifications to the script.

3. **Error Handling**: While the package includes basic error handling, it may not cover all edge cases. Users are encouraged to review and modify the code as needed to handle their specific scenarios.

4. **Performance**: The package is designed for small to medium-sized projects. Performance in very large projects or in systems with significant load may vary and should be assessed by the user.

5. **Security Considerations**: The package does not include advanced security features. Users should ensure that appropriate security measures are in place when using this package in any environment, especially those involving sensitive data or public-facing systems.

6. **Support and Maintenance**: The `venvat` package is provided with limited support. Users are encouraged to contribute to its development and report any issues via the project's issue tracker. However, there is no guarantee of timely fixes or updates.

By using this package, you agree to these terms and conditions. Learn more in the [LICENSE](https://github.com/Kelocker/venvat/blob/main/LICENSE).


## Introduction
Are you tired of typing long commands to activate Python virtual environments? **venvat** simplifies this process with a simple command. This tool is designed to streamline the activation of virtual environments, making your workflow more efficient.

## Installation

### Requirements
Before using **venvat**, ensure the following requirements are met:
- **Python**: This tool requires Python 3.6 or newer. Install Python from [the official website](https://www.python.org/downloads/).
- **Virtual Environment**: You should have a virtual environment already set up in your project. `venvat` is designed to activate these environments, not to create them.


### Installing Python
If you need to install Python, you can download it from the official site:

Visit https://www.python.org/downloads/



### Installing pip
If `pip` is not installed, you can install it by downloading `get-pip.py`:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```


### Installing venvat
To install venvat, run the following command:
```
pip install venvat
```


## Activating Your Virtual Environment

Once `venvat` is installed, you can easily activate your virtual environment. If you're using `venvat` for the first time or if you want to switch to a different virtual environment, you need to specify the name of your virtual environment. Here’s how:


If your virtual environment is named `venv` you can run:
```
venvat
```

### Specifying a Custom Virtual Environment
If your virtual environment is not named `venv`, you will need to configure it the first time you use `venvat`:

```
venvat --venv your-env-name
```

Reseting your configuration:
```
venvat --reset
```

For more feature, you can explore with:
```
venvat --help
```

## Security
For information on how to report security vulnerabilities, please see our [Security Policy](./SECURITY.md).


## Support
For questions, issues, or support with venvat, please open an issue on the [GitHub issues page](https://github.com/Kelocker/venvat/issues).

## How to Contribute
Contributions are welcome! If you'd like to contribute, please fork the repository and create a feature branch. Pull requests are warmly encouraged. For more details, please refer to our [CONTRIBUTING.md](https://github.com/Kelocker/venvat/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/Kelocker/venvat/blob/main/CODE_OF_CONDUCT.md).
