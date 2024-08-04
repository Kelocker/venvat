import os

def read_version():
    with open("VERSION") as version_file:
        return version_file.read().strip()

def update_pyproject_version(version):
    with open("pyproject.toml", "r") as file:
        lines = file.readlines()

    with open("pyproject.toml", "w") as file:
        for line in lines:
            if line.startswith("version ="):
                file.write(f'version = "{version}"\n')
            else:
                file.write(line)

if __name__ == "__main__":
    version = read_version()
    update_pyproject_version(version)
