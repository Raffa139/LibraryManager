class Menu:
    def __init__(self, title):
        self.title = title
        self.commands = []
        self.close_requested = False

    def take_cmd(self):
        print(self.title)
        print(self)
        cmd_input = input().strip()

        for command in self.commands:
            if cmd_input == command.cmd:
                command.run(self)
                return True
        else:
            return False

    def register_cmd(self, cmd, title, action):
        self.commands.append(Command(cmd, title, action))

    def request_close(self):
        self.close_requested = True

    def __str__(self):
        cmds = [f"{command}" for command in self.commands]
        return "\n".join(cmds)


class Command:
    def __init__(self, cmd, title, action):
        self.cmd = cmd
        self.title = title
        self.action = action

    def run(self, menu):
        self.action.run(menu)

    def __str__(self):
        return f"{self.cmd}. {self.title}"


class MenuException(Exception):
    def __init__(self, message):
        self.message = message
