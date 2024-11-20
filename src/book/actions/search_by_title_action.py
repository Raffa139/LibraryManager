import src.cli as cli
import src.book.repository as repo

from src.views.list_view import ListView


class SearchByTitleAction:
    def run(self, menu):
        title = cli.read_stripped_str("Title: ")
        results = repo.instance().find_by_title(title)
        ListView(results).show()
