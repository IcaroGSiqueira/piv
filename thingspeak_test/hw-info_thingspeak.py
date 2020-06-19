import urllib #sudo apt install python3-urllib3
from time import localtime, strftime
import psutil #sudo apt install python3-psutil
import subprocess 
import time
import http.client # sudo apt install python3-httplib2
 
sleep = 90 # Intervalo em segundos de cada postagem
key = 'HQISCJAU87GQL8PB'  # Thingspeak API key

while True:
    # Leitura dos sensores
	cpu_percent = psutil.cpu_percent(interval=1)
	cpu_freq = psutil.cpu_freq(percpu=False)
	mem = psutil.virtual_memory()
	cpu_temp =	psutil.sensors_temperatures(fahrenheit=False)
	gpu_temp = subprocess.check_output(["nvidia-settings", "-q", "gpucoretemp", "-t"])
	gpu_freq = subprocess.check_output(["nvidia-settings", "-q", "GPUCurrentClockFreqs", "-t"])
	gpu_mem = subprocess.check_output(["nvidia-settings", "-q", "UsedDedicatedGPUMemory", "-t"])
	gpu_percent = subprocess.check_output(["nvidia-settings", "-q", "GPUUtilization", "-t"])

	# Tratamento de valores
	names = list(cpu_temp.keys())
	if names[2] in cpu_temp:
		for entry in cpu_temp[names[2]]:
			#print("%s %s°C" % (entry.label, entry.current))
			break
	cpu_temp = entry.current

	gpu_temp = gpu_temp.decode("utf-8")
	gpu_temp = gpu_temp.split("\n")

	gpu_freq = gpu_freq.decode("utf-8")
	gpu_freq = gpu_freq.split("\n")
	gpu_freq = gpu_freq[0].split(",")

	gpu_mem = gpu_mem.decode("utf-8")
	gpu_mem = gpu_mem.split("\n")

	gpu_percent = gpu_percent.decode("utf-8") 
	gpu_percent = gpu_percent.split("\n")
	gpu_percent = gpu_percent[0].split(",")
	gpu_percent = gpu_percent[0].split("=")

	# Criação da linha com os campos do canal
	params = urllib.parse.urlencode({'field1': mem.available, 'field2': cpu_percent, 'field3': cpu_freq.current, 'field4': cpu_temp, 'field5': gpu_temp[0], 'field6': gpu_freq[0], 'field7': gpu_mem[0], 'field8': gpu_percent[1], 'key':key}) 
	# Cria variaveis para conexão
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = http.client.HTTPConnection("api.thingspeak.com:80")

	time.sleep(sleep)

	try:
		conn.request("POST", "/update", params, headers) # Faz a conexão
		response = conn.getresponse() # Retorno da Conexão
		# Printa os valores enviados, data e status da conexão
		print(mem.available)
		print(cpu_percent)
		print(cpu_freq.current)
		print(cpu_temp)
		print(gpu_temp[0])
		print(gpu_freq[0])
		print(gpu_mem[0])
		print(gpu_percent[1])

		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

		print(response.status, response.reason)

		data = response.read()
		conn.close() # Termina conexão
	except:
		print("connection failed") # Em caso de erro de conexão
		