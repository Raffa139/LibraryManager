class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.borrowed = False

    def borrow(self):
        self.borrowed = True

    def give_back(self):
        self.borrowed = False

    def __str__(self):
        return f"{'[x]' if self.borrowed else '[v]'} {self.title} by {self.author} from {self.year}"
