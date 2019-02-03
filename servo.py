import RPi.GPIO as GPIO
from time import sleep

servo_pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)  # GPIO 17 for PWM with 50Hz
p.start(0)

order = {"open": 0, "close": 100}
locked = True


def set_angle(angle):

    duty = angle / 18 + 2

    print("angle: {} and duty: {} ".format(angle, duty))
    GPIO.output(servo_pin, True)
    p.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servo_pin, False)
    p.ChangeDutyCycle(0)


def unlock():
    global locked
    set_angle(90)
    print("Unlocked")
    locked = False


def lock():
    global locked
    set_angle(0)
    print("Locked")
    locked = True


#----------------------------------------------------------------


# from flask import Flask, jsonify, request
# import json

# app = Flask(__name__)


# def get_data():

#     with open('data.json', 'r') as fp:
#         data = json.load(fp)

#     stat = ""

#     if close:
#         stat = "close"
#     else:
#         stat = "open"

#     data["dariche"] = stat
#     return jsonify(data)


# @app.route('/dariche/open', methods=['GET'])
# def open_dariche():

#     global close

#     if close:
#         set_angle(order["open"])
#         close = False
#         return "Succesfully opened dariche."
#     else:
#         return "Dariche is already opened."


# @app.route('/dariche/close', methods=['GET'])
# def close_dariche():

#     global close

#     if not close:
#         set_angle(order["close"])
#         close = True
#         return "Succesfully closed dariche."
#     return "Dariche is already closed."


# @app.route('/room/status', methods=['GET'])
# def status():

#     return get_data()


# @app.route('/room/update', methods=['POST'])
# def update_data():

#     data = request.args.to_dict()
#     with open('data.json', 'w') as fp:
#         json.dump(data, fp)
#     return "Success"


# if __name__ == '__main__':
#     # app.run(debug=True)
#     app.run(host='0.0.0.0', debug=True)
