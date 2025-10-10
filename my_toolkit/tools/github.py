
from my_toolkit.settings import Settings
from my_toolkit.tools.base_tool import Tool
from my_toolkit.utils.cli_utils import info, spinner
import requests
import subprocess

from InquirerPy.prompts.secret import SecretPrompt
from InquirerPy.prompts.fuzzy import FuzzyPrompt
from InquirerPy.base.control import Choice

settings = Settings()

class GithubTool(Tool):
    name = "github"
    pat_key = "pat_token"

    def run(self):
        option = FuzzyPrompt(choices=[
                    Choice(name="List Repos", value="list_repo"),
                    Choice(name="Clone Repo", value="clone_repo"),
                    Choice(name="Settings",value="settings")
                ], message="Select tool").execute()
        
        option_map = { 
            "list_repo" : lambda : self.list_repo(),
            "clone_repo" : lambda : self.clone_repo(),
            "settings" : lambda : self.set_pat_token()
        }

        option_map[option]()

        pat = settings.get(self.name, self.pat_key)
        if pat is None or len(pat) == 0:
            self.set_pat_token()

    def help(self):
        return ""

    def set_pat_token(self):
        pat_input = SecretPrompt(message="Enter you PAT token", mandatory=True).execute()
        settings.set(self.name, self.pat_key, pat_input)
    
    def get_auth_headers(self):
        return {
            'Authorization' :  f"token {settings.get(self.name, self.pat_key)}"
        }

    def list_repo_api(self):
        response = spinner(requests.get, 'https://api.github.com/user/repos', headers=self.get_auth_headers())
        return response.json()

    def list_repo(self):
        repos = self.list_repo_api()
        if isinstance(repos, list):
            info("Clone URLs:")
            for repo in repos:
                info(repo.get('clone_url', 'N/A'))
        else:
            info(f"Error: {repos}")

    def clone_repo(self):
        repos = self.list_repo_api()

        if not isinstance(repos, list):
            info(f"Error fetching repos: {repos}")
            return

        choices = [{"name": repo['name'], "value": repo['clone_url']} for repo in repos]
        selected_url = FuzzyPrompt(
            message="Select repo to clone:",
            choices=choices
        ).execute()

        try:
            subprocess.run(['git', 'clone', selected_url], check=True)
            info(f"Cloned {selected_url}")
        except subprocess.CalledProcessError as e:
            info(f"Failed to clone: {e}")

