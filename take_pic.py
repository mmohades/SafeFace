from picamera import PiCamera
from time import sleep
import os


def main(image_name):
    camera = PiCamera()
    try:
        os.remove(image_name)
    except Exception as e:
        print(e)
    camera.start_preview()
    sleep(5)
    camera.capture(image_name)
    camera.stop_preview()
    camera.close()

    return image_name
