import random
import pandas as pd
from fastparquet import write
from time import sleep
# from board import D14
# import adafruit_dht

import grpc
import collector_pb2_grpc
import collector_pb2

# dht_device = adafruit_dht.DHT22(D14)

def poll(stub : collector_pb2_grpc.CollectorStub):
    tick = 0 
    data = []
    
    while True:
        try:
            sleep(1)
            tick += 1

            humidity =  random.random() * 76.6 # dht_device.humidity 
            temperature = random.random() * 29.6 # dht_device.temperature 

            print("Humidity:", humidity)
            print("Temparature:", temperature)

            data_point = [humidity, temperature]

            # May want to yield this instead
            reading = collector_pb2.Reading(humidity=humidity, temperature=temperature)
            stub.SendReading(reading)

            data.append(data_point)

        except Exception as e:
            print(e)
            continue

with grpc.insecure_channel('localhost:8080') as channel:
    stub = collector_pb2_grpc.CollectorStub(channel)
    poll(stub)