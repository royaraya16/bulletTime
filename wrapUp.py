#Bullet Time!!! 90 degrees GIF

import time
import sys
import requests
import re
import urllib
import os

from wireless import Wireless

#Iniciando la clase para conexion con camaras
wifi = Wireless('wlan0')

#Lista con ssid de camaras
cameras = ['Bullet_5', 'Bullet_6']

#Funcion para descargar las ultimas 10 imagenes de la camara seleccionada

def getImages(cam):
	
	image = urllib.URLopener()
	
	#Variable con la direccion donde se encuentran las fotos
	adress = "http://10.5.5.9/videos/DCIM/100GOPRO/"
	
	#Descargando toda la informacion desplegada en el url
	r = requests.get(adress)
	
	#Variable con caracteres que forman parte del nombre de las imagenes
	expression = r'"(\w+.JPG)"'
	#Creando un patron con esos caracteres
	pattern = re.compile(expression)
	
	#Buscando en el contenido de la url el patron que corresponde al nombre de las imagenes
	#Los ultimos 10 nombres se guardan en la variable photos como una lista
	photos = re.findall(pattern, r.content)[-10:]
	
	#Contador para el nombre de las imagenes	
	photoCount = 1
	
	#Creando carpeta de la camara
	if not os.path.exists(cam):
		os.makedirs(cam)

	#Recorriendo la lista de nombres
	for item in photos:
		print photoCount
		#Descargando las imagenes
		image.retrieve(adress+item, cam+"/"+str(photoCount)+".jpg")
		photoCount = photoCount + 1
	return;

for camera in cameras:
	print camera
	print "--------------------"
	wifi.connect(ssid=camera, password='goprosession')
	time.sleep(7)
	getImages(camera)
