import src.book.repository as repo


class SaveExitAction:
    def run(self, menu):
        repo.instance().save_to_disk()
        menu.request_close()
