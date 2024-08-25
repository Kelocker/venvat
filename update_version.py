import os

def read_version():
    """Reads the version number from a VERSION file."""
    with open("VERSION") as version_file:
        version = version_file.read().strip()
    print(f"Read version: {version}")
    return version

def update_setuppy_version(version):
    """Updates the version number in setup.py."""
    updated = False
    with open("setup.py", "r") as file:
        lines = file.readlines()

    with open("setup.py", "w") as file:
        for line in lines:
            if "version=" in line:
                file.write(f"    version='{version}',\n")
                updated = True
            else:
                file.write(line)
    return updated

if __name__ == "__main__":
    version = read_version()
    if update_setuppy_version(version):
        print(f"setup.py has been successfully updated to version {version}.")
    else:
        print("No version update required in setup.py.")
