import socket

serverPort = 5000

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(("192.168.3.8",serverPort))

print("ready")

while(True):
    message, clientAddress = serverSocket.recvfrom(2048)   
    print(message.decode())
    if(message.decode() == "request"):
        message = "Liam is good boy"
        serverSocket.sendto(message.encode(),clientAddress)
    else:
        message = "Liam is bad boy"
        serverSocket.sendto(message.encode(),clientAddress)
    print(message)

serverSocket.close()
