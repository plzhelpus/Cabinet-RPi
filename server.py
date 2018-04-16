import bluetooth
import pigpio
from time import sleep

SERVO_PIN = 18

def toggle_lock(pi, PIN, is_lock):
    if is_lock:
        unlock(pi, PIN)
    else:
        lock(pi, PIN)

def lock(pi, PIN):
    pi.set_servo_pulsewidth(SERVO_PIN, 1000)
    sleep(0.5)

def unlock(pi, PIN):
    pi.set_servo_pulsewidth(SERVO_PIN, 1500)
    sleep(0.5)

HOST_MAC_ADDRESS = 'B8:27:EB:21:B6:12'
PORT = 10
BACKLOG = 1
BUFFER_SIZE = 2**5

is_lock = True

try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((HOST_MAC_ADDRESS, bluetooth.PORT_ANY))
    s.listen(BACKLOG)

    pi = pigpio.pi()
    pi.set_mode(SERVO_PIN, pigpio.OUTPUT)
    
    lock(pi, SERVO_PIN)
    is_lock = True
    
    print('create socket :', s.getsockname())
    port = s.getsockname()[1]

    uuid = "00001101-0000-1000-8000-00805F9B34FB"

    bluetooth.advertise_service(s, "Cabinet", service_id = uuid,
        service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
        profiles = [ bluetooth.SERIAL_PORT_PROFILE ])

    while True:
        try:
            client, address = s.accept()
            print('create connection :', client.getpeername())
            while True:
                data = client.recv(BUFFER_SIZE)
                if data:
                    print(data.decode())
                    msg = data.decode() + "from Raspberry Pi 3B"
                    toggle_lock(pi, SERVO_PIN, is_lock)
                    is_lock = not is_lock
                    client.send(msg.encode())
                else:
                    print("No Data")
        except bluetooth.BluetoothError as err:
            print("[ERROR] ", err)
        except Exception as e:
            print("Occurs Error", e)
        finally:
            if client:
                client.close()
finally:
    if s:
        s.close()
    if pi:
        pi.set_mode(SERVO_PIN, pigpio.INPUT)
        pi.stop()
