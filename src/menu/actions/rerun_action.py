class RerunAction:
    def __init__(self, *, rerun_on):
        self.rerun_on = rerun_on

    def run(self, menu, repo):
        if self.rerun_on == menu:
            raise RuntimeError("To prevent infinite recursion, retry action cannot run on menu it is registered upon.")

        self.rerun_on.rerun_latest_cmd()
