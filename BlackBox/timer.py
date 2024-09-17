import time
import webbrowser
import requests

mess = open("message.bin","rb")
message = mess.read()
message = message.decode("utf-8")

TOKEN = "" # Впишите токен.
chat_id = "" # Впишите чат айди.

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"


file = open("time.txt","r")
reader = file.read()
file.close()
reader = float(reader)
timing = time.time()



while True:
    clo = open("close.txt","r")
    readclo = clo.read()
    clo.close()
    if len(readclo) != 0:
    	clo = open("close.txt","w")
    	clo.write("")
    	exit(0)
    if time.time() - timing > reader:
        for i in range(10):
        	print(requests.get(url).json())
        exit(0)