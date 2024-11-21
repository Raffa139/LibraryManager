from src.menu.menu import Menu
from src.menu.actions.close_menu_action import CloseMenuAction
from src.book.actions.search.search_by_author_action import SearchByAuthorAction
from src.book.actions.search.search_by_title_action import SearchByTitleAction


class SearchAction:
    def run(self, menu):
        search_menu = Menu("Book search", on_error=menu.on_error)
        search_menu.register_cmd("1", "Search by title", SearchByTitleAction())
        search_menu.register_cmd("2", "Search by author", SearchByAuthorAction())
        search_menu.register_cmd("0", "Home", CloseMenuAction())

        search_menu.take_single_cmd()

        # TODO: Result menu w/ options how to proceed
