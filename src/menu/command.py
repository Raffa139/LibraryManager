class Command:
    def __init__(self, trigger, title, action):
        self.trigger = trigger
        self.title = title
        self.action = action

    def run(self, menu):
        self.action.run(menu)

    def __str__(self):
        return f"{self.trigger}. {self.title}"
