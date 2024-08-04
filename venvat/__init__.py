import subprocess
import os

def main():
    venv_path = ".\\venv\\Scripts\\activate"
    if os.path.exists(venv_path):
        print("Activating virtual environment...")
        subprocess.call(["powershell.exe", venv_path])
    else:
        print("Virtual environment activation script not found.")
