from src.book.author import Author
from src.book.book import Book
from src.book.publication_year import PublicationYear
from src.book.title import Title

SER_IDX_TITLE = 0
SER_IDX_AUTHOR = 1
SER_IDX_YEAR = 2
SER_IDX_BORROWED = 3


class CsvSerializer:
    def serialize(self, books):
        """
        Serialize a list of book objects into comma seperated lines.
        :param books: The books
        :return: Serialized content
        """
        lines = [self._serialize(book) for book in books]
        return "\n".join(lines)

    def deserialize(self, data):
        """
        Deserialize the data into a list of book objects.
        :param data: The data
        :return: A list of book objects
        """
        lines = self._rm_empty_lines(data)
        return [self._deserialize(line) for line in lines]

    def _serialize(self, book):
        """
        Serialize a single book into a string containing the books values separated by commas.
        :param book: The book
        :return: Serialized string
        """
        available = "1" if book.borrowed else "0"
        return f"{book.title},{book.author},{book.year},{available}"

    def _deserialize(self, data):
        """
        Deserialize a comma separated string of a single book into a book object.
        :param data: The string
        :return: A book object
        """
        book_parts = data.split(",")

        title = book_parts[SER_IDX_TITLE]
        author = book_parts[SER_IDX_AUTHOR]
        year = book_parts[SER_IDX_YEAR]
        borrowed = book_parts[SER_IDX_BORROWED]

        return Book(Title(title), Author(author), PublicationYear(year), bool(int(borrowed)))

    def _rm_empty_lines(self, data):
        """
        Takes a string, separated it into lines and remove empty lines.
        For empty lines trailing whitespaces are not accounted for.
        :param data: The string
        :return: A list of non empty strings
        """
        lines = data.splitlines()
        return [line for line in lines if line.strip()]
