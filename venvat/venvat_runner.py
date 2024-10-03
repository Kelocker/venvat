import argparse
import subprocess
import os
import platform
import sys

def is_windows():
    return platform.system() == "Windows"

def get_rc_file():
    home_dir = os.path.expanduser("~")
    shell = os.environ.get("SHELL", "")

    if "bash" in shell:
        return os.path.join(home_dir, ".bashrc")
    elif "zsh" in shell:
        return os.path.join(home_dir, ".zshrc")
    else:
        print(f"Unsupported shell ({shell}). Only Bash and Zsh are supported.")
        return None

def get_venvat_function(rc_file):
    if ".bashrc" in rc_file:
        return """
function venvat() {
    # Venvat: Activate Python virtual environments
    config_file="venvat.config"
    
    if [ "$1" = "--help" ]; then
        echo "Usage: venvat [--venv your-env-name] [--reset] [--remove]"
        echo "Venvat will consider 'venv' as your virtual environment name by default."
        echo "Use '--venv your-env-name' to specify the name of your virtual environment."
        echo "Use '--reset' to clear the stored virtual environment configuration."
        echo "Use '--remove' to remove the venvat function from the shell configuration."
        return
    elif [ "$1" = "--reset" ]; then
        rm -f "$config_file"
        echo "Configuration reset."
        return
    elif [ "$1" = "--venv" ] && [ -n "$2" ]; then
        echo "$2" > "$config_file"
        echo "Environment name '$2' saved."
        return
    elif [ "$1" = "--remove" ]; then
        sed -i '/function venvat()/,/^}/d' ~/.bashrc
        echo "venvat function removed from shell configuration. To save changes, run 'source ~/.bashrc'."
        return
    elif [[ "$1" =~ ^-- ]]; then
        echo "Invalid command '$1'. For more info, use: venvat --help"
        return
    fi

    if [ -f "$config_file" ]; then
        venv_name=$(cat "$config_file")
        echo "Using saved environment: '$venv_name'."
    else
        venv_name="venv"
        echo "No environment name provided, using default 'venv'."
    fi

    venv_path="./$venv_name/bin/activate"

    if [ -f "$venv_path" ]; then
        echo "Activating virtual environment '$venv_name'..."
        source "$venv_path"
    else
        echo "Virtual environment not found. Ensure it is created and available at $venv_path."
    fi
}
"""
    else:
        return """
function venvat() {
    # Venvat: Activate Python virtual environments
    local config_file="venvat.config"

    if [[ "$1" == "--help" ]]; then
        echo "Usage: venvat [--venv your-env-name] [--reset] [--remove]"
        echo "Venvat will consider 'venv' as your virtual environment name by default."
        echo "Use '--venv VENV_NAME' to specify the name of your virtual environment."
        echo "Use '--reset' to clear the stored virtual environment configuration."
        echo "Use '--remove' to remove the venvat function from the shell configuration."
        return
    elif [[ "$1" == "--reset" ]]; then
        rm -f "$config_file"
        echo "Configuration reset."
        return
    elif [[ "$1" == "--venv" ]] && [[ -n "$2" ]]; then
        local venv_name="$2"
        echo "$venv_name" > "$config_file"
        echo "Environment name '$venv_name' saved."
        return
     elif [[ "$1" == "--remove" ]]; then
        local shell_rc="$HOME/.zshrc"
        if [[ $(uname) == "Darwin" ]]; then
            sed -i '' '/function venvat()/,/^}/d' "$shell_rc"
        else
            sed -i '/function venvat()/,/^}/d' "$shell_rc"
        fi
        echo "venvat function removed from shell configuration. To save changes, run 'source $shell_rc'."
        return
    elif [[ "$1" =~ ^-- ]]; then
        echo "Invalid command '$1'. For more info, use: venvat --help"
        return
    fi

    if [[ -f "$config_file" ]]; then
        local venv_name=$(<"$config_file")
        echo "Using saved environment: '$venv_name'."
    else
        local venv_name="venv"
        echo "No environment name provided, using default 'venv'."
    fi

    local venv_path="./$venv_name/bin/activate"

    if [[ -f "$venv_path" ]]; then
        echo "Activating virtual environment '$venv_name'..."
        source "$venv_path"
    else
        echo "Virtual environment not found. Ensure it is created and available at $venv_path."
    fi
}
"""

def modify_shell_config():
    rc_file = get_rc_file()
    if not rc_file:
        return

    if not is_function_present(rc_file):
        with open(rc_file, "a") as f:
            f.write("\n" + get_venvat_function(rc_file))
            print(f"Added venvat function to {rc_file}")
    else:
        print(f"venvat function is already present in {rc_file}")
        
def is_function_present(rc_file):
    if not os.path.exists(rc_file):
        return False

    with open(rc_file, "r") as f:
        content = f.read()
        return "function venvat()" in content

rc_file = get_rc_file()
def run_venvat_script(venv_name=None, help_flag=False, reset_flag=False, remove_flag=False):
    if is_windows():
        script_path = os.path.join(sys.prefix, 'Scripts', 'venvat.ps1')
        if not os.path.exists(script_path):
            print(f"Error: venvat script not found at {script_path}")
            return

        command = ['powershell.exe', script_path]

        if help_flag:
            command.append("--help")
        elif reset_flag:
            command.append("--reset")
        elif venv_name:
            command.append(f"--venv {venv_name}")
        elif remove_flag:
            print("This command are only available for Linux and MacOS.")

        try:
            subprocess.call(command, shell=False)
        except Exception as e:
            print(f"Failed to execute venvat script: {e}")
    elif ".bashrc" in rc_file:
        print("venvat function is ready to use. Please run 'source ~/.bashrc' to apply changes.")
    else:
        print("venvat function is ready to use. Please run 'source ~/.zshrc' to apply changes.")

def main():
    parser = argparse.ArgumentParser(description="Activate a Python virtual environment easily.")
    parser.add_argument('--remove', action='store_true', help='Remove the venvat function from the shell configuration for Linux and MacOS only')
    parser.add_argument('--venv', type=str, help='Specify the virtual environment to activate')
    parser.add_argument('--reset', action='store_true', help='Reset the venvat configuration')

    args = parser.parse_args()

    if not is_windows():
        modify_shell_config()
    
    if args.remove:
        run_venvat_script(remove_flag=True)
    elif args.reset:
        run_venvat_script(reset_flag=True)
    elif args.venv:
        run_venvat_script(venv_name=args.venv)
    else:
        run_venvat_script()

if __name__ == "__main__":
    main()
