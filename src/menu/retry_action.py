class RetryAction:
    def __init__(self, external_menu):
        self.external_menu = external_menu

    def run(self, menu):
        if self.external_menu == menu:
            raise RuntimeError("To prevent infinite recursion, retry action cannot run on menu it is registered upon.")

        self.external_menu.rerun_latest_cmd()
