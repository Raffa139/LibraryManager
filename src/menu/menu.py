import src.shared.cli as cli

from src.menu.command import Command
from src.menu.menu_exception import MenuException


class Menu:
    def __init__(self, title, *, on_error, subtitle=None):
        self.title = title
        self.subtitle = subtitle
        self.on_error = on_error
        self.commands = []
        self.close_requested = False

    def take_cmd(self):
        cli.write_str(self.title)

        if self.subtitle is not None:
            cli.write_str(self.subtitle)

        cli.write_str(self)
        cmd_input = cli.read_stripped_str()

        for command in self.commands:
            if cmd_input == command.cmd:
                try:
                    command.run(self)
                except MenuException as e:
                    self.on_error.run(self, e)

                return True
        else:
            return False

    def register_cmd(self, cmd, title, action):
        self.commands.append(Command(cmd, title, action))

    def request_close(self):
        self.close_requested = True

    def __str__(self):
        cmds = [f"  {command}" for command in self.commands]
        return "\n".join(cmds)
