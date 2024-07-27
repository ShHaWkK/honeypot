import logging

def setup_logger(log_path):
    logger = logging.getLogger("honeypot")
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler(log_path)
    handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    return logger
