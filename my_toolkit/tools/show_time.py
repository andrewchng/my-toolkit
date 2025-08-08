
from datetime import datetime

from my_toolkit.utils.print_utils import info

def run():
    info(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
