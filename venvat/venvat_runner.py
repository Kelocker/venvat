import argparse
import subprocess
import os

def run_venvat_script(venv_name=None, help_flag=False, reset_flag=False):
    """Runs the venvat PowerShell script to activate the specified virtual environment or show help."""
    script_path = os.path.join(os.path.dirname(__file__), 'venvat.ps1')
    
    if not os.path.exists(script_path):
        print("Error: venvat PowerShell script not found at", script_path)
        return
    
    command = ['powershell.exe', script_path]
    if help_flag:
        command.append("--help")
    elif reset_flag:
        command.append("--reset")
    elif venv_name:
        command.append(f"--venv {venv_name}")
    
    try:
        subprocess.call(command, shell=True)
    except Exception as e:
        print(f"Failed to execute venvat script: {e}")

def main():
    parser = argparse.ArgumentParser(description="Activate a Python virtual environment easily.")
    parser.add_argument('--venv', type=str, help='Specify the virtual environment to activate')
    parser.add_argument('--help', action='store_true', help='Show this help message and exit')
    parser.add_argument('--reset', action='store_true', help='Reset the venvat configuration')

    args = parser.parse_args()

    if args.help:
        run_venvat_script(help_flag=True)
    elif args.reset:
        run_venvat_script(reset_flag=True)
    elif args.venv:
        run_venvat_script(venv_name=args.venv)
    else:
        run_venvat_script()

if __name__ == "__main__":
    main()
