import time

class FakeService:
    def __init__(self, config_path, logger):
        self.config_path = config_path
        self.logger = logger

    def run(self):
        self.logger.info("Honeypot started.")
        while True:
            self.logger.info("Fake service running...")
            time.sleep(60)

    def stop(self):
        self.logger.info("Honeypot stopped.")
