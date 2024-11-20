import src.cli as cli
import src.book.repository as repo

from src.book.author import Author
from src.book.book import Book
from src.book.publication_year import PublicationYear
from src.book.title import Title
from src.menu.menu_exception import MenuException
from src.value import InvalidValueException


class AddAction:
    def run(self, menu):
        cli.write_str("Add book:")

        title_in = cli.read_str("Title: ")
        author_in = cli.read_str("Author: ")
        year_in = cli.read_str("Year: ")

        try:
            title = Title(title_in)
            author = Author(author_in)
            year = PublicationYear(year_in)
        except InvalidValueException:
            raise MenuException("Failed to created book.")

        book = Book(title, author, year)
        repo.instance().add(book)
