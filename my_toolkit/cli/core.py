# Core CLI logic for landing page and menu


from pathlib import Path
from time import sleep
from typing import Any
from InquirerPy.prompts.list import ListPrompt

from my_toolkit.tools import show_time, unzip_files
from my_toolkit.utils.print_utils import info, success, title, with_spinner

def show_landing():
    ascii_art = r"""
__________________________    ____________  __
______  /__    |__  __ \_ |  / /___  _/_  |/ /
___ _  /__  /| |_  /_/ /_ | / / __  / __    / 
/ /_/ / _  ___ |  _, _/__ |/ / __/ /  _    |  
\____/  /_/  |_/_/ |_| _____/  /___/  /_/|_|  
                                                                    
"""
    version = "0.1.0"  # Sync with pyproject.toml
    try:
        title(ascii_art)
        # `InquirerPy.inquirer` exposes prompts dynamically; alias as Any for type-checkers
        while True:
            info(f"Version: {version}")
            choice = ListPrompt(
                message="Choose an option: [↑/↓] Navigate  [Enter] Confirm  [Esc] Cancel",
                choices=[
                    {"name": "Show current cpu usage", "value": "show_cpu"},
                    {"name": "JARVIX", "value": "print_title"},
                    {"name": "Unzip files", "value": "unzip_files"},
                    {"name": "Fake task with spinner", "value": "fake_task"},
                    {"name": "Exit", "value": "exit"},
                ],
                default="show_cpu"
            ).execute()
            if choice == "show_cpu":
                with_spinner(show_time.sys)
            elif choice == "print_title":
                with_spinner(title, ascii_art)
            elif choice == "unzip_files":
                unzip_files.run()
            elif choice == "fake_task":
                show_time.scan_select(path=Path.cwd())
            elif choice == "exit":
                success("Goodbye!")
                exit(0)
    except KeyboardInterrupt:
        success("Exited by user (Ctrl+C)")
        exit(0)

def fake_task():
    sleep(4)  # Simulate work
