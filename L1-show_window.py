import tkinter as tk
import tkinter.messagebox

def clickButton():
    tkinter.messagebox.showinfo(title = "提示", message = "好痛")

window = tk.Tk()

window.title("我的第一個GUI程式")
window.geometry("300x300")
label = tk.Label(window, text = "我的GUI", bg="#05A",fg="#5FC")
label.pack()

entry = tk.Entry(window, width = 20)
entry.pack()

button = tk.Button(window, text = "按鈕", command = clickButton)
button.pack()
window.mainloop()






"""
label = tk.Label(window, text = "我的GUI")
label.pack()

entry = tk.Entry(window, width = 20)
entry.pack()

#button = tk.Button(window, text = "按鈕")
#button.pack()

#window.mainloop()



import tkinter.messagebox

def clickButton():
    tkinter.messagebox.showinfo(title = "提示", message = "好痛")

button = tk.Button(window, text = "按鈕", command = clickButton)
button.pack()

label = tk.Label(window, text = "我的GUI", bg="#05A",fg="#5FC")
label.pack()

window.mainloop()
"""