import http.client
import os
import threading
import sys

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ip = conn.getresponse().read()

def Starter():
	os.system("python timer.py")
	
def Closer():
	q = input("Exit:    ")
	q = q.upper()
	if q == "E":
		file = open("close.txt","w")
		file.write("1")
		file.close()
		
def Binput(b,mode):
	bin = open("message.bin",mode)
	bin.write(b)
	bin.close()
	
def Newstr():
	st = open("message.bin","a")
	st.write("\n")
	st.close()
	
print("you can choese mod: \n[S]et time\n[M]essage")
mod = input("input mod [S/M]:	")
mod = mod.upper()

if mod == "M":
	message = input("Input message:	")
	Binput(ip,"wb")
	Newstr()
	Binput(bytes(message,"utf-8"),"ab")
	
if mod == "S":
	timeH = input("Set time H:    ")
	timeH = float(timeH)
	timeH = timeH*60*60
	
	file = open("time.txt","w")
	file.write(str(timeH))
	file.close()
	
	thread1 = threading.Thread(target=Starter)
	thread2 = threading.Thread(target=Closer)
 
	thread1.start()
	thread2.start()
 
	thread1.join()
	thread2.join()