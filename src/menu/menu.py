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
        """
        Asks to input a valid command via the console, until the menu is requested to close.
        On an invalid command it will ask again.
        """
        while not self.close_requested:
            self.take_cmd()

    def take_single_cmd(self):
        """
        Asks to input a valid command via the console once.
        After a command has been recognized, the menu is finished.
        On an invalid command it will ask again.
        """
        while not self.close_requested:
            if self.take_cmd():
                break

    def take_cmd(self):
        """
        Prints the menu and asks to input a command via the console.
        If the command got recognized it will run the associated action and return True.
        Otherwise it returns False.
        :return: True if the entered command got recognized, False otherwise.
        """
        self.print_menu()
        cli_input = cli.read_stripped_str()

        for command in self.commands:
            if cli_input == command.trigger:
                self.run_cmd(command)
                return True
        else:
            return False

    def run_cmd(self, command):
        """
        Runs the associated action from the commmand and keeps track of the latest runned command.
        On Menu exception, the on_error action will be run.
        :param command: The command to run
        """
        try:
            self.latest_command = command
            command.run(self, self.repo)
        except MenuException as e:
            self.on_error.run(self, self.repo, e)

    def rerun_latest_cmd(self):
        """
        Reruns the latest runned command, if there has been one.
        """
        if self.latest_command is not None:
            self.run_cmd(self.latest_command)

    def register_cmd(self, trigger, title, action):
        """
        Adds a new entry to the menu.
        :param trigger: The string to enter to trigger the command
        :param title: Will be displayed in the menu
        :param action: The action to run when the command is triggered
        """
        self.commands.append(Command(trigger, title, action))

    def request_close(self):
        """
        Instructs the menu to not take any commands anymore.
        """
        self.close_requested = True

    def print_menu(self):
        """
        Print the title, subtitle and entries to the console.
        """
        cli.write_title_str(self.title)

        if self.subtitle is not None:
            cli.write_str(self.subtitle)

        cli.write_str(self)

    def __str__(self):
        cmds = [f"  {command}" for command in self.commands]
        return "\n".join(cmds)
