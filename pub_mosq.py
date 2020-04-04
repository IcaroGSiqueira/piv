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

yn = "n"

yn = input("Deseja digitar as informaçoes? (y/n) ")

if yn == "y":
    ip = input("Digite o ip: ")
    topic = input("Digite a topico: ")
    user = input("Digite o usuario(0 se nao necessario): ")
    passw = input("Digite a senha(0 se nao necessario): ")

mesg = "null"

mesg = input("Digite a mensagem: ")

if user == "0":
    	os.system("mosquitto_pub -h %s -t %s -m \"%s\""%(ip,topic,mesg))
else:
	os.system("mosquitto_pub -h %s -t %s -u %s -P %s -m \"%s\""%(ip,topic,user,passw,mesg))
