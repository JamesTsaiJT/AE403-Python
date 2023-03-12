#匯入tkinter模組
import tkinter as tk

"""創建基本視窗"""
window = tk.Tk()

window.title("Menu")

window.geometry("500x500")

"""Menu"""
menuBar = tk.Menu(window)

#檔案->第二層視窗
fileMenu = tk.Menu(menuBar,tearoff=False) #起始tear虛線

fileMenu.add_command(label="開新遊戲")

fileMenu.add_command(label="作弊指令")
#分隔線
fileMenu.add_separator()

fileMenu.add_command(label="Exit")
#設定好檔案的第二層視窗後，再包進檔案目錄內
menuBar.add_cascade(label="檔案  ",menu=fileMenu)

#選項->第二層視窗
fileMenu2 = tk.Menu(menuBar,tearoff=False)

fileMenu2.add_command(label="遊戲設定")

fileMenu2.add_command(label="畫面設定")

#選項->進階設定->第三層視窗
subMenu = tk.Menu(menuBar,tearoff=False)

subMenu.add_command(label="遊戲優化Max")

subMenu.add_command(label="攻擊所有敵人")
#設定好選項->進階設定->第三層視窗後，再包進進階設定目錄內
fileMenu2.add_cascade(label="進階設定",menu=subMenu)
#設定好選項->第二層視窗後，再包進選項目路內
menuBar.add_cascade(label="選項  ",menu=fileMenu2)

#修改window屬性，把我們設定好的menu放進去
window.config(menu=menuBar)

#開始跑視窗
window.mainloop()