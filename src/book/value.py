from src.book.invalid_value_exception import InvalidValueException


class Value:
    def __init__(self, value):
        if not self.valid(value):
            raise InvalidValueException(type(self).__name__, value)

        self.value = self.normalize(value)

    def valid(self, value):
        pass

    def normalize(self, value):
        return value

    def __str__(self):
        return self.value
