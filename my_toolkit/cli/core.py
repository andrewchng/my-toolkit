# Core CLI logic for landing page and menu


from time import sleep
from InquirerPy import inquirer

from my_toolkit.tools import echo_input, show_time, unzip_files
from my_toolkit.utils.print_utils import info, success, title, with_spinner
from rich.console import Console

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
        while True:
            info(f"Version: {version}")
            choice = inquirer.select(
                message="Choose an option: [↑/↓] Navigate  [Enter] Confirm  [Esc] Cancel",
                choices=[
                    {"name": "Show current cpu usage", "value": "show_cpu"},
                    {"name": "JARVIX", "value": "print_title"},
                    {"name": "Unzip files", "value": "unzip_files"},
                    {"name": "Fake task with spinner", "value": "fake_task"},
                    {"name": "Exit", "value": "exit"},
                ],
                default="show_time"
            ).execute()
            if choice == "show_cpu":
                with_spinner(show_time.sys)
            elif choice == "print_title":
                with_spinner(title, ascii_art)
            elif choice == "unzip_files":
                with_spinner(
                    unzip_files.run()
                )
            elif choice == "fake_task":
                with_spinner(fake_task)
            elif choice == "exit":
                success("Goodbye!")
                exit(0)
    except KeyboardInterrupt:
        success("Exited by user (Ctrl+C)")
        exit(0)

def fake_task():
    sleep(4)  # Simulate work

