import src.book.repository as repo

from src.book.author import Author
from src.book.book import Book
from src.book.publication_year import PublicationYear
from src.book.title import Title
from src.menu.menu_exception import MenuException
from src.value import InvalidValueException


class AddAction:
    def run(self, menu):
        print("Add book:")

        title_in = input("Title: ")
        author_in = input("Author: ")
        year_in = input("Year: ")

        try:
            title = Title(title_in)
            author = Author(author_in)
            year = PublicationYear(year_in)
        except InvalidValueException:
            raise MenuException("Failed to created book.")

        book = Book(title, author, year)
        repo.instance().add(book)
