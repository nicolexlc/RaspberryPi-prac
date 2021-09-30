import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

SleepTimeL = 2

try:
    GPIO.output(2, GPIO.LOW)
    print("UNO")
    time.sleep(SleepTimeL);
    GPIO.output(3, GPIO.LOW)
    print("DOS")
    time.sleep(SleepTimeL);
    GPIO.output(4, GPIO.LOW)
    print("TRES")
    time.sleep(SleepTimeL);
    GPIO.output(17, GPIO.LOW)
    print("CUATRO")
    time.sleep(SleepTimeL);
    GPIO.output(27, GPIO.LOW)
    print("CINCO")
    time.sleep(SleepTimeL);
    GPIO.output(22, GPIO.LOW)
    print("SEIS")
    time.sleep(SleepTimeL);
    GPIO.output(10, GPIO.LOW)
    print("SIETE")
    time.sleep(SleepTimeL);    
    GPIO.output(9, GPIO.LOW)
    print("OCHO")
    time.sleep(SleepTimeL);
    GPIO.cleanup()
    print("Adiós!")

except KeyboardInterrupt:
        print("Salir")

GPIO.cleanup()