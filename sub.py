import time, socket, sys
import ast

    
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 4455
socket_server.connect((server_host, sport))
#print('This is your IP address: ',ip)

FORMAT = "utf-8"
SIZE = 1024


socket_server.send("1".encode())
topic = input('Enter Topic Name:')

key_val = topic

socket_server.send(key_val.encode())

offset = socket_server.recv(SIZE).decode(FORMAT)
print("Your initial offset is",offset)
while True:
    socket_server.send(offset.encode())
    #print("Sent stuff")

    message = socket_server.recv(SIZE).decode(FORMAT)
    #print("message is: ",message)
    message = message.split(',')
    offset = message[0]
    message = message[1]
    #print("Recieved stuff")
    print(message)
    continue

 
    

print("Exiting")
socket_server.close()
