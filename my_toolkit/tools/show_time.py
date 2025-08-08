
from datetime import datetime
import click
from rich.console import Console
from rich.table import Table
import psutil

from my_toolkit.utils.print_utils import info

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