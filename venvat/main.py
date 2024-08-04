# venvat/main.py

import os
import shutil
import subprocess
import argparse

# Function to read the version from the VERSION file
def read_version():
    version_file_path = os.path.join(os.path.dirname(__file__), '..', 'VERSION')
    with open(version_file_path) as version_file:
        return version_file.read().strip()

# Read the current version
VERSION = read_version()

def activate_venv():
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

def publish_script():
    """Copy the venvat.ps1 script to the project root directory."""
    current_directory = os.getcwd()  # Get the current working directory
    src_path = os.path.join(os.path.dirname(__file__), 'venvat.ps1')
    dest_path = os.path.join(current_directory, 'venvat.ps1')

    try:
        shutil.copy(src_path, dest_path)
        print(f"Copied venvat.ps1 to {dest_path}")
    except FileNotFoundError:
        print("Source PowerShell script not found.")
    except Exception as e:
        print(f"An error occurred while copying the script: {e}")

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="venvat: A tool for managing Python virtual environments",
        formatter_class=argparse.RawTextHelpFormatter  # Allow for detailed help formatting
    )

    # Add arguments to the parser
    parser.add_argument(
        '--publish', 
        action='store_true', 
        help="Copy venvat.ps1 to the project root directory"
    )
    parser.add_argument(
        '--version', 
        action='version', 
        version=f"venvat {VERSION}", 
        help="Show the current version of venvat"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Handle the publish argument
    if args.publish:
        publish_script()
    else:
        # Show help message if no specific flag is provided
        parser.print_help()
        print("\nTo activate your virtual environment, run the following command in PowerShell:")
        print(".\\venvat.ps1")

