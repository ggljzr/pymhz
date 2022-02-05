from time import sleep

from serial import Serial


class MHZ19B:

    CONCENTRATION_COMMAND = bytes(
        [0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]
    )
    RESPONSE_LENGTH = 9

    def __init__(self, port: str, baudrate: int = 9600):
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

    def read_concentration(self) -> bytes:
        self.serial.write(self.CONCENTRATION_COMMAND)
        sleep(0.1)
        response = self.serial.read(self.RESPONSE_LENGTH)
        return response
