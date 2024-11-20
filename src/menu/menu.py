import src.cli as cli

from src.menu.command import Command


class Menu:
    def __init__(self, title):
        self.title = title
        self.commands = []
        self.close_requested = False

    def take_cmd(self):
        cli.write_str(self.title)
        cli.write_str(self)
        cmd_input = cli.read_stripped_str()

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
