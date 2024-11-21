import src.shared.cli as cli

from src.menu.command import Command
from src.menu.menu_exception import MenuException


class Menu:
    def __init__(self, title, *, on_error, subtitle=None):
        self.title = title
        self.subtitle = subtitle
        self.on_error = on_error
        self.commands = []
        self.latest_command = None
        self.close_requested = False

    def take_cmd_until_close(self):
        while not self.close_requested:
            self.take_cmd()

    def take_single_cmd(self):
        while not self.close_requested:
            if self.take_cmd():
                break

    def take_cmd(self):
        cli.write_str(self.title)

        if self.subtitle is not None:
            cli.write_str(self.subtitle)

        cli.write_str(self)
        cmd_input = cli.read_stripped_str()

        for command in self.commands:
            if cmd_input == command.cmd:
                self.run_cmd(command)
                return True
        else:
            return False

    def run_cmd(self, command):
        try:
            self.latest_command = command
            command.run(self)
        except MenuException as e:
            self.on_error.run(self, e)

    def rerun_latest_cmd(self):
        if self.latest_command is not None:
            self.run_cmd(self.latest_command)

    def register_cmd(self, cmd, title, action):
        self.commands.append(Command(cmd, title, action))

    def request_close(self):
        self.close_requested = True

    def __str__(self):
        cmds = [f"  {command}" for command in self.commands]
        return "\n".join(cmds)
