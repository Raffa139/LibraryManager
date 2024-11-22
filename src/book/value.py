from src.book.invalid_value_exception import InvalidValueException


class Value:
    def __init__(self, value):
        if not self.valid(value):
            raise InvalidValueException(type(self).__name__, value)

        self.value = self.normalize(value)

    def valid(self, value):
        """
        Validates the given value.
        :param value: The value to be validated
        :return: True if the valid is valid, False otherwise
        """
        return True

    def normalize(self, value):
        """
        Normalize the value, before passing it on. For example to strip a string.
        :param value: The value to be normalized
        :return: The normalized value
        """
        return value

    def __str__(self):
        return self.value
