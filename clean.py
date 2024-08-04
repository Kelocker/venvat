import shutil
import os

# Directories to clean
directories = ['dist', 'build', '.egg-info']

for dir_name in directories:
    for item in os.listdir('.'):
        if dir_name in item:
            print(f"Removing {item}")
            shutil.rmtree(item, ignore_errors=True)
