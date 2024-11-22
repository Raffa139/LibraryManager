import src.cli as cli

from src.menu.command import Command
from src.menu.menu_exception import MenuException


class Menu:
    def __init__(self, title, *, repo, on_error, subtitle=None):
        self.title = title
        self.repo = repo
        self.on_error = on_error
        self.subtitle = subtitle
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
        self.print_menu()
        cli_input = cli.read_stripped_str()

        for command in self.commands:
            if cli_input == command.trigger:
                self.run_cmd(command)
                return True
        else:
            return False

    def run_cmd(self, command):
        try:
            self.latest_command = command
            command.run(self, self.repo)
        except MenuException as e:
            self.on_error.run(self, self.repo, e)

    def rerun_latest_cmd(self):
        if self.latest_command is not None:
            self.run_cmd(self.latest_command)

    def register_cmd(self, trigger, title, action):
        self.commands.append(Command(trigger, title, action))

    def request_close(self):
        self.close_requested = True

    def print_menu(self):
        cli.write_title_str(self.title)

        if self.subtitle is not None:
            cli.write_str(self.subtitle)

        cli.write_str(self)

    def __str__(self):
        cmds = [f"  {command}" for command in self.commands]
        return "\n".join(cmds)
