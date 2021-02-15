import serial
from time import sleep
from gpiozero import LED
from datetime import datetime
import json

led = LED(2)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

def get_data():
    led = LED(2)
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    try:
        data = {}
        led.off()
        sleep(1)
        temp = str(float(ser.readline().decode("utf-8").strip()))
        #print("Temp: " + temp + "C")
        humidity = str(float(ser.readline().decode("utf-8").strip()))
        #print("Humidity: " + humidity + "%")
        time = datetime.now()
        data[str(time)[:-7]] = {
            "Temperature" : temp,
            "Humidity" : humidity
        }
        data_set = json.dumps(data)
        print(json.loads(data_set))
        return data_set
    except Exception as ex:
        print(ex)
        led.on()
        sleep(2)
    
