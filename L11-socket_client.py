import socket
from threading import Thread
import tkinter as tk

serverName = "192.168.3.8"
serverPort = 5000

def receive_msg(sock,addr):
    sock.connect((serverName,serverPort))
    print("start thread")
    while True:
        receivedMessage = sock.recvfrom(2048)
        print(receivedMessage[0])
        entry2.delete(0,tk.END)
        entry2.insert(0,receivedMessage[0])
        window.update()

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
Thread(target=receive_msg, args=(clientSocket, (serverName,serverPort)), daemon=True).start()


def send_msg():
    global var
    message = entry.get()
    clientSocket.sendto(message.encode(),(serverName,serverPort))

window = tk.Tk()

window.title("網路聊天軟體")
window.geometry("500x150")
window.resizable(False,False)

label = tk.Label(window,text = "請輸入傳送文字")
label.pack()

entry = tk.Entry(window, width = 50)
entry.pack()

button = tk.Button(window, text = "傳送",command = send_msg)
button.pack()

label2 = tk.Label(window,text = "接收到的文字")
label2.pack()

entry2 = tk.Entry(window, width = 50)
entry2.pack()

window.mainloop()
