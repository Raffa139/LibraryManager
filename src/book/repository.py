class Repository:
    instance = None

    def __init__(self, initial_date=()):
        self.books = list(initial_date)

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

    def remove(self, book):
        self.books.remove(book)

    def borrow(self, book):
        book.borrow()

    def give_back(self, book):
        book.give_back()


def instance(initial_date=()):
    if Repository.instance is None:
        Repository.instance = Repository(initial_date)

    return Repository.instance
