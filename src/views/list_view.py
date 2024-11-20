class ListView:
    def __init__(self, items):
        self.items = items

    def show(self):
        for item in self.items:
            print(item)
