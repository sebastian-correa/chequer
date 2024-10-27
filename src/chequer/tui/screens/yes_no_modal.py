"""A modal pop up screen to confirm quitting the app."""

from collections.abc import Callable
from typing import Any, Literal, cast

from textual.app import ComposeResult
from textual.containers import Grid
from textual.widgets import Button, Label

from chequer.tui.screens.utils import SelfClosingModalScreen

YES_NO = Literal["yes", "no"]


class YesNoModal(SelfClosingModalScreen):
    """A modal screen with a yes and no button."""

    CSS_PATH = "yes_no_modal.tcss"

    def __init__(
        self,
        question: str,
        action_yes: Callable,
        action_no: Callable,
        *,
        dangerous_option: YES_NO = "yes",
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.question = question
        self._dangerous_option = dangerous_option
        self._safe_option = "no" if dangerous_option == "yes" else "yes"

        self._button_variants: dict[YES_NO, Literal["error", "primary"]] = {
            self._dangerous_option: "error",
            self._safe_option: "primary",
        }

        self._actions: dict[YES_NO, Callable] = {
            "yes": action_yes,
            "no": action_no,
        }

    def compose(self) -> ComposeResult:
        """Build the modal dialog."""
        with Grid(id="dialog"):
            yield Label(self.question, id="question")
            yield Button("Si", variant=self._button_variants["yes"], id="yes")
            yield Button("No", variant=self._button_variants["no"], id="no")

    def on_mount(self) -> None:
        """Set focus on the safe button."""
        cancel_button = self.query_one(f"#{self._safe_option}", Button)
        cancel_button.focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        self._actions[cast(YES_NO, event.button.id)]()
