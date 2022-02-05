from sys import argv
from time import sleep
from pymhz.mhz19b import MHZ19B


with MHZ19B(argv[1]) as sensor:
    while True:
        response = sensor.read_concentration()
        print(f"CO2: {response.concentration} ppm")
        sleep(1.0)
