"""
venvat: A package to simplify the activation of Python virtual environments using a PowerShell script.
Provides a command line tool 'venvat' that activates the virtual environment directly from the command line.
"""

from .venvat_runner import main as venvat_main

__all__ = ["venvat_main"]
