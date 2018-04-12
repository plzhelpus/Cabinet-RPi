import bluetooth

HOST_MAC_ADDRESS = 'B8:27:EB:21:B6:12'
PORT = 10
BACKLOG = 1
BUFFER_SIZE = 2**5

try: 
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((HOST_MAC_ADDRESS, bluetooth.PORT_ANY))
    s.listen(BACKLOG)

    print('create socket :', s.getsockname())
    port = s.getsockname()[1]

    uuid = "00001101-0000-1000-8000-00805F9B34FB"

    bluetooth.advertise_service(s, "Cabinet", service_id = uuid,
        service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS], 
        profiles = [ bluetooth.SERIAL_PORT_PROFILE ])


    try:
        client, address = s.accept()
        print('create connection :', client.getpeername())
        while True:
            data = client.recv(BUFFER_SIZE)
            if data:
                print(data.decode())
                msg = data.decode() + "from Raspberry Pi 3B"
                client.send(msg.encode())
            else:
                print("No Data")
    except Exception as e:
        print("Occurs Error", e)
    finally:
        if client:
            client.close()
finally:
    if s:
        s.close()

