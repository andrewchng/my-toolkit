
from datetime import datetime
from pathlib import Path
import time
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
        files = [str(item) for item in Path(path).iterdir()]
        spinner.ok(f"✔ Found {len(files)} files")
    selected = iterfzf(files, prompt="Jarvic Select> ", preview="bat --color=always {}")
    if selected:
        success(f"Selected: {selected}")
    else:
        warning("No file selected") 
