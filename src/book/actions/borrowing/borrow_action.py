import src.book.repository as repo

from src.book.actions.borrowing.borrow_selection_action import BorrowSelectionAction
from src.menu.actions.close_menu_action import CloseMenuAction
from src.menu.menu import Menu


class BorrowAction:
    def run(self, menu):
        available_books = repo.instance().find_available()

        borrow_menu = Menu("Select book", on_error=menu.on_error)

        for i in range(len(available_books)):
            book = available_books[i]
            borrow_menu.register_cmd(str(i + 1), book.title, BorrowSelectionAction(book))

        borrow_menu.register_cmd("0", "Back", CloseMenuAction())

        borrow_menu.take_single_cmd()
