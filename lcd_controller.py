import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)
status = {"locked": '1', "unlocked": '2', "take_pic": '3', "not_auth": '4'}


def write_lcd(current_stat):
    try:

        ser.write(status[current_stat].encode())
        print("yes")

    except KeyboardInterrupt as e:
        exit()

    except Exception as e:
        print("error: {}".format(e))
