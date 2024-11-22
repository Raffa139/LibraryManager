class Command:
    def __init__(self, trigger, title, action):
        self.trigger = trigger
        self.title = title
        self.action = action

    def run(self, menu, repo):
        """
        Delegates to the actions run method.
        :param menu: The menu this command is registered on
        :param repo: The repo from within the menu
        """
        self.action.run(menu, repo)

    def __str__(self):
        return f"{self.trigger}. {self.title}"
