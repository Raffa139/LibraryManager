import src.shared.file as f

from src.book.csv_serializer import CsvSerializer


class Repository:
    instance = None

    def __init__(self, *, file, serializer):
        self.file = file
        self.serializer = serializer
        self.books = []
        self.load_from_disk()

    def find_borrowed(self):
        return [book for book in self.books if book.borrowed]

    def find_available(self):
        return [book for book in self.books if not book.borrowed]

    def find_by_title(self, title):
        return [book for book in self.books if book.title.value.lower().find(title.lower()) != -1]

    def find_by_author(self, author):
        return [book for book in self.books if book.author.value.lower().find(author.lower()) != -1]

    def add(self, book):
        self.books.append(book)

    def borrow(self, book):
        book.borrow()

    def give_back(self, book):
        book.give_back()

    def load_from_disk(self):
        try:
            content = f.read(self.file)
            self.books = self.serializer.deserialize(content)
        except FileNotFoundError:
            pass  # Ignored: will be created on exit

    def save_to_disk(self):
        if len(self.books) == 0:
            return

        content = self.serializer.serialize(self.books)
        f.write(self.file, content)


def instance():
    if Repository.instance is None:
        Repository.instance = Repository(file="library.txt", serializer=CsvSerializer())

    return Repository.instance
