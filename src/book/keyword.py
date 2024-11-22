from src.book.value import Value


class Keyword(Value):
    def __init__(self, keyword):
        super().__init__(keyword)

    def valid(self, value):
        """
        :param value: The value
        :return: True if the stripped value has min. length of 1 and does not contain ',' and ';', False otherwise
        """
        return len(value.strip()) > 0 and "," not in value and ";" not in value

    def normalize(self, value):
        """
        :param value: The value
        :return: The stripped value
        """
        return value.strip()
