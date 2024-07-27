import socket
import sys

class FakeService:
    def __init__(self, port, logger):
        self.port = port
        self.logger = logger

    def run(self):
        self.logger.info(f"Honeypot started on port {self.port}.")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', self.port))
                s.listen()
                self.logger.info(f"Listening on port {self.port}")
                while True:
                    conn, addr = s.accept()
                    with conn:
                        self.logger.info(f"Connection attempt from {addr}")
                        conn.sendall(b"Fake honeypot service.\n")
        except Exception as e:
            self.logger.error(f"Failed to start honeypot: {e}")
            sys.exit(1)

    def stop(self):
        self.logger.info("Honeypot stopped.")
