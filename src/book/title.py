from src.book.value import Value


class Title(Value):
    def __init__(self, title):
        super().__init__(title)

    def valid(self, value):
        """
        :param value: The value
        :return: True if the stripped value has min. length of 1, False otherwise
        """
        return len(value.strip()) > 0 and "," not in value

    def normalize(self, value):
        """
        :param value: The value
        :return: The stripped value
        """
        return value.strip()
