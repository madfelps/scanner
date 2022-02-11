from influxdb import InfluxDBClient
from datetime import datetime
import bluetooth 

def update_device(number_of_devices):
    payload = []
    data = []

    data = {
    "measurement":"bluetoothproject",
    "tags":{
        "ticker":"TSLA"
    },
    "time":datetime.now(),
    "fields":{
        'number_of_devices': number_of_devices
    }
    }

    payload.append(data)
    return payload

#Setup database
client = InfluxDBClient('localhost', 8086, 'torizon', 'felipe', 'scanner_db')
client.create_database('monitoring_db')

#Update device
payload = []

while(1):
    #Scanning our nearby devices using bluetooth
    nearby_devices = bluetooth.discover_devices(lookup_names=True)

    print("number of devices: ", len(nearby_devices))
    payload = update_device(len(nearby_devices))

    #Sending our payload to influxDB
    client.write_points(payload)

    for addr, name in nearby_devices:
        print("address: ", addr)
        print("name ", name)
    

