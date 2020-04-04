import urllib
from time import localtime, strftime
import psutil
import time
import http.client
 
sleep = 30 
key = 'HQISCJAU87GQL8PB'  # Thingspeak API key
 
def doit():
	cpu_percent = psutil.cpu_percent(interval=1)
	cpu_freq = psutil.cpu_freq(percpu=False)
	mem = psutil.virtual_memory()
	cpu_temp =	psutil.sensors_temperatures(fahrenheit=False)

	names = list(cpu_temp.keys())
	if names[2] in cpu_temp:
		for entry in cpu_temp[names[2]]:
			#print("%s %s°C" % (entry.label, entry.current))
			break
	cpu_temp = entry.current

	params = urllib.parse.urlencode({'field1': cpu_percent, 'field2': mem.available, 'field3': cpu_freq.current, 'field4': cpu_temp,'key':key}) 
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = http.client.HTTPConnection("api.thingspeak.com:80")
	time.sleep(1)

	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print(cpu_percent)
		print(mem.available)
		print(cpu_freq.current)
		print(cpu_temp)
		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		print(response.status, response.reason)
		data = response.read()
		conn.close()
	except:
		print("connection failed")
 
if __name__ == "__main__":
	while True:
		doit()
		time.sleep(sleep)