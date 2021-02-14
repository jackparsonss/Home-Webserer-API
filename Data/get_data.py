import serial
from time import sleep
from gpiozero import LED

led = LED(2)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

while True:
    try:
        sleep(1)
        temp = str(float(ser.readline().decode("utf-8").strip()))
        print("Temp: " + temp + "C")
        humidity = str(float(ser.readline().decode("utf-8").strip()))
        print("Humidity: " + humidity + "%")
    except:
        led.on()
        sleep(2)
