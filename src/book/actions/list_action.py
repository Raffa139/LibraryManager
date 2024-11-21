from src.shared.views.list_view import ListView


class ListAction:
    def run(self, menu, repo):
        all_books = repo.books
        ListView(all_books).show()
