import socket

serverName = "192.168.3.8"
serverPort = 5000

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = input("input:")
    
clientSocket.sendto(message.encode(),(serverName,serverPort))

receivedMessage, serverAddress = clientSocket.recvfrom(2048)
print(receivedMessage)
    
    
clientSocket.close()
