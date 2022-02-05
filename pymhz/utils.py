def calculate_checksum(data: bytes) -> int:
    """
    Checksum calculation, as per MH-Z19B datasheet, section C. Calibrate and calculate.
    ``data`` are either command or response, including the original/expected checksum as last byte.

    Link: https://www.winsen-sensor.com/d/files/infrared-gas-sensor/mh-z19b-co2-ver1_0.pdf
    """

    # -1 to skip the checksum at the end
    s = sum(data[1:-1]) & 0xFF
    inv = 0xFF - s
    return (inv + 1) & 0xFF
