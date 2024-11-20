import re

from value import Value


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


class Title(Value):
    def __init__(self, title):
        super().__init__(title)

    def valid(self, value):
        return len(value.strip()) > 0

    def normalize(self, value):
        return value.strip()


class Author(Value):
    def __init__(self, author):
        super().__init__(author)

    def valid(self, value):
        return len(value.strip()) > 0

    def normalize(self, value):
        return value.strip()


class PublicationYear(Value):
    def __init__(self, year):
        super().__init__(year)

    def valid(self, value):
        match = re.fullmatch(r"^[1-9]\d+|^[1-9]", value)
        return match is not None
