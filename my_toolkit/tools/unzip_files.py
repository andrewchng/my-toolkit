
import os
import zipfile
from typing import Any
from InquirerPy import inquirer
from glob import glob

from pathlib import Path
from iterfzf import iterfzf

from my_toolkit.utils.cli_utils import error, info, success, warning

paths = [
    str(Path.home() / 'Downloads'),
    str(Path.home() / 'Documents'),
    str(Path.home() / 'Desktop'),
    str(Path.home() / 'Projects'),
    str(Path.home() / 'Resources'),
    str(Path.home() / 'dotfiles'),
    os.getcwd(),
]

def run():
    # 1. Input path
    path = iterfzf(paths, prompt="Select path to search:")
    if not path:
        error("No path selected.")
        return
    
    if not os.path.isdir(path):
        error(f"Invalid directory: {path}")
        return

    # 2. Ask for recursive search (use dynamic alias to satisfy type checkers)
    inquirer_dyn: Any = inquirer
    recursive = inquirer_dyn.confirm(message="Search recursively?", default=True).execute()
    info(f"Searching for archives in: {path} (recursive: {recursive})")

    # 3. Find all .zip, .war, .jar files
    pattern = "**/*" if recursive else "*"
    extensions = [".zip", ".war", ".jar"]
    found_files = []
    for ext in extensions:
        found_files.extend(glob(os.path.join(path, pattern + ext), recursive=recursive))
    if not found_files:
        warning("No archive files found.")
        return

    # 4. Select files to unzip
    choices = [{"name": f, "value": f, "enabled": True} for f in found_files]
    selected = inquirer_dyn.checkbox(
        message="Select files to unzip: [↑/↓] Navigate  [Space] Select  [Enter] Confirm  [a] Toggle all  [Esc] Cancel",
        choices=choices,
        default=[f for f in found_files]
    ).execute()
    if not selected:
        warning("No files selected.")
        return

    # 5. Unzip selected files
    for file_path in selected:
        try:
            dest_dir = os.path.join(os.path.dirname(file_path), os.path.splitext(os.path.basename(file_path))[0] + "_unzipped")
            os.makedirs(dest_dir, exist_ok=True)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(dest_dir)
            success(f"Unzipped: {file_path} -> {dest_dir}")
        except Exception as e:
            error(f"Failed to unzip {file_path}: {e}")
