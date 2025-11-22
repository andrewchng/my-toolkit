from .base_tool import Tool
from my_toolkit.utils.cli_utils import info
import subprocess
import shutil

class TestTool(Tool):
    name = "test_tool"
    description = "A tool for testing purposes."

    def run(self) -> None:
        if self.check_prerequisite():
            self.run_copilot("Look through this repository and summary what it does. Write the report in reports/ folder in markdown format")

    def check_prerequisite(self) -> bool:
        if shutil.which("copilot") is None:
            info("Copilot CLI is not installed. Please install it using 'brew install github/gh/copilot' or refer to https://github.com/github/copilot-cli")
            return False
        return True

    def run_copilot(self, prompt: str) -> None:
        info(f"Running Copilot with prompt: {prompt}")
        try:
            cmd = [
                "copilot",
                "-p", prompt,
                "--allow-tool", "write",
                "--allow-tool", "shell(git)",
                "--allow-tool", "shell(touch)",
                "--allow-tool", "shell(mkdir)",
                "--allow-tool", "shell(ls)",
                "--allow-tool", "shell(cat)",
                "--allow-tool", "shell(echo)"
            ]
            subprocess.run(cmd, check=True)
        except Exception as e:
            info(f"Error running copilot: {e}")

    def help(self) -> str:
        return "This is a test tool for demonstration purposes."
