from socket import *
import pandas as pd
import numpy as np
import ast
from _thread import *
import os



IP = gethostbyname(gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

PORT2 = 4456
PORT3 = 4457
ADDR2 = (IP,PORT2)
ADDR3 = (IP,PORT3)

#topic_data = {}


def thread_pub(conn,topic):
    '''
    message = conn.recv(SIZE).decode(FORMAT)
    message = message.split(",",1)
    topic = message[0]
    value = message[1]

    
    file_name = topic+".txt"
    f = open(file_name, "a")
    f.write(value+"\n")
    f.close()
    '''
    file_name = topic+".txt"

    while True:
        value = conn.recv(SIZE).decode(FORMAT)

        curr_part = 0
        curr_f = open("topics/"+topic+".txt",'r')
        curr_part= str((int(curr_f.read()) )%3 + 1)
        curr_f.close()

        curr_f = open("topics/"+topic+".txt",'w')
        curr_f.write(curr_part)
        curr_f.close()
        '''
        if curr_part == "3":
            socket_server = socket(AF_INET, SOCK_STREAM)
            socket_server.connect(ADDR2)
            socket_server.send("rand".encode())
            print(socket_server.recv(SIZE).decode())
            message = topic+","+message
            socket_server.send(message.encode())
            socket_server.close()
            continue
        elif curr_part == "1":
            socket_server = socket(AF_INET, SOCK_STREAM)
            socket_server.connect(ADDR3)
            socket_server.send("rand".encode())
            print(socket_server.recv(SIZE).decode())
            message = topic+","+message
            socket_server.send(message.encode())
            socket_server.close()
            continue
        '''

        socket_server1 = socket(AF_INET, SOCK_STREAM)
        socket_server1.connect(ADDR2)
        socket_server1.send("rand".encode())
        print(socket_server1.recv(SIZE).decode())
        message = curr_part+","+topic+","+value # partition number , topic , message
        socket_server1.send(message.encode())
        socket_server1.close()

        socket_server2 = socket(AF_INET, SOCK_STREAM)
        socket_server2.connect(ADDR3)
        socket_server2.send("rand".encode())
        print(socket_server2.recv(SIZE).decode())
        message = curr_part+","+topic+","+value # partition number , topic , message
        socket_server2.send(message.encode())
        socket_server2.close()


        
        file_name = "broker1"+"/"+topic+"/part"+curr_part+".txt"

        f = open(file_name, "a")
        f.write(value+"\n")
        f.close()


    


def thread_sub(conn,topic):
    #topic = conn.recv(SIZE).decode(FORMAT)
    #print(topic)
    #message = "Your current offset is 0"
    #conn.send(message.encode())
    #print("Hello")
    while True:
        off = int(conn.recv(SIZE).decode(FORMAT))
        curr = -1
        while(True):
        
            f = open(topic+".txt", "r")
            f.seek(0, 2)
            curr = f.tell()
            #print(curr,off)
            if curr>off:
                break
        

    
        f.seek(off)
        message = str(curr) + "," +f.read()
        #print("pipe")
        conn.send(message.encode())
        f.close()

        #print("pipe2")
   





def main():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("Server is listening")
    topic_port = {}
    producer = []

    while True:
        conn, addr = server.accept()
        print(f"{addr} connected")
        type_client = conn.recv(8).decode(FORMAT)
        if type_client=='0':
            print("We recieved Publisher at port",addr[1])
            topic = conn.recv(SIZE).decode(FORMAT)

            newpath1 = "broker1/"+topic
            newpath2 = "broker2/"+topic
            newpath3 = "broker3/"+topic

            if not os.path.exists(newpath1):
                os.mkdir(newpath1)
                os.mkdir(newpath2)
                os.mkdir(newpath3)

            f = open("topics/"+topic+".txt",'w')
            f.write("2")
            f.close()
            start_new_thread(thread_pub,(conn,topic,))
        elif type_client == '1':
            print("We received Subscriber at port",addr[1])
            topic = conn.recv(SIZE).decode(FORMAT)
            
            file_name = topic+".txt"
            f = open(file_name, "a")
            f.close()
            f = open(file_name, "r")
            f.seek(0, 2)
            curr = f.tell()
            conn.send(str(curr).encode())


            start_new_thread(thread_sub,(conn,topic,))
        else :
            accepted = "accepted"
            conn.send(accepted.encode())
            message = conn.recv(SIZE).decode(FORMAT)
            message = message.split(',',2)
            part = message[0]
            topic = message[1]
            mess = message[2] 
            file_name = "broker1"+"/"+topic+"/part"+part+".txt"
            f = open(file_name, "a")
            f.write(mess+"\n")
            f.close()
            conn.close()

        

if __name__ == "__main__":
    main()
