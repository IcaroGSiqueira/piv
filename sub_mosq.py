import os
import subprocess
import time

#ip = "200.132.103.53"
ip = "test.mosquitto.org"

#topic = "piv"
topic = "1883"

#user = "middleware"
user = "0"

#passw = "exehda"
passw = "0"

yn = input("Deseja digitar as informaçoes? (y/n) ")

if yn == "y":
	ip = input("Digite o ip: ")
	topic = input("Digite a topico: ")
	user = input("Digite o usuario(0 se nao necessario): ")
	passw = input("Digite a senha(0 se nao necessario): ")

if user == "0":
	os.system("mosquitto_sub -h %s -t %s"%(ip,topic))
else:
	os.system("mosquitto_sub -h %s -t %s -u %s -P %s"%(ip,topic,user,passw))

#try:
	#test = subprocess.Popen(["mosquitto_sub -h %s -t %s"%(ip,topic)], shell=True)
	#test = subprocess.check_output(["mosquitto_sub","-h","%s"%ip,"-t","%s"%topic])
	#print(test)
	#if 'not authorised' in test:
	#	print("if")
	#	pass
	#else:
	#	os.system("mosquitto_sub -h %s -t %s"%(ip,topic))
#except:
#	print("ex")
#	os.system("mosquitto_sub -h %s -t %s -u %s -P %s"%(ip,topic,user,passw))
