import src.shared.cli as cli
import src.book.repository as repo

from src.book.author import Author
from src.book.book import Book
from src.book.publication_year import PublicationYear
from src.book.title import Title
from src.menu.menu_exception import MenuException
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
