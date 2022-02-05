from sys import argv
from time import sleep
from pymhz.mhz19b import MHZ19B


with MHZ19B(argv[1]) as sensor:
    while True:
        print(sensor.read_concentration())
        sleep(1.0)
