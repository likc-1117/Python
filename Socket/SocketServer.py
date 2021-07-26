import socket,json
import pickle

def SocketServer():
    HOST='127.0.0.1'
    PORT=8006
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen(2)
    while True:
        conn,addr=s.accept()
        print('address is ', addr)
        while True:
            data=conn.recv(1024)
            print(data)
            if 'Goto_NumPhone_By_Finger' in str(data):
                conn.send('Waring'.encode(encoding='utf-8',errors='strict'))
            elif 'CheckWaring' in str(data):
                conn.send('False'.encode(encoding='utf-8',errors='strict'))
            elif 'SideKey' in str(data):
                conn.send('SideKey OK'.encode(encoding='utf-8'))
            elif 'Goto_Press_Finger' in str(data):
                conn.send('press Ok'.encode(encoding='utf-8',errors='strict'))
            elif 'Goto_Finger' in str(data):
                conn.send('Goto_Finger OK'.encode(encoding='utf-8',errors='strict'))
            else:
                conn.send('Stylue_Reset'.encode(encoding='utf-8',errors='strict'))
            #client_data=json.loads(data)
            #print(client_data)
            if not data:break
        conn.close()



SocketServer()
#SocketClient()