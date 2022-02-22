import bluetooth

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
