"""Main menu screen."""

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from chequer.branding import ascii_brand, tag_line


class MainMenu(Screen):
    """Main menu screen."""

    SUB_TITLE = "Menú Principal"

    def compose(self) -> ComposeResult:
        """Compose the screen."""
        yield Header()

        with Horizontal(classes="main-menu"):
            with Vertical(classes="buttons-panel"):
                yield Button("Nueva Operación", id="new-transaction")
                yield Button("Buscar Operaciones", id="search")
                yield Button("Próximos vencimientos", id="upcoming")

            with Vertical(classes="branding-container"):
                yield Static(ascii_brand, classes="branding-logo")
                yield Static(tag_line, classes="branding-subtitle")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Go to the screen indicated by `event.button.id`."""
        if event.button.id is None:
            message = "Pressed button has no id."
            raise ValueError(message)

        self.app.push_screen(event.button.id)
