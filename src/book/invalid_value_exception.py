class InvalidValueException(Exception):
    def __init__(self, obj_name, value):
        super().__init__()

        self.obj_name = obj_name
        self.value = value
