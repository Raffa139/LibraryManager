import src.shared.cli as cli
import src.book.repository as repo

from src.shared.views.list_view import ListView


class SearchByAuthorAction:
    def run(self, menu):
        author = cli.read_stripped_str("Author: ")
        results = repo.instance().find_by_author(author)
        ListView(results).show()
