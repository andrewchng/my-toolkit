from rich.console import Console
from rich.markup import escape

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

