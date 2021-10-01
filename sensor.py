from time import sleep
import logging as log
import os
import threading
from queue import SimpleQueue

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

def send_to_collector(queue: SimpleQueue):
    with grpc.insecure_channel('192.168.0.161:8080') as channel:
        stub = collector_pb2_grpc.CollectorStub(channel)
        while True:
            (temperature, humidity) = queue.get()
            reading = collector_pb2.Reading(temperature=temperature, humidity=humidity)
            stub.SendReading(reading)

def poll(queue: SimpleQueue):
    while True:
        try:
            sleep(1)

            humidity =   dht_device.humidity 
            temperature = dht_device.temperature 

            if humidity == None or temperature == None:
                continue

            log.debug("Humidity: %s", humidity)
            log.debug("Temperature: %s", temperature)

            queue.put((temperature, humidity))

        except RuntimeError as e:
            log.warning(e)
            continue

queue = SimpleQueue();
poller = threading.Thread(target=poll, args=[queue])
sender = threading.Thread(target=send_to_collector, args=[queue])

poller.start()
sender.start()
poller.join()
