import src.shared.cli as cli

from src.menu.menu import Menu
from src.menu.close_menu_action import CloseMenuAction


class ErrorAction:
    def run(self, menu, exception):
        error_menu = Menu("=== An error occurred ===")
        error_menu.register_cmd("1", "Retry", None)
        error_menu.register_cmd("2", "Home", CloseMenuAction())

        while not error_menu.close_requested:
            cli.write_str(exception.message)

            if error_menu.take_cmd():
                break
