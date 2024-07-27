import logging
import os

def setup_logger(log_path):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    logger = logging.getLogger("honeypot")
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler(log_path)
    handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    return logger
