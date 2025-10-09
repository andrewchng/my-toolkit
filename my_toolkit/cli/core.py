# Core CLI logic for landing page and menu

from pathlib import Path
from time import sleep
from InquirerPy.prompts.list import ListPrompt
from InquirerPy.prompts.fuzzy import FuzzyPrompt
from InquirerPy.prompts.input import InputPrompt
from InquirerPy.separator import Separator

from my_toolkit.tools import show_time, unzip_files
from my_toolkit.utils.cli_utils import info, success, title, with_spinner
from my_toolkit.settings import Settings

# Initialize settings
settings = Settings()

def show_landing():
    ascii_art = r"""
__________________________    ____________  __
______  /__    |__  __ \_ |  / /___  _/_  |/ /
___ _  /__  /| |_  /_/ /_ | / / __  / __    / 
/ /_/ / _  ___ |  _, _/__ |/ / __/ /  _    |  
\____/  /_/  |_/_/ |_| _____/  /___/  /_/|_|  
                                                                    
"""
    version = "0.1.0"  # Sync with pyproject.toml
    title(ascii_art)
    # `InquirerPy.inquirer` exposes prompts dynamically; alias as Any for type-checkers
    try:
        while True:
            info(f"Version: {version}")
            choice = FuzzyPrompt(
                message="Search and choose an option: [Type to search]  [Enter] Confirm  [Esc] Cancel",
                choices=[
                    {"name": "Show current cpu usage", "value": "show_cpu"},
                    {"name": "JARVIX", "value": "print_title"},
                    {"name": "Unzip files", "value": "unzip_files"},
                    {"name": "Fake task with spinner", "value": "fake_task"},
                    # Separator(""),
                    {"name": "Settings", "value": "settings"},
                    {"name": "Exit", "value": "exit"},
                ],
                default=""
            ).execute()
            if choice == "show_cpu":
                with_spinner(show_time.sys)
            elif choice == "print_title":
                with_spinner(title, ascii_art)
            elif choice == "unzip_files":
                unzip_files.run()
            elif choice == "fake_task":
                show_time.scan_select(path=Path.cwd())
            elif choice == "settings":
                manage_settings()
            elif choice == "exit":
                if settings.get("general", "confirm_exit", True):
                    confirm = ListPrompt(
                        message="Are you sure you want to exit?",
                        choices=[
                            {"name": "Yes", "value": True},
                            {"name": "No", "value": False}
                        ]
                    ).execute()
                    if not confirm:
                        continue
                success("Goodbye!")
                exit(0)
    except KeyboardInterrupt:
        success("\nExited by user (Ctrl+C)")
        exit(0)

def manage_settings():
    """Manage application settings."""
    while True:
        choice = ListPrompt(
            message="Settings menu: [↑/↓] Navigate  [Enter] Confirm  [Esc] Back",
            choices=[
                {"name": "View all settings", "value": "view"},
                {"name": "Edit setting", "value": "edit"},
                {"name": "Reset to defaults", "value": "reset"},
                {"name": "Back to main menu", "value": "back"},
            ]
        ).execute()

        if choice == "view":
            title("Current Settings:")
            for section, values in settings._config.items():
                info(f"\n[{section}]")
                for key, value in values.items():
                    info(f"{key} = {value}")
        
        elif choice == "edit":
            # Select section
            sections = list(settings._config.keys())
            section = ListPrompt(
                message="Select section to edit:",
                choices=[{"name": s, "value": s} for s in sections]
            ).execute()
            
            # Select key
            keys = list(settings._config[section].keys())
            key = ListPrompt(
                message="Select setting to edit:",
                choices=[{"name": k, "value": k} for k in keys]
            ).execute()
            
            # Get current value type
            current_value = settings.get(section, key)
            if isinstance(current_value, bool):
                new_value = ListPrompt(
                    message=f"Set {key}:",
                    choices=[
                        {"name": "True", "value": True},
                        {"name": "False", "value": False}
                    ]
                ).execute()
            else:
                new_value = InputPrompt(
                    message=f"Enter new value for {key}:",
                    default=str(current_value)
                ).execute()
                # Convert to appropriate type
                if isinstance(current_value, int):
                    new_value = int(new_value)
                elif isinstance(current_value, float):
                    new_value = float(new_value)
            
            settings.set(section, key, new_value)
            success(f"Updated {section}.{key} to {new_value}")
        
        elif choice == "reset":
            confirm = ListPrompt(
                message="Are you sure you want to reset all settings to defaults?",
                choices=[
                    {"name": "Yes", "value": True},
                    {"name": "No", "value": False}
                ]
            ).execute()
            if confirm:
                settings.reset_to_defaults()
                success("Settings reset to defaults")
        
        elif choice == "back":
            break
def fake_task():
    sleep(4)  # Simulate work
