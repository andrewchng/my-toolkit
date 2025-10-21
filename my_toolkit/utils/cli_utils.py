import shutil
from pathlib import Path

from iterfzf import iterfzf
from rich.console import Console
from rich.markup import escape
from yaspin import yaspin

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


def spinner(func, *args, **kwargs):
    """
    Runs a function with a yaspin spinner loader.

    Args:
        func: The function to execute with the spinner
        *args: Positional arguments to pass to func
        **kwargs: Keyword arguments to pass to func

    Usage:
        spinner(my_func, arg1, arg2, kwarg1=val)
    """
    text = "Loading"
    color = "cyan"
    success_msg = "✔ Done"
    fail_msg = "✗ Error"
    try:
        with yaspin(color=color) as spinner:
            result = func(*args, **kwargs)
            spinner.ok(success_msg)
            return result
    except Exception as e:
        with yaspin(text=text, color="red") as spinner:
            spinner.fail(fail_msg)
        raise e


def scan_select(path):
    """Scan a directory and select files with fzf."""
    with yaspin(text=f"Scanning {path}...", color="cyan") as spinner:
        files = [str(item) for item in Path(path).iterdir() if item.is_file()]
        spinner.ok(f"✔ Found {len(files)} files")

    # Check for bat and set preview command
    if shutil.which("bat"):
        preview_cmd = "bat --color=always --plain {}"
    elif shutil.which("cat"):
        preview_cmd = "cat {}"
    else:
        preview_cmd = None  # No preview if neither bat nor cat is available

    if not files:
        return

    selected = iterfzf(files, prompt="Jarvic Select> ", preview=preview_cmd)
    if selected:
        success(f"Selected: {selected}")
    else:
        warning("No file selected")
