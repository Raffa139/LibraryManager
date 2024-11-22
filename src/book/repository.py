import src.file as f


class Repository:
    def __init__(self, *, file, serializer):
        self.file = file
        self.serializer = serializer
        self.books = []
        self.load_from_disk()

    def find_borrowed(self):
        """
        Finds all books wich are currently marked as borrowed.
        :return: A list of borrowed books
        """
        return [book for book in self.books if book.borrowed]

    def find_available(self):
        """
        Finds all books which are currently marked as available.
        :return: A list of available books
        """
        return [book for book in self.books if not book.borrowed]

    def find_by_title(self, title):
        """
        Finds all books of which the given title is a substring of the books title.
        :param title: The title to search for
        :return: A list of books matching part of the title
        """
        return [book for book in self.books if book.title.value.lower().find(title.lower()) != -1]

    def find_by_author(self, author):
        """
        Finds all books of which the given author is a substring of the books author name.
        :param author: The author to search for
        :return: A list of books matching part of the author
        """
        return [book for book in self.books if book.author.value.lower().find(author.lower()) != -1]

    def find_by_keyword(self, keyword):
        return [book for book in self.books if keyword.lower() in book.keyword_strs_lower()]

    def add(self, book):
        """
        Adds a book to the library.
        :param book: The book to add
        """
        self.books.append(book)

    def load_from_disk(self):
        """
        Reads the content of file and uses the serializer to deserialize its contents.
        Nothing will be done if the file does not exist.
        """
        try:
            content = f.read(self.file)
            self.books = self.serializer.deserialize(content)
        except FileNotFoundError:
            pass  # Ignored: will be created on exit

    def save_to_disk(self):
        """
        Serialize the books using the serializer and write the serialized content to the file.
        File will be created if not yet existing.
        Nothing will be done if no books are stored.
        :return:
        """
        if len(self.books) == 0:
            return

        content = self.serializer.serialize(self.books)
        f.write(self.file, content)
