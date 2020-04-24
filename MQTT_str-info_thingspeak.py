import paho.mqtt.publish as publish

import time
from time import localtime, strftime

import psutil #sudo apt install python3-psutil
import subprocess 

SERVER = "mqtt.thingspeak.com"

CHANNEL_ID = "1044535"
WRITE_API_KEY = "UCGURXQSV8FXK6JF"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

sleep = 300 # Intervalo em segundos de cada postagem

while True:
    # Leitura dos sensores

	str_ssd = psutil.disk_usage('/')
	str_hd = psutil.disk_usage('/home')

	batt = psutil.sensors_battery()

	try:
		# Printa os valores enviados, data e status da conexão
		print("HD:", str_hd.used)
		print("SSD:",str_ssd.used)
		print("Battery:", batt.percent)

		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

		params = "field1="+str(str_hd.used)+"&field2="+str(str_ssd.used)+"&field3="+str(batt.percent)

		publish.single(topic, payload=params, hostname=SERVER, port=1883, tls=None, transport="tcp")

	except:
		print("connection failed") # Em caso de erro de conexão
	
	time.sleep(sleep)