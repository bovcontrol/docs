# INSTALAR DEPENTENCIA:
#
# pip install pyserial

import serial
import requests

bovcontrol = 'http://api.staging.bovcontrol.com/ioc/v1/wearable/data'

# LINUX
#arduino = serial.Serial('/dev/ttyUSB0', 9600)

# MAC
#arduino = serial.Serial('/dev/tty.usbserial-A603RTGW', 9600)

# WINDOWS
arduino = serial.Serial('COM3', 9600)

information = {'token':'uCszjIpDMb2NCm2Z', 'data' : {'weight': 0}}

while True:
	information['data']['weight'] = arduino.readline().rstrip()
	print information
	requests.post(bovcontrol, json=information)
