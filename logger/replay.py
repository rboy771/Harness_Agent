class replay:
    def __init__(self, logger):
        self.logger = logger
    def replay(self):
        for entry in self.logger.entries:
            print("\n--- STEP", entry['step'], "---")
            print("OBSERVATION:", entry['observation'])
            print("ACTION:", entry['action'])
