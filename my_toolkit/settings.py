import os
from pathlib import Path
from typing import Any, Dict, Optional

import tomli
import tomli_w

from my_toolkit.utils.cli_utils import info

DEFAULT_CONFIG = {
    "general": {
        "verbose": False,
    },
    "tools": {
        "unzip": {
            "default_output_dir": "unzipped",
            "overwrite_existing": False,
        },
        "github" : {
            "pat_token" : ""
        }
    },
}


class Settings:
    def __init__(self):
        self._config: Dict[str, Any] = {}
        self._config_path = self._get_config_path()
        self.load_config()

    def _get_config_path(self) -> Path:
        """Get the configuration file path."""
        xdg_config_home = os.environ.get(
            "XDG_CONFIG_HOME", str(Path.home() / ".config")
        )
        config_dir = Path(xdg_config_home) / "jarvix"
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / "config.toml"

    def create_config(self) -> None:
        """Create a new configuration file with default values."""
        self._config = DEFAULT_CONFIG.copy()
        self.save_config()

    def load_config(self) -> None:
        """Load configuration from file or create default if not exists."""
        try:
            with open(self._config_path, "rb") as f:
                self._config = tomli.load(f)
        except FileNotFoundError:
            self.create_config()

    def save_config(self) -> None:
        """Save current configuration to file."""
        with open(self._config_path, "wb") as f:
            tomli_w.dump(self._config, f)

    def get(self, section: str, key: str, default: Any = None) -> Any:
        """Get a configuration value by section and key."""
        try:
            return self._config[section][key]
        except KeyError:
            return default

    def set(self, section: str, key: str, value: Any) -> None:
        """Set a configuration value by section and key."""
        if section not in self._config:
            self._config[section] = {}
        self._config[section][key] = value
        self.save_config()

    def get_section(self, section: str) -> Optional[Dict[str, Any]]:
        """Get an entire configuration section."""
        return self._config.get(section)

    def reset_to_defaults(self) -> None:
        """Reset configuration to default values."""
        self._config = DEFAULT_CONFIG.copy()
        self.save_config()

    @property
    def config_path(self) -> Path:
        """Get the path to the configuration file."""
        return self._config_path

