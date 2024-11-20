import repository as repo

from menu import Menu
from list_view import ListView
from close_menu_action import CloseMenuAction


class SearchAction:
    def run(self, menu):
        search_menu = Menu("=== Book search ===")
        search_menu.register_cmd("1", "Search by title", SearchByTitleAction())
        search_menu.register_cmd("2", "Search by author", SearchByAuthorAction())
        search_menu.register_cmd("0", "Home", CloseMenuAction())

        while not search_menu.close_requested:
            if search_menu.take_cmd():
                break


class SearchByTitleAction:
    def run(self, menu):
        title = input("Title: ")
        results = repo.instance().find_by_title(title)
        ListView(results).show()


class SearchByAuthorAction:
    def run(self, menu):
        author = input("Author: ")
        results = repo.instance().find_by_author(author)
        ListView(results).show()
