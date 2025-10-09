from abc import ABC, abstractmethod


class Tool(ABC):
    """Base class for all tools."""

    @abstractmethod
    def run(self, *args, **kwargs):
        """Run the tool."""
        pass

    @abstractmethod
    def help(self) -> str:
        """Return a help string for the tool."""
        pass
