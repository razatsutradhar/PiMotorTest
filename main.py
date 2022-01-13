import time
import RPi.GPIO as GPIO

driver_port_1 = 11
driver_port_2 = 13
button_port = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(driver_port_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(driver_port_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button_port, GPIO.IN)


def forward():
    GPIO.output(driver_port_1, GPIO.HIGH)
    GPIO.output(driver_port_2, GPIO.LOW)
    time.sleep(2)
    GPIO.output(driver_port_1, GPIO.LOW)
    GPIO.output(driver_port_2, GPIO.LOW)


def backward():
    GPIO.output(driver_port_1, GPIO.LOW)
    GPIO.output(driver_port_2, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(driver_port_1, GPIO.LOW)
    GPIO.output(driver_port_2, GPIO.LOW)


if GPIO.input(button_port) == GPIO.HIGH:
    forward()
    backward()
