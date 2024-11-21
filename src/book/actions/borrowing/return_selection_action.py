class ReturnSelectionAction:
    def __init__(self, book):
        self.book = book

    def run(self, menu, repo):
        self.book.give_back()
