# Core CLI logic for landing page and menu

from InquirerPy import inquirer

def show_landing():
    from tools import show_time, echo_input
    ascii_art = r"""
   ____            _                 _                 _ _         _   _           _ _     _            
  |  _ \  ___  ___| |_ ___  _ __ ___| |__   ___   ___ | (_) ___   | | | |_ __   __| (_)___| |_ ___ _ __ 
  | | | |/ _ \/ __| __/ _ \| '__/ _ \ '_ \ / _ \ / _ \| | |/ _ \  | | | | '_ \ / _` | / __| __/ _ \ '__|
  | |_| |  __/\__ \ || (_) | | |  __/ |_) | (_) | (_) | | |  __/  | |_| | |_) | (_| | \__ \ ||  __/ |   
  |____/ \___||___/\__\___/|_|  \___|_.__/ \___/ \___/|_|_|\___|   \___/| .__/ \__,_|_|___/\__\___|_|   
                                                                       |_|                              
"""
    while True:
        print(ascii_art)
   
        choice = inquirer.select(
            message="Choose an option:",
            choices=[
                {"name": "Show current time", "value": "show_time"},
                {"name": "Echo input", "value": "echo_input"},
                {"name": "Exit", "value": "exit"}
            ],
            default="show_time"
        ).execute()
        if choice == "show_time":
            show_time.run()
        elif choice == "echo_input":
            echo_input.run()
        elif choice == "exit":
            print("Goodbye!")
            exit(0)
