from pymhz.utils import calculate_checksum


def test_calculate_checksum():
    # from M-HZ19 datasheet
    # checksum of the 'read concentration' command
    test_data = bytes([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
    assert calculate_checksum(test_data) == 0x79

    # edge case
    test_data = bytes([0xFF, 0x01, 0xFE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    assert calculate_checksum(test_data) == 0x01
