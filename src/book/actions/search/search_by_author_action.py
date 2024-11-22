import src.cli as cli

from src.book.views.list_view import ListView


class SearchByAuthorAction:
    def run(self, menu, repo):
        author = cli.read_stripped_str("Author: ")
        results = repo.find_by_author(author)
        ListView(results).show()
