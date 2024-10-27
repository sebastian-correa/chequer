"""General utility screens for use in the app."""

from textual.app import ComposeResult
from textual.containers import Center, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static


class UnderConstrucionScreen(Screen):
    """Screen to display a message indicating the screen is under construction."""

    CSS = """
    #content-container {
        width: 100%;
        height: 100%;
        align: center middle;
    }

    #construction-message {
        border: wide gold;
        width: auto;
        height: auto;
        padding: 1 2;
        text-align: center;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the screen."""
        yield Header()
        with Vertical(id="content-container"):
            with Center():
                yield Static(
                    ":construction: En construcción! :building_construction:",
                    id="construction-message",
                )
            with Center():
                yield Button("Menú principal", variant="primary", id="close")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "close":
            self.dismiss()
