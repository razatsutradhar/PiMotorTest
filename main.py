import time
import RPi.GPIO as GPIO

driver_port_1 = 11
driver_port_2 = 13
button_port = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(driver_port_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(driver_port_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button_port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def forward():
    GPIO.output(driver_port_1, GPIO.HIGH)
    GPIO.output(driver_port_2, GPIO.LOW)
    time.sleep(.8)
    GPIO.output(driver_port_1, GPIO.LOW)
    GPIO.output(driver_port_2, GPIO.LOW)


def backward():
    GPIO.output(driver_port_1, GPIO.LOW)
    GPIO.output(driver_port_2, GPIO.HIGH)
    time.sleep(.65)
    GPIO.output(driver_port_1, GPIO.LOW)
    GPIO.output(driver_port_2, GPIO.LOW)


def button_callback(channel):
    if GPIO.input(button_port) == GPIO.HIGH:
        forward()
        time.sleep(5)
        backward()


GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)

while True:
    time.sleep(1)
