import src.book.repository as repo

from src.book.author import Author
from src.book.book import Book
from src.book.publication_year import PublicationYear
from src.book.title import Title
from src.menu.error_action import ErrorAction
from src.menu.menu import Menu
from src.book.actions.add_action import AddAction
from src.book.actions.list_action import ListAction
from src.book.actions.search_action import SearchAction
from src.menu.close_menu_action import CloseMenuAction

# print("=== Library Manager ===")
# print("1. Add book")
# print("2. List all books")
# print("3. Search books")
# print("4. Borrow/Return book")
# print("5. Save and exit")

book_repo = repo.instance((
    Book(Title("Musterbuch"), Author("Max Muster"), PublicationYear("2000")),
    Book(Title("Das Buch"), Author("Artur Author"), PublicationYear("2020")),
    Book(Title("Physik für Einsteiger"), Author("Albert Einstein"), PublicationYear("1975")),
))

menu = Menu("=== Library Manager ===", on_error=ErrorAction())

menu.register_cmd("1", "Add book", AddAction())
menu.register_cmd("2", "List all books", ListAction())
menu.register_cmd("3", "Search books", SearchAction())
menu.register_cmd("5", "Save and exit", CloseMenuAction())

menu.take_cmd_until_close()
