from time import sleep
import logging as log
import os

from board import D14
import adafruit_dht

import grpc
import collector_pb2_grpc
import collector_pb2

dht_device = adafruit_dht.DHT22(D14)

log.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%H:%S')

def poll(stub : collector_pb2_grpc.CollectorStub):
    tick = 0 
    data = []
    
    while True:
        try:
            sleep(1)
            tick += 1

            humidity =   dht_device.humidity 
            temperature = dht_device.temperature 

            if humidity == None or temperature == None:
                continue

            log.debug("Humidity: %s", humidity)
            log.debug("Temperature: %s", temperature)

            # May want to yield this instead
            reading = collector_pb2.Reading(humidity=humidity, temperature=temperature)
            stub.SendReading(reading)

        except RuntimeError as e:
            log.warning(e)
            continue

with grpc.insecure_channel('192.168.0.161:8080') as channel:
    stub = collector_pb2_grpc.CollectorStub(channel)
    poll(stub)