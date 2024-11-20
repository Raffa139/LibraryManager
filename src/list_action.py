import repository as repo

from list_view import ListView


class ListAction:
    def run(self, menu):
        all_books = repo.instance().books
        ListView(all_books).show()
