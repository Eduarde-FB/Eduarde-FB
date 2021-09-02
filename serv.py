#!/usr/bin/python
# Coded by: Eduarde David Freitas Brandão
# Contact: edudavid47@gmail.com
#


import urllib.parse
import urllib.request   
import socket
import time
from datetime import datetime

ip = '192.168.0.199'
port = 80
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr)

#envia  caracter especifico no socket
client_socket.sendall("\a".encode())
 
result = client_socket.recv(10000)
now = datetime.now()
ano = str(now.year)
mes = str(now.month)
dia = str(now.day)
hora = str(now.hour)
minutos = str(now.minute)
segundos = str(now.second)

arquivo = open('dados.txt', 'at')
dados = str('Dia: '+ dia+'/'+mes+'/'+ano+' '+ 'Horario: '+hora+':'+minutos+':'+segundos+'\n')
arquivo.write(dados)
	
while (len(result) > 0):
    
    imprimir = result.decode()
    print(imprimir)
    arquivo.write(imprimir)
      
    result = client_socket.recv(10000)

arquivo.write('\n')
time.sleep(2.0)
arquivo.close()   
client_socket.close()
