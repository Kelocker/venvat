import os
import shutil

def remove_pycache(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            print(f"Removing {pycache_path}")
            shutil.rmtree(pycache_path)

if __name__ == '__main__':
    project_root = os.path.dirname(os.path.abspath(__file__))
    remove_pycache(project_root)
    print("All __pycache__ directories have been removed.")
