import src.book.repository as repo


class BorrowSelectionAction:
    def __init__(self, book):
        self.book = book

    def run(self, menu):
        repo.instance().borrow(self.book)
