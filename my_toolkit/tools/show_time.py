from datetime import datetime
from pathlib import Path
import time
import shutil
from rich.console import Console
from rich.table import Table
import psutil
from iterfzf import iterfzf
from yaspin import yaspin

from my_toolkit.utils.cli_utils import info, success, warning

def run():
    info(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def sys():
    console = Console()
    table = Table(title="Jarvic Tool - System Info")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("CPU Usage", f"{psutil.cpu_percent()}%")
    table.add_row("Memory", f"{psutil.virtual_memory().percent}%")
    console.print(table)

def scan_select(path):
    """Scan a directory and select files with fzf."""
    with yaspin(text=f"Scanning {path}...", color="cyan") as spinner:
        time.sleep(1)
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
        warning("No files to select in the current directory.")
        return

    selected = iterfzf(files, prompt="Jarvic Select> ", preview=preview_cmd)
    if selected:
        success(f"Selected: {selected}")
    else:
        warning("No file selected")
