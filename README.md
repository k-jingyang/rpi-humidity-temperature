## Architecture - Maybe?
Sensor - `sensor.py` that retrieves humidity and temperature readings from the sensor and sends it over the wire using gRPC to the Collector.
Collector - Receives readings from the Sensor and writes them into multiple Parquet files
Ingester - Reads the values from the Parquet files and ingest it into a TSDB (InfluxDB?) and will trim the file after ingesting the values  

Uses Nomad to orchestrate Collector and Ingester

## Learning Objectives
1. Trying out Nomad, InfluxDB, Parquet, gRPC
1. The right way for multiple services to read and modify the same file 
1. Experiment with error handling when the Collector is unavailable. Can be done by buffering? Exponential backoffs?

## Learnt
- Avoid growing your DataFrame when accumulating your data. [link](https://stackoverflow.com/a/62734983)
- Parquet is a binary file format
    - Generally not a good idea to append [link](https://issues.apache.org/jira/browse/SPARK-18199), but why does Spark provide the API for it? Maybe, it's still creating new files BTS? [link](https://stackoverflow.com/questions/39234391/how-to-append-data-to-an-existing-parquet-file)
- Check ahead of time, if a binary can be installed on an ARM board
- Use `parquet-tools` to read a Parquet file 

## PIN Setup
DHT22 Out ~ GPIO14  
DHT22 + ~ 3V3  
DHT22 - ~ GND  

## Dev Setup
On PC 

```$ ls rpi-humidity/* | entr rsync -r rpi-humidity pi@raspberrypi.local:/home/pi/```

On Raspberry Pi

```$ ls | entr -r python3 sensor.py```
