# src/main.py

import os
import subprocess

def main():
    print("Activating virtual environment using PowerShell script...")

    # Determine the path to the PowerShell script
    script_path = os.path.join(os.path.dirname(__file__), 'venvat.ps1')

    # Check if the PowerShell script exists
    if os.path.exists(script_path):
        try:
            # Execute the PowerShell script
            result = subprocess.run(["powershell.exe", "-File", script_path], capture_output=True, text=True)

            # Output the results
            print("PowerShell Output:", result.stdout)
            if result.stderr:
                print("PowerShell Error:", result.stderr)
            
            # Check if the script ran successfully
            if result.returncode == 0:
                print("Virtual environment activated successfully.")
            else:
                print("Failed to activate virtual environment.")

        except Exception as e:
            print(f"An error occurred while running the PowerShell script: {e}")
    else:
        print("PowerShell script not found.")
