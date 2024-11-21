from src.menu.menu import Menu
from src.menu.close_menu_action import CloseMenuAction
from src.menu.retry_action import RetryAction


class ErrorAction:
    def run(self, menu, exception):
        error_menu = Menu("=== An error occurred ===", on_error=menu.on_error, subtitle=exception.message)
        error_menu.register_cmd("1", "Retry", RetryAction(menu))
        error_menu.register_cmd("2", "Ok (Home)", CloseMenuAction())

        while not error_menu.close_requested:
            if error_menu.take_cmd():
                break
