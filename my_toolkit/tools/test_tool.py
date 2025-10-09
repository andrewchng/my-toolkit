from .base_tool import Tool
from my_toolkit.utils.cli_utils import info


class TestTool(Tool):
    name = "test_tool"
    description = "A tool for testing purposes."

    def run(self) -> None:
        info("TestTool is running...")
        pass

    def help(self) -> str:
        return "This is a test tool for demonstration purposes."
