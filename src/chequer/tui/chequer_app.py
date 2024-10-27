"""Chequer TUI app."""

from __future__ import annotations

from typing import ClassVar

from textual.app import App

from chequer.tui.screens import (
    MainMenu,
    NewTransactionScreen,
    UpcomingScreen,
    YesNoModal,
)


class ChequerApp(App):
    """Gestor de descuentos o préstamos."""

    CSS_PATH = "chequer_app.tcss"

    BINDINGS: ClassVar = [
        ("d", "toggle_dark", "Modo oscuro"),
        ("m", "goto_main_menu", "Menú principal"),
        ("q", "request_quit", "Salir"),
    ]

    SCREENS: ClassVar = {
        "main-menu": MainMenu,
        "new-transaction": NewTransactionScreen,
        "search": UpcomingScreen,
        "upcoming": UpcomingScreen,
    }

    TITLE = "Chequer"

    def action_toggle_dark(self) -> None:
        """Toggle between dark and light modes."""
        self.dark = not self.dark

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.push_screen(YesNoModal("Seguro que deseas salir?", self.exit, self.pop_screen))

    def action_goto_main_menu(self) -> None:
        """Action to display the main menu."""
        self.push_screen("main-menu")

    def on_mount(self) -> None:
        """Sets the initial status of the app."""
        self.dark = True
        self.push_screen("main-menu")
