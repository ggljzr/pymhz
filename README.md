# pymhz

Library for reading MH-Z CO2 sensors. Inspiration:

* https://github.com/UedaTakeyuki/mh-z19/tree/master/pypi
* https://www.arduino.cc/reference/en/libraries/mh-z-co2-sensors/

## Instalation

For now, [pyserial](https://pypi.org/project/pyserial/) is the only dependency.

```
$ git clone https://github.com/ggljzr/pymhz
$ cd pymhz
$ python3 -m pip install .
```

## Usage

Basic usage example, that expects that sensor is connected to the Linux computer via
USB<>UART convertor. Assigned serial port is ``/dev/ttyUSB0``.

```python

from pymhz.mhz19b import MHZ19B

# usage is similar to the serial.Serial object
with MHZ19B("/dev/ttUSB0") as sensor:
    # turn on autocalibration
    # (note that this should be on by default)
    sensor.enable_autocalibration()

    # read single concentration value
    response = sensor.read_concentration()

    if response.is_valid:
        print(f"CO2 concentration: {response.concentration} ppm")
    else:
        print("Invalid response!")

```

## Links

* [MH-Z19B dataheet](https://www.winsen-sensor.com/d/files/infrared-gas-sensor/mh-z19b-co2-ver1_0.pdf)