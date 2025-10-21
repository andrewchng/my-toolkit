# Agent Guidelines for my-toolkit

## Build/Lint/Test Commands

### Building
- `uv build` - Build the package
- `uv run python -m build` - Alternative build command

### Testing
- No testing framework currently configured
- Run individual test: `uv run python -m pytest my_toolkit/tests/test_core.py::test_show_landing -v`
- Run all tests: `uv run python -m pytest` (requires pytest to be added to dependencies)

### Linting & Type Checking
- `uv run pyright` - Type checking with pyright
- No linters currently configured (consider adding ruff/black)

## Code Style Guidelines

### Imports
- Standard library imports first
- Third-party imports second
- Local imports last
- Use absolute imports for local modules
- Group imports with blank lines between groups

### Naming Conventions
- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

### Type Hints
- Use type hints for all function parameters and return values
- Use `typing` module for complex types (Dict, List, Optional, etc.)
- Use `Path` from `pathlib` for file paths

### Error Handling
- Use try/except blocks for expected errors
- Catch specific exceptions rather than bare `except`
- Use `pathlib.Path` for file operations
- Handle `FileNotFoundError` for missing config files

### Code Structure
- Use docstrings for classes and public methods
- Follow single responsibility principle for functions
- Use abstract base classes for tool interfaces
- Keep functions under 50 lines when possible

### CLI Output
- Use `rich` for formatted console output
- Use `InquirerPy` for interactive prompts
- Follow existing CLI patterns in `cli_utils.py`

### Dependencies
- Check existing dependencies before adding new ones
- Use `uv` for dependency management
- Prefer well-maintained, popular libraries