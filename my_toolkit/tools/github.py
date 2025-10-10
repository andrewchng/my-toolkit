
from my_toolkit.tools.base_tool import Tool
from my_toolkit.utils.cli_utils import info

class GithubTool(Tool):

    def run(self):
        info("HELLO WORLD FROM GITHUB TOOL")

    def help(self):
        return ""

