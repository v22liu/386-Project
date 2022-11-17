import serial

from plotting import plot_heatmap

# Set COM to the Arduino COM and set baud rate to same val in arduino (ie. Serial.begin(9600);)
arduino_port = 'COM7'  
baud = 9600
ser = serial.Serial(arduino_port, baud, timeout=.1)
ser.close()
ser.open()  # this will also reboot the arduino

positions = [""] * 25
samples = 25
line = 0
while line < samples:
    data = str(ser.readline())[2:][:-5] # the last bit gets rid of the new-line chars
    split_data = ""
    if data:
        split_data = [float(val) for val in data.split(', ')]
        positions[line] = split_data
        line += 1

ser.close()

plot_heatmap(positions)