import paho.mqtt.publish as publish

import time
from time import localtime, strftime

import psutil #sudo apt install python3-psutil
import subprocess 

SERVER = "mqtt.thingspeak.com"

CHANNEL_ID = "1044535"
WRITE_API_KEY = "3T2HQB2FUCZ95Z4D"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

sleep = 59 # Intervalo em segundos de cada postagem
key = "HQISCJAU87GQL8PB"  # Thingspeak API key

net_sts = 0 
old_value = 0

while True:
    # Leitura dos sensores
	cpu_percent = psutil.cpu_percent(interval=1)
	cpu_freq = psutil.cpu_freq(percpu=False)

	gpu_freq = subprocess.check_output(["nvidia-settings", "-q", "GPUCurrentClockFreqs", "-t"])
	gpu_mem = subprocess.check_output(["nvidia-settings", "-q", "UsedDedicatedGPUMemory", "-t"])
	gpu_percent = subprocess.check_output(["nvidia-settings", "-q", "GPUUtilization", "-t"])

	old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
	time.sleep(1)
	new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
	net_sts = new_value - old_value

	# Tratamento de valores
	gpu_freq = gpu_freq.decode("utf-8")
	gpu_freq = gpu_freq.split("\n")
	gpu_freq = gpu_freq[0].split(",")

	gpu_mem = gpu_mem.decode("utf-8")
	gpu_mem = gpu_mem.split("\n")

	gpu_percent = gpu_percent.decode("utf-8") 
	gpu_percent = gpu_percent.split("\n")
	gpu_percent = gpu_percent[0].split(",")
	gpu_percent = gpu_percent[0].split("=")

	try:
		# Printa os valores enviados, data e status da conexão
		print("CPU %:", cpu_percent)
		print("CPU Hz:", cpu_freq.current)
		print("GPU Hz:", gpu_freq[0])
		print("GPU Memory:", gpu_mem[0])
		print("GPU %:", gpu_percent[1])
		print("Net:", net_sts)

		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

		params = "field1="+str(gpu_percent[1])+"&field2="+str(cpu_percent)+"&field3="+str(cpu_freq.current)+"&field4="+str(gpu_mem[0])+"&field5="+str(gpu_freq[0])+"&field6="+str(net_sts)

		publish.single(topic, payload=params, hostname=SERVER, port=1883, tls=None, transport="tcp")

	except:
		print("connection failed") # Em caso de erro de conexão

	time.sleep(sleep)
