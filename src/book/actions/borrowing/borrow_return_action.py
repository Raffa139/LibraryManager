from src.book.actions.borrowing.borrow_action import BorrowAction
from src.book.actions.borrowing.return_action import ReturnAction
from src.menu.actions.close_menu_action import CloseMenuAction
from src.menu.menu import Menu


class BorrowReturnAction:
    def run(self, menu):
        borrow_return_menu = Menu("Borrow / Return", on_error=menu.on_error)
        borrow_return_menu.register_cmd("1", "Borrow", BorrowAction())
        borrow_return_menu.register_cmd("2", "Return", ReturnAction())
        borrow_return_menu.register_cmd("0", "Home", CloseMenuAction())

        borrow_return_menu.take_cmd_until_close()
