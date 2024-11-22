from src.book.value import Value


class Keyword(Value):
    def __init__(self, keyword):
        super().__init__(keyword)

    def valid(self, value):
        return len(value.strip()) > 0

    def normalize(self, value):
        return value.strip()
