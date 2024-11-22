from src.book.value import Value


class Author(Value):
    def __init__(self, author):
        super().__init__(author)

    def valid(self, value):
        """
        :param value: The value
        :return: True if the stripped value has min. length of 1, False otherwise
        """
        return len(value.strip()) > 0

    def normalize(self, value):
        """
        :param value: The value
        :return: The stripped value
        """
        return value.strip()
