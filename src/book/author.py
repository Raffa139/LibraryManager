from src.shared.value import Value


class Author(Value):
    def __init__(self, author):
        super().__init__(author)

    def valid(self, value):
        return len(value.strip()) > 0

    def normalize(self, value):
        return value.strip()
