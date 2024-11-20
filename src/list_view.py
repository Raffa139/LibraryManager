class ListView:
    def __init__(self, books):
        self.books = books

    def show(self):
        for book in self.books:
            print(book)
