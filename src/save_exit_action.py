class SaveExitAction:
    def run(self, menu, repo):
        repo.save_to_disk()
        menu.request_close()
