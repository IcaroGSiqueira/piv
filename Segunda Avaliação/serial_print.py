import serial
import time

serial = serial.Serial("/dev/tnt0",9600)
#serial.close()

while True:
	serial.write(b'b')
	time.sleep(1)

