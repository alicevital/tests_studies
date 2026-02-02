import os
import shutil

for root, dirs, files in os.walk(".", topdown=False):
    for d in dirs:
        if d == "__pycache__" or d == ".pytest_cache":
            full_path = os.path.join(root, d)
            shutil.rmtree(full_path, ignore_errors=True)
            print(f"Removed: {os.path.join(root, d)}")