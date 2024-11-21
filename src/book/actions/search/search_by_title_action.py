import src.shared.cli as cli

from src.shared.views.list_view import ListView


class SearchByTitleAction:
    def run(self, menu, repo):
        title = cli.read_stripped_str("Title: ")
        results = repo.find_by_title(title)
        ListView(results).show()
