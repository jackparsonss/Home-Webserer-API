import serial
from time import sleep
from gpiozero import LED

led = LED(2)

ser = serial.Serial('/dev/tty/ACM0', 9600, timeout=5)

while True:
    try:
        sleep(1)
        out = str(float(ser.readline().decode("utf-8").strip()))
        print("Temp: " + out + "C")
    except:
        led.on()
        sleep(2)