from src.book.value import Value


class Title(Value):
    def __init__(self, title):
        super().__init__(title)

    def valid(self, value):
        return len(value.strip()) > 0

    def normalize(self, value):
        return value.strip()
