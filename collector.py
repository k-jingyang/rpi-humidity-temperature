from board import D14
import adafruit_dht
from time import sleep

dht_device = adafruit_dht.DHT22(D14)

while True:
    try:
        sleep(1)
        print("Humidity:", dht_device.humidity)
        print("Temperator:", dht_device.temperature)
    except Exception as e:
        continue