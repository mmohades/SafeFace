#!/usr/bin/env python
import RPi.GPIO as GPIO
from driver import main
from time import sleep
from lcd_controller import write_lcd

TouchPin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

touched = False


def loop():

    global touched
    while True:
        if GPIO.input(TouchPin) == GPIO.LOW:
            touched = False
        else:
            print("Touched")
            write_lcd("take_pic")
            touched = True
            result = main()
            write_lcd(result["status"])
            sleep(2)


def destroy():
    GPIO.cleanup()                     # Release resource


if __name__ == '__main__':     # Program start from here
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
