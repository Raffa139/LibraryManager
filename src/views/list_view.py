import src.cli as cli


class ListView:
    def __init__(self, items):
        self.items = items

    def show(self):
        for item in self.items:
            cli.write_str(item)
