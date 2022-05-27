1. Try out pull-up resistor to see if it improves temperature readings 
2. Try out Nomad
  - Nomad cannot be installed on Raspberry Pi
  - Learn how to configure Nomad, esp. ports 
      - Nomad does port mapping with a binded address (e.g. 127.0.0.1:8080->8080/tcp). What this mean is that we won't be able to reach 8080 on the same host if we try to access via another IP address
      - To resolve the above issue, we can configure using the nomad `client` stanza's `network_interface`  

       
3. Read up and undertand Parquet files
