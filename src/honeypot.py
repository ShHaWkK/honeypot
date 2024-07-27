import os
import yaml
from src.fake_service import FakeService
from src.logger import setup_logger

def main():
    config_path = "../config/honeypot_config.yaml"
    log_path = "../logs/honeypot.log"
    
    logger = setup_logger(log_path)
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    port = config['honeypot']['port']
    
    honeypot = FakeService(port, logger)
    honeypot.run()

if __name__ == "__main__":
    main()
