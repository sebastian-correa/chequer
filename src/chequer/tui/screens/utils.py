"""General utility screens for use in the app."""

from textual.app import ComposeResult
from textual.containers import Center, Vertical
from textual.events import Click
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Footer, Header, Static


class SelfClosingModalScreen(ModalScreen):
    """A modal screen that closes itself when the user clicks outside of it."""

    def on_click(self, event: Click) -> None:
        """Close the screen if the user clicks outside the modal.

        Args:
            event (Click): The click event.
        """
        clicked, _ = self.get_widget_at(event.screen_x, event.screen_y)
        # Note that the area outside the modal is the modal itself, while the are inside the modal
        # will usually have children widgets.
        if clicked is self:
            self.dismiss()


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
