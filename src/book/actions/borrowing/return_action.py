import src.book.repository as repo

from src.book.actions.borrowing.return_selection_action import ReturnSelectionAction
from src.menu.close_menu_action import CloseMenuAction
from src.menu.menu import Menu


class ReturnAction:
    def run(self, menu):
        borrowed_books = repo.instance().find_borrowed()

        return_menu = Menu("=== Select book ===", on_error=menu.on_error)

        for i in range(len(borrowed_books)):
            book = borrowed_books[i]
            return_menu.register_cmd(str(i + 1), book.title, ReturnSelectionAction(book))

        return_menu.register_cmd("0", "Back", CloseMenuAction())

        return_menu.take_single_cmd()
