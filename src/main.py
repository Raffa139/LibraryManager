import src.book.repository as repo

from src.book.actions.borrowing.borrow_return_action import BorrowReturnAction
from src.menu.actions.error_action import ErrorAction
from src.menu.menu import Menu
from src.book.actions.add_action import AddAction
from src.book.actions.list_action import ListAction
from src.book.actions.search.search_action import SearchAction
from src.save_exit_action import SaveExitAction

book_repo = repo.instance()

menu = Menu("Library Manager", on_error=ErrorAction())

menu.register_cmd("1", "Add book", AddAction())
menu.register_cmd("2", "List all books", ListAction())
menu.register_cmd("3", "Search books", SearchAction())
menu.register_cmd("4", "Borrow/Return book", BorrowReturnAction())
menu.register_cmd("5", "Save and exit", SaveExitAction())

menu.take_cmd_until_close()
