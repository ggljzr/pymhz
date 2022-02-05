from sys import argv
from time import sleep
from datetime import datetime
from pymhz.mhz19b import MHZ19B

with MHZ19B(argv[1]) as sensor:
    sensor.enable_autocalibration()
    while True:
        response = sensor.read_concentration()
        print(f"[{datetime.now().isoformat()}] CO2: {response.concentration} ppm")
        sleep(0.9)
