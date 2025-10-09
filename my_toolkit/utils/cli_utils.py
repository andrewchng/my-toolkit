from rich.console import Console
from rich.markup import escape
from yaspin import yaspin
import time

console = Console()

def info(msg):
    console.print(f"[bold cyan][INFO][/bold cyan] {escape(msg)}")

def success(msg):
    console.print(f"[bold green][SUCCESS][/bold green] {escape(msg)}")

def error(msg):
    console.print(f"[bold red][ERROR][/bold red] {escape(msg)}")

def warning(msg):
    console.print(f"[bold yellow][WARNING][/bold yellow] {escape(msg)}")
    
def title(msg):
    console.print(f"[bold blue] {escape(msg)} [/bold blue]")


def with_spinner(func, *args, **kwargs):
    """
    Runs a function with a yaspin spinner loader.
    Usage:
        with_spinner(my_func, text="Working...", color="magenta", arg1, arg2, kwarg1=val)
    """
    text="Loading"
    color="cyan"
    success_msg="✔ Done"
    fail_msg="✗ Error"
    try:
        
        with yaspin(color=color) as spinner:
            result = func(*args, **kwargs)
            spinner.ok(success_msg)
            return result
    except Exception as e:
        with yaspin(text=text, color="red") as spinner:
            spinner.fail(fail_msg)
        raise e