import serial
from time import sleep
from datetime import datetime
import json


def get_data():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    data = {}
    try:
        temp = str(float(ser.readline().decode("utf-8").strip()))
        #print("Temp: " + temp + "C")
        humidity = str(float(ser.readline().decode("utf-8").strip()))
        #print("Humidity: " + humidity + "%")
        time = datetime.now()
        data[str(time)[:-7]] = {
            "Temperature" : temp,
            "Humidity" : humidity
        }
        ser.close()
        return data
    except Exception as ex:
        print(ex)
    
