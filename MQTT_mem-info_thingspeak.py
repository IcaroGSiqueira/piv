import paho.mqtt.publish as publish

import time
from time import localtime, strftime

import psutil #sudo apt install python3-psutil
import subprocess 

SERVER = "mqtt.thingspeak.com"

CHANNEL_ID = "1044535"
WRITE_API_KEY = "3DA656M1HS6ZO0E5"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY


sleep = 5 # Intervalo em segundos de cada postagem
key = "HQISCJAU87GQL8PB"  # Thingspeak API key

while True:
    # Leitura dos sensores
	mem = psutil.virtual_memory()

	cpu_temp =	psutil.sensors_temperatures(fahrenheit=False)
	gpu_temp = subprocess.check_output(["nvidia-settings", "-q", "gpucoretemp", "-t"])

	hd_tmp = None
	try:
		hd_tmp = subprocess.check_output(["sudo", "smartctl", "-A", "/dev/sda"])
	except subprocess.CalledProcessError as e:
		hd_tmp = e.hd_tmp

	ssd_tmp = None
	try:
		ssd_tmp = subprocess.check_output(["sudo", "smartctl", "-A", "/dev/nvme0"])
	except subprocess.CalledProcessError as e:
		ssd_tmp = e.ssd_tmp

	# Tratamento de valores
	names = list(cpu_temp.keys())
	if names[2] in cpu_temp:
		for entry in cpu_temp[names[2]]:
			#print("%s %s°C" % (entry.label, entry.current))
			break
	cpu_temp = entry.current

	gpu_temp = gpu_temp.decode("utf-8")
	gpu_temp = gpu_temp.split("\n")

	hd_tmp = hd_tmp.decode("utf-8")
	hd_tmp = hd_tmp.split("\n")
	hd_tmp = hd_tmp[19]
	dummy, hd_tmp = hd_tmp.split("-")
	hd_tmp = hd_tmp.strip(" ")

	ssd_tmp = ssd_tmp.decode("utf-8")
	ssd_tmp = ssd_tmp.split("\n")
	ssd_tmp = ssd_tmp[6]
	dummy, ssd_tmp = ssd_tmp.split(":")
	ssd_tmp = ssd_tmp.strip(" Celscius")

	try:
		# Printa os valores enviados, data e status da conexão
		print("Memoria:", mem.available)
		print("CPU Temp: ", cpu_temp)
		print("GPU Temp:", gpu_temp[0])
		print("HD Temp:", hd_tmp)
		print("SSD Temp:",ssd_tmp)

		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

		params = "field1="+str(mem.available)+"&field2="+str(cpu_temp)+"&field3="+str(gpu_temp[0])+"&field4="+str(hd_tmp)+"&field5="+str(ssd_tmp)

		publish.single(topic, payload=params, hostname=SERVER, port=1883, tls=None, transport="tcp")

	except:
		print("connection failed") # Em caso de erro de conexão

	time.sleep(sleep)