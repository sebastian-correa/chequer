"""Run the Chequer application."""

from chequer.tui import ChequerApp


def main() -> None:
    """Run the Chequer TUI."""
    app = ChequerApp()
    app.run()


if __name__ == "__main__":
    main()
