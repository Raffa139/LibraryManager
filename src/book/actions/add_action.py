import src.shared.cli as cli
import src.book.repository as repo

from src.book.actions.list_action import ListAction
from src.book.author import Author
from src.book.book import Book
from src.book.publication_year import PublicationYear
from src.book.title import Title
from src.menu.actions.close_menu_action import CloseMenuAction
from src.menu.menu import Menu
from src.menu.menu_exception import MenuException
from src.menu.actions.rerun_action import RerunAction
from src.shared.value import InvalidValueException


class AddAction:
    def run(self, menu):
        cli.write_str("Add book:")

        try:
            title = Title(cli.read_str("Title: "))
            author = Author(cli.read_str("Author: "))
            year = PublicationYear(cli.read_str("Year: "))
        except InvalidValueException as e:
            invalid_value = f"'{e.value}'" if e.value else None
            details = f"Invalid value {f'{invalid_value} ' if invalid_value else ''}for {e.obj_name} given."

            raise MenuException(f"Failed to create book. {details}")

        book = Book(title, author, year)
        repo.instance().add(book)

        next_steps_menu = Menu("=== Next steps ===", on_error=menu.on_error, subtitle="Book added successfully.")
        next_steps_menu.register_cmd("1", "Add another book", RerunAction(rerun_on=menu))
        next_steps_menu.register_cmd("2", "List all books", ListAction())
        next_steps_menu.register_cmd("0", "Home", CloseMenuAction())

        next_steps_menu.take_single_cmd()
