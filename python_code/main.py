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

test_positions = [[1100.0, 1100.0, 92.08], [1300.0, 1100.0, 125.18], [1500.0, 1100.0, 28.91], [1700.0, 1100.0, 56.61], [1900.0, 1100.0, 98.39], [1900.0, 1300.0, 14.27], [1700.0, 1300.0, 99.37], [1500.0, 1300.0, 84.26], [1300.0, 1300.0, 11.59], [1100.0, 1300.0, 74.55], [1100.0, 1500.0, 26.82], [1300.0, 1500.0, 121.3], [1500.0, 1500.0, 133.7], [1700.0, 1500.0, 70.13], [1900.0, 1500.0, 108.08], [1900.0, 1700.0, 124.37], [1700.0, 1700.0, 120.36], [1500.0, 1700.0, 19.67], [1300.0, 1700.0, 24.08], [1100.0, 1700.0, 61.16], [1100.0, 1900.0, 28.91], [1300.0, 1900.0, 165.72], [1500.0, 1900.0, 124.78], [1700.0, 1900.0, 121.56], [1900.0, 1900.0, 0.93]]
plot_heatmap(positions)