import serial
from models import plant


def processRequest(serial_port, seconds):
    sendRequestTo(serial_port, seconds)
    return None


def sendRequestTo(serial_port, seconds):
    arduino = serial.Serial(serial_port)
    arduino.write(serial.unicode(seconds))
    waitForData(arduino)


def waitForData(arduino):
    while True:
        line = arduino.readline()
        break
    return line.decode()
