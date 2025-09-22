import json
import shutil
import os

def load_json(file_path):
    """Load data from JSON file."""
    with open(file_path) as f:
        data = json.load(f)
    return data

def clear_directory(directory):
    """Clear the contents of the given directory."""
    if os.path.exists(directory):
        # Remove all files and subdirectories in the directory
        shutil.rmtree(directory)
    os.makedirs(directory)


def copy_folder(src, dst):
    shutil.copytree(src, dst, True)