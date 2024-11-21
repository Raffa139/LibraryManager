class BorrowSelectionAction:
    def __init__(self, book):
        self.book = book

    def run(self, menu, repo):
        self.book.borrow()
