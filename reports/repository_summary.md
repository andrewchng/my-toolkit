# Repository Summary: my-toolkit

## Overview
`my-toolkit` is a Python-based CLI tool designed to enhance developer productivity. It provides a foundation for building interactive command-line tools and comes with a set of built-in utilities. The main entry point for the CLI is the command `jarvix`.

## Architecture
The project follows a modular structure:
- **CLI Entry Point:** `my_toolkit/cli/core.py` handles the main execution flow.
- **Tool System:** Tools are implemented as classes inheriting from a `Tool` abstract base class (`my_toolkit/tools/base_tool.py`), ensuring a consistent interface (`run` and `help` methods).
- **Configuration:** A `Settings` class (`my_toolkit/settings.py`) manages persistent configuration.
- **Utilities:** Helper functions for CLI interaction (spinners, success messages) are located in `my_toolkit/utils/cli_utils.py`.

## Key Features & Tools
The repository currently includes the following tools:

1.  **GitHub Tool (`my_toolkit/tools/github.py`)**:
    -   Allows users to authenticate with a Personal Access Token (PAT).
    -   Provides functionality to list and clone repositories from the authenticated user's GitHub account.
    -   Uses `PyGithub` for API interaction and `GitPython` for cloning.

2.  **Unzip Files (`my_toolkit/tools/unzip_files.py`)**:
    -   (Inferred) A utility to unzip files.

3.  **Show Time (`my_toolkit/tools/show_time.py`)**:
    -   (Inferred) A simple utility to display the current time.

4.  **Test Tool (`my_toolkit/tools/test_tool.py`)**:
    -   Likely a placeholder or example tool for testing the framework.

## Dependencies
The project relies on several key libraries:
-   **Interaction:** `InquirerPy` (prompts), `rich` (formatted output), `yaspin` (loading spinners), `iterfzf` (fuzzy finding).
-   **System/Core:** `click` (CLI framework), `psutil` (system monitoring), `tomli`/`tomli-w` (TOML parsing).
-   **External Services:** `PyGithub` (GitHub API), `GitPython` (Git operations).

## Installation & Usage
The tool is designed to be installed via `pipx`:
```bash
pipx install git+https://github.com/andrewchng/my-toolkit.git
```
Once installed, the CLI can be launched using the `jarvix` command.
