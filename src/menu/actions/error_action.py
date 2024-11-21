from src.menu.menu import Menu
from src.menu.actions.close_menu_action import CloseMenuAction
from src.menu.actions.rerun_action import RerunAction


class ErrorAction:
    def run(self, menu, repo, exception):
        error_menu = Menu("An error occurred", repo=repo, on_error=menu.on_error, subtitle=exception.message)
        error_menu.register_cmd("1", "Retry", RerunAction(rerun_on=menu))
        error_menu.register_cmd("0", "Ok (Home)", CloseMenuAction())

        error_menu.take_single_cmd()
