## Architecture - Maybe?
Sensor - `sensor.py` that retrieves humidity and temperature readings from the sensor and sends it over the wire using gRPC to the Collector.
Collector - Receives readings from the Sensor and writes them into a Parquet file  
Ingester - Reads the values from the Parquet file and ingest it into a TSDB (InfluxDB?) and will trim the file after ingesting the values  

Uses Nomad to orchestrate Collector and Ingester

## Learning Objectives
1. Trying out Nomad, InfluxDB, Parquet, gRPC
1. The right way for multiple services to read and modify the same file 
1. Experiment with error handling when the Collector is unavailable. Can be done by buffering? Exponential backoffs?

## Learnt
- Avoid growing your DataFrame when accumulating your data. [link](https://stackoverflow.com/a/62734983)
- Parquet is not a plain text file
- Check ahead of time, if a binary can be installed on an ARM board
- Follow when guides tell you to use a pull-up resistor? 

## PIN Setup
DHT22 Out ~ GPIO14  
DHT22 + ~ 3V3  
DHT22 - ~ GND  

## Dev Setup
On PC 

```$ ls rpi-humidity/* | entr rsync -r rpi-humidity pi@raspberrypi.local:/home/pi/```

On Raspberry Pi

```$ ls | entr -r python3 sensor.py```
