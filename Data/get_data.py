import serial
from time import sleep
from gpiozero import LED
from datetime import datetime
import json

led = LED(2)
data = {}
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

while True:
    try:
        sleep(1)
        temp = str(float(ser.readline().decode("utf-8").strip()))
        #print("Temp: " + temp + "C")
        humidity = str(float(ser.readline().decode("utf-8").strip()))
        #print("Humidity: " + humidity + "%")
        data[datetime.now()] = {
            "Temperature" : temp,
            "Humidity" : humidity
        }
        data_set = json.dumps(data)
        print(json.load(data_set))
    except:
        led.on()
        sleep(2)
