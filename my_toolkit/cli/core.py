# Core CLI logic for landing page and menu


from InquirerPy import inquirer

from my_toolkit.tools import echo_input, show_time, unzip_files
from my_toolkit.utils.print_utils import info, success, title
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
                    {"name": "Show current time", "value": "show_time"},
                    {"name": "Echo input", "value": "echo_input"},
                    {"name": "Unzip files", "value": "unzip_files"},
                    {"name": "Exit", "value": "exit"}
                ],
                default="show_time"
            ).execute()
            if choice == "show_time":
                info("Selected: Show current time")
                show_time.run()
            elif choice == "echo_input":
                info("Selected: Echo input")
                echo_input.run()
            elif choice == "unzip_files":
                info("Selected: Unzip files")
                unzip_files.run()
            elif choice == "exit":
                success("Goodbye!")
                exit(0)
    except KeyboardInterrupt:
        success("Exited by user (Ctrl+C)")
        exit(0)
