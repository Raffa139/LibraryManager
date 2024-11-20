class Value:
    def __init__(self, value):
        if not self.valid(value):
            raise InvalidValueException(value)

        self.value = self.normalize(value)

    def valid(self, value):
        pass

    def normalize(self, value):
        return value

    def __str__(self):
        return self.value


class InvalidValueException(Exception):
    def __init__(self, value):
        super().__init__(f"Value '{value}' invalid")
