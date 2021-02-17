import serial
from datetime import datetime
import RPi.GPIO as GPIO
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

def get_data():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
    data = {}
    try:
        temp = str(float(ser.readline().decode("utf-8").strip()))
        humidity = str(float(ser.readline().decode("utf-8").strip()))
        time = datetime.now()
        data[str(time)[:-7]] = {
            "Temperature" : temp,
            "Humidity" : humidity
        }
        ser.close()
        return data
    except Exception as ex:
        print(ex)

def toggle_led(state):
    if state == 'on':
        GPIO.output(18, GPIO.HIGH)
    elif state == 'off':
        GPIO.output(18, GPIO.LOW)
    else:
        abort(400, message="did not enter on or off...")
    return {'LED': state}, 200



    
