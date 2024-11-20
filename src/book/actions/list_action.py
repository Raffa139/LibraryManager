import src.book.repository as repo

from src.views.list_view import ListView


class ListAction:
    def run(self, menu):
        all_books = repo.instance().books
        ListView(all_books).show()
