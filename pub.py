import time, socket, sys
import ast
    
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 4455
socket_server.connect((server_host, sport))
#print('This is your IP address: ',ip)



socket_server.send("0".encode())
topic = input('Enter Topic Name:')
#val = input("Enter Message")

key_val = topic#+","+val


socket_server.send(key_val.encode())

while True:
    val = input("Enter Message")
    socket_server.send(val.encode())

 
    


socket_server.close()
