import socket

serverPort = 5000

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(("192.168.3.8",serverPort))

print("ready")

while(True):
    message, clientAddress = serverSocket.recvfrom(2048)    
    message = message.upper()
    serverSocket.sendto(message,clientAddress)

serverSocket.close()
