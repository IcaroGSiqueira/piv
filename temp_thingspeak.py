import urllib2
import time

import sys
import RPi.GPIO as GPIO
from time import sleep
import urllib2

a = 0
b = 1
c = 0
baseURL = 'https://api.thingspeak.com/update?api_key=HQISCJAU87GQL8PB&field1=0'

while(a < 10):
	print(a)
	f = urllib2.urlopen(baseURL +str(a))
	f.read()
	f.close()
	sleep(5)
	c = a
	a = a + b
	b = c 	
print("Program has ended")
