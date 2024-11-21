import src.book.repository as repo


class ReturnSelectionAction:
    def __init__(self, book):
        self.book = book

    def run(self, menu):
        repo.instance().give_back(self.book)
