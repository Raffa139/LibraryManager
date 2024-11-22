import src.cli as cli

from src.book.views.list_view import ListView


class SearchByKeywordAction:
    def run(self, menu, repo):
        keyword = cli.read_stripped_str("Keyword: ")
        results = repo.find_by_keyword(keyword)
        ListView(results).show()
