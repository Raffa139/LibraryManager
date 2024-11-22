class Book:
    def __init__(self, title, author, year, borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.borrowed = borrowed

    def borrow(self):
        """
        Mark the book as borrowed.
        """
        self.borrowed = True

    def give_back(self):
        """
        Mark the book as returned.
        :return:
        """
        self.borrowed = False

    def __str__(self):
        return f"{'[x]' if self.borrowed else '[v]'} {self.title} by {self.author} from {self.year}"
