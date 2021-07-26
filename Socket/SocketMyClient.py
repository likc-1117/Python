import socket,json
import sys



def socketclient():
    client_id='c_001'
    to_client_id='c_002'
    host='127.0.0.1'
    port =2001
    print('>')
    message=input()
    send_msg={'client_id':client_id,'to_client_id':to_client_id,'message':message}
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(json.dumps(send_msg))
    data=s.recv(1024)
    if len(data)>0:
        print('Comunicate is',data)
    s.close()

socketclient()
