import re

from src.value import Value


class PublicationYear(Value):
    def __init__(self, year):
        super().__init__(year)

    def valid(self, value):
        match = re.fullmatch(r"^[1-9]\d+|^[1-9]", value)
        return match is not None
