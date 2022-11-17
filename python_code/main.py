import serial
import math
import time

from datetime import datetime

# Set COM to the Arduino COM and set baud rate to same val in arduino (ie. Serial.begin(9600);)
arduino_port = 'COM7'  
baud = 9600
ser = serial.Serial(arduino_port, baud, timeout=.1)
ser.close()
ser.open()  # this will also reboot the arduino



def read(ser):
    data = str(ser.readline())[2:][:-5] # the last bit gets rid of the new-line chars
    split = ""
    if data:
        split = [float(val) for val in data.split(',')]
    return data, split if split else data


def csv(data, file, line=0):
    timestamp = datetime.strftime(datetime.now(), '%Y, %m, %d, %H, %M, %S.%f') + ','
    print('Line ' + str(line) + ': writing...' + timestamp + data)
    file.write(timestamp + data + '\n')