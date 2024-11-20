import repository as repo

from book import Book, Title, Author, PublicationYear
from menu import MenuException
from value import InvalidValueException


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
