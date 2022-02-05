from serial import Serial


class MHZ19B:
    def __init__(self, port: str, baudrate: int):
        self.port = port
        self.baudrate = baudrate
        self.serial = Serial(port=None, baudrate=baudrate)

    @property
    def is_open(self) -> bool:
        return self.serial.is_open

    def open(self):
        self.serial.port = self.port
        self.serial.open()

    def close(self):
        self.serial.close()
        self.serial.port = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args, **kwargs):
        self.close()
