import src.shared.file as f

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
        lines = [self._serialize(book) for book in books]
        return "\n".join(lines)

    def deserialize(self, data):
        lines = f.rm_empty_lines(data)
        return [self._deserialize(line) for line in lines]

    def _serialize(self, book):
        available = "1" if book.borrowed else "0"
        return f"{book.title},{book.author},{book.year},{available}"

    def _deserialize(self, data):
        book_parts = data.split(",")

        title = book_parts[SER_IDX_TITLE]
        author = book_parts[SER_IDX_AUTHOR]
        year = book_parts[SER_IDX_YEAR]
        borrowed = book_parts[SER_IDX_BORROWED]

        return Book(Title(title), Author(author), PublicationYear(year), bool(int(borrowed)))
