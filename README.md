## PIN Setup
DHT22 Out ~ GPIO14  
DHT22 + ~ 3V3  
DHT22 - ~ GND  


## Dev Setup
On PC 

```$ ls rpi-humidity/* | entr rsync -r rpi-humidity pi@raspberrypi.local:/home/pi/```

On Raspberry Pi

```$ ls | entr -r python3 main.py```

