from time import sleep

from serial import Serial

from .utils import calculate_checksum


class Response:
    """
    Response from the MH-Z19B sensor.
    """

    def __init__(self, data: bytes) -> None:
        self.data = data

    @property
    def checksum(self) -> int:
        return calculate_checksum(self.data)

    @property
    def is_valid(self) -> bool:
        """
        Validates the data against expected checksum
        (last byte of the recieved data).
        """

        return self.checksum == self.data[-1]

    @property
    def concentration(self) -> float:
        """
        Returns calculated CO2 concentration or -1 if the checksum
        of the response is not valid.
        """

        if not self.is_valid:
            return -1

        return float(256 * self.data[2] + self.data[3])


class MHZ19B:

    CONCENTRATION_COMMAND = bytes(
        [0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]
    )
    ENABLE_AUTOCALIBRATION_COMMAND = bytes(
        [0xFF, 0x01, 0x79, 0xA0, 0x00, 0x00, 0x00, 0x00, 0xE6]
    )
    DISABLE_AUTOCALIBRATION_COMMAND = bytes(
        [0xFF, 0x01, 0x79, 0x00, 0x00, 0x00, 0x00, 0x00, 0x86]
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

    def enable_autocalibration(self):
        self.serial.write(self.ENABLE_AUTOCALIBRATION_COMMAND)
        sleep(0.1)

    def disable_autocalibration(self):
        self.serial.write(self.DISABLE_AUTOCALIBRATION_COMMAND)
        sleep(0.1)

    def read_concentration(self) -> Response:
        self.serial.write(self.CONCENTRATION_COMMAND)
        sleep(0.1)
        data = self.serial.read(self.RESPONSE_LENGTH)
        return Response(data)
