## Architecture - Maybe?
Collector - `collector.py` that retrieves humidity and temperature readings from the sensor and writes them into a Parquet file  
Ingester - ??? that reads the values from the Parquet file and ingest it into a TSDB (InfluxDB?) and will trim the file after ingesting the values  


Uses Nomad to orchestrate

## Learning Objectives
1. Trying out Nomad, InfluxDB, Parquet
1. The right way for multiple services to read and modify the same file 

## Learnt
- Avoid growing your DataFrame when accumulating your data. [link](https://stackoverflow.com/a/62734983)
- Parquet is not a plain text file

## PIN Setup
DHT22 Out ~ GPIO14  
DHT22 + ~ 3V3  
DHT22 - ~ GND  

## Dev Setup
On PC 

```$ ls rpi-humidity/* | entr rsync -r rpi-humidity pi@raspberrypi.local:/home/pi/```

On Raspberry Pi

```$ ls | entr -r python3 collector.py```
