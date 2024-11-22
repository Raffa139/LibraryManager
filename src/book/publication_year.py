import re

from src.book.value import Value


class PublicationYear(Value):
    def __init__(self, year):
        super().__init__(year)

    def valid(self, value):
        """
        :param value: The value
        :return: True if the value is a number not starting with 0, False otherwise
        """
        match = re.fullmatch(r"^[1-9]\d+|^[1-9]", value)
        return match is not None
