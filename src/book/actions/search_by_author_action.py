import src.book.repository as repo

from src.views.list_view import ListView


class SearchByAuthorAction:
    def run(self, menu):
        author = input("Author: ")
        results = repo.instance().find_by_author(author)
        ListView(results).show()
