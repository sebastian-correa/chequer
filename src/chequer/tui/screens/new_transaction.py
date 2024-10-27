"""A screen that allows the user to add new instruments to the system."""

from chequer.tui.screens.utils import UnderConstrucionScreen


class NewTransactionScreen(UnderConstrucionScreen):
    """Create a new transaction, comprised of multiple instruments.

    The user can add, remove, and edit instruments in the transaction.
    """

    SUB_TITLE = "Crear una nueva transacción."
