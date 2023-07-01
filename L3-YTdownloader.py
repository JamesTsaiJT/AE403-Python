#匯入pytube模組內的YouTube
from pytube import YouTube

#def showProgress(stream,chunk,file_handle,bytes_remaining):
#
#        size = stream.filesize
#        
#        currentProgress = (size - bytes_remaining)*100 / size
#        
#        print("目前進度： " + str(currentProgress) + "%")

#定義全域變數，儲存目前下載進度
progress = 0        
#定義進度條函式 
def showProgress(stream,chunk,bytes_remaining):
        #總檔案大小
        size = stream.filesize
        #上次執行showProgress的進度
        global progress
        preProgress = progress
        #目前下載進度(總大小-剩餘大小)除總大小 = 已下載百分比
        currentProgress = (size - bytes_remaining)*100 // size
        progress = currentProgress
        
        if progress == 100:
            print("下載完成！")
            return
        #若上次進度不等於本次進度才輸出，以免洗評
        if preProgress != progress:
            print("目前進度： " + str(progress) + "%")
        
#建立YouTube物件，並指定on_progress_callback函式
yt = YouTube("https://www.youtube.com/watch?v=K5rjNK_De-I&ab_channel=%E5%8D%8E%E8%AF%AD%E6%AD%8C%E6%9B%B2%E9%A2%91%E9%81%93",on_progress_callback=showProgress)
#從yt內的所有串流中，篩選出只有音樂的串流，並從此串流抓出第一個串流
stream = yt.streams.filter(only_audio=True).first()
#下載串流，並選擇資料夾及檔案名稱
stream.download("youtube",yt.title + " music only")
