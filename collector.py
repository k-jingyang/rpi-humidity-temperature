import collections
import random
from fastparquet import write
from time import sleep
import fastparquet
import pandas as pd

# from board import D14
# import adafruit_dht

# dht_device = adafruit_dht.DHT22(D14)

# Should the Parquet file contain time too? Are timestamps treated specially as compared to normal data?

data = []
tick = 0
PERSIST_INTERVAL = 10

while True:
    try:
        sleep(1)
        tick += 1
        humidity = random.random() * 76.6
        temperature = random.random() * 29.6

        data_point = [humidity, temperature]
        data.append(data_point)

        if tick % PERSIST_INTERVAL == 0:
            df = pd.DataFrame(data,  columns=["humidity", "temperature"])

            # How to append to Parquet file? You can't
            write('outfile.parquet', df)
            tick = 0
            data = []

        # print("Humidity:", dht_device.humidity)
        # print("Temparature:", dht_device.temperature)

    except Exception as e:
        continue
