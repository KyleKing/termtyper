"""Main application."""

from textual.app import App

from ..screens.main import Main


class TuiTyperTutor(App[None]):
    """Main Application."""

    TITLE = 'TUI Typer Tutor'

    def on_mount(self) -> None:
        """Set up the application after the DOM is ready."""
        self.push_screen(Main())
