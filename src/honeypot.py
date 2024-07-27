import os
from src.fake_service import FakeService
from src.logger import setup_logger

def main():
    config_path = "../config/honeypot_config.yaml"
    log_path = "../logs/honeypot.log"
    
    logger = setup_logger(log_path)
    
    honeypot = FakeService(config_path, logger)
    honeypot.run()

if __name__ == "__main__":
    main()
