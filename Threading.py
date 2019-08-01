import wx
import time
import threading
import wx.lib.newevent

#-----------20190801 關於使用新event的方法 我把步驟寫出來標注在旁邊-------------#

Darren, EVT_Darren=wx.lib.newevent.NewEvent()   #Step 1: 建立新的event種類   
# EVT_Darren就是一個新的event type如同wx.EVT_BUTTON
# Darren是一個class的概念  之後可以用Darren來創event的instance




class GUI(wx.Frame):
    def __init__(self):  
        super(GUI,self).__init__(parent=None)
        self.initUI()
        
    def initUI(self):
        
        panel=wx.Panel(self)
        bt1=wx.Button(panel,label='start long task',pos=(50,50),id=1)
        self.Bind(wx.EVT_BUTTON,self.Onbt1,id=1)

        bt2=wx.Button(panel,label='test',pos=(200,50),id=2)
        self.Bind(wx.EVT_BUTTON,self.Onbt2,id=2)

        bt3=wx.Button(panel,label='stop',pos=(300,50),id=3)    #Step3 建立stop按鈕
        self.Bind(wx.EVT_BUTTON,self.OnStop,id=3)              #Step4 按下去後會觸發OnStop method

        self.stop_running=0                           #一開始default 不要stop

        self.Bind(EVT_Darren,self.ReturnData)         #Step11 發回來的event要和一個method(event handler)綁再一起
        
    def Onbt1(self,e):
        self.worker=WorkThread(self)                  #Step6:多加這個參數Self就是為了把GUI class也丟給WorkerThread 因為等等postevent要用到 還有stop_running也要傳進去
        self.worker.start()                           #這東西會連接到workThread去執行run method
        print(self.worker)

    def Onbt2(self,e):
        print(self.worker.isAlive())                  #isAlive()可以用來看Thread來是不是活著

    def OnStop(self,e):                               #Step5,OnStop method只是把這個flag設定成1   
        self.stop_running=1

    def ReturnData(self,e):                           #step12: 當GUI主視窗發現這個新的event出現後 會執行下面動作         
        print('This is data from WorkThread=',e.pig)  #Step13:同時因為event有夾帶data，所以這裡可以把WorkThred處理的data透過這個新event來這裡取出
    

class WorkThread(threading.Thread): 
    def __init__(self,winnn):                         #Step7 當GUI把self也傳過來 這裡也要拿東西接阿 就隨便用個參數接住
        super(WorkThread,self).__init__()      
        self.windowss=winnn                           #Step8 你知道為什麼一把傳進來的GUI Class 要變成self.windowss嗎?  因為不這樣做run method那邊沒辦法直接用winnn.stop_running
    def run(self):
        evt=Darren(pig="you are pig")                 #Step2: 在這裡用Darren建立evt 有點像是建立class的instance的感覺 建立在這是因為等等要從這裡把event發回去
        
        for i in range(6):
            time.sleep(1)
            print("computing! {} sec".format(i))
            if self.windowss.stop_running==1:         #Step9: 當我運算到一半時候 會不斷的檢查這個flag有沒有被人設定為1
                print('stop here')
                wx.PostEvent(self.windowss,evt)       #Step10: 當發現flag==1 這裡把Darren這個新event發回去給GUI class
                return                                #post完event後 在跳出run


def main():
    MyApp=wx.App()
    MyGUI=GUI()      #創建GUI這個class的instance
    MyGUI.Show()     #沒有這行 面板就不會顯示在螢幕上
    MyApp.MainLoop()


if __name__=="__main__": 
    main()
