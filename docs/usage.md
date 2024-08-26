
# Usage Guide

Welcome to the **venvat** Usage Guide. This document will walk you through the core functionalities of **venvat** and how to use it in your projects.

## Basic Usage

### Activating the Default Virtual Environment

If your virtual environment is named `venv`, you can activate it by simply running:

```
venvat
```

This command will automatically find and activate the `venv` environment in your project.

### Specifying a Custom Virtual Environment Name

If your virtual environment is named something other than `venv`, you will need to specify the name the first time you use **venvat**:

```
venvat --venv your-env-name
```

This command will activate the specified virtual environment and save the name for future use. After running this command once, you can activate the same environment by simply using:

```
venvat
```

### Resetting the Configuration

If you want to reset **venvat** and configure a new virtual environment, use the following command:

```
venvat --reset
```

This will remove the saved environment name, allowing you to set up a new one.



## Troubleshooting

### Common Issues

#### Virtual Environment Not Found

If you see an error like "Virtual environment activation script not found," make sure that:
- The virtual environment exists in the project directory.
- You have correctly specified the environment name using `--venv`.

#### Command Not Recognized

If the `venvat` command is not recognized, ensure that **venvat** is properly installed in your Python environment and that your system's PATH is correctly configured.

### Getting Help

If you encounter any issues that aren't covered here, feel free to reach out via the [GitHub issues page](https://github.com/Kelocker/venvat/issues).

## Best Practices

- **Consistent Environment Naming**: Use consistent naming conventions for your virtual environments across different projects to streamline the usage of **venvat**.
- **Keep **venvat** Updated**: Regularly check for updates to **venvat** to benefit from new features and bug fixes.

## Additional Resources

- **[Setup Guide](./setup.md)**: If you haven't set up **venvat** yet, start with the setup guide.

---

Thank you for using **venvat**! We hope this tool makes managing your Python environments easier and more efficient.

