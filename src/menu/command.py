class Command:
    def __init__(self, cmd, title, action):
        self.cmd = cmd
        self.title = title
        self.action = action

    def run(self, menu):
        self.action.run(menu)

    def __str__(self):
        return f"{self.cmd}. {self.title}"
