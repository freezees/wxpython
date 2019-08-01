import wx
#------------------Bind練習1-------------------
class Example1(wx.Frame):

    def __init__(self,p,t):
        super(Example1, self).__init__(parent=p,title=t)
        self.InitUI()

    def InitUI(self):

        wx.StaticText(self, label='x:', pos=(10,10))
        wx.StaticText(self, label='y:', pos=(10,30))

        self.st1 = wx.StaticText(self, label='', pos=(30, 10))
        self.st2 = wx.StaticText(self, label='', pos=(30, 30))

        self.Bind(wx.EVT_MOVE, self.OnMove)
        #Here we bind the wx.EVT_MOVE event binder to the OnMove() method.
        #wx.EVT_MOVE是個EVENT binder
        #他的工作就是把move這個event type 和 event handler(self.OnMove)串起來 

        self.SetSize((350, 250))
        self.SetTitle('Move event')
        self.Centre()

    def OnMove(self, e):

        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))  #改變顯示的文字
        self.st2.SetLabel(str(y))
#------------------Bind練習1-------------------



#------------------防止誤關視窗-------------------
#在這個例子中 當你按下程式右上角的X  就會跳出訊息說 你真的要關閉嗎
        
class Example2(wx.Frame):

    def __init__(self,p,t):
        super(Example2, self).__init__(parent=p,title=t)
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow) #在執行close event的時候 我們做一個method叫做OnCloseWindow


    def OnCloseWindow(self,e):
        dial = wx.MessageDialog(None,'Are u really want to quit?','Questions',wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)

        ret=dial.ShowModal()

        if ret==wx.ID_YES:
            self.Destroy()  #此時不能用Close() method 不然會無限迴圈
        else:
            e.Veto()        #當我們要中斷某個event的進行的時候  用Veto這個方法

        
        
#------------------防止誤關視窗-------------------


#------------------EVENT propagation-------------------
class MyPanel(wx.Panel):

    def __init__(self, *args, **kw):
        super(MyPanel, self).__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):

        print('event reached panel class')
        e.Skip()


class MyButton(wx.Button):

    def __init__(self, *args, **kw):
        super(MyButton, self).__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):

        print('event reached button class')
        e.Skip()


class Example3(wx.Frame):

    def __init__(self, p,t):
        super(Example3, self).__init__(parent=p,title=t)
        self.InitUI()


    def InitUI(self):

        mpnl = MyPanel(self)                  #這裡告訴你MyPanel的媽媽是Example3

        MyButton(mpnl, label='Ok', pos=(15, 15)) #這裡告訴妳MyButton的媽媽是Mypanel

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)  #當我按下去的時候 會先觸發button裡面定義的method 再來一路往上找

 
        self.Centre()

    def OnButtonClicked(self, e):

        print('event reached frame class')
        e.Skip()
            
          
#------------------EVENT propagation-------------------


#------------------ID的用法-------------------
class Example4(wx.Frame):

    def __init__(self, p,t):
        super(Example4, self).__init__(parent=p,title=t)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        exitButton = wx.Button(pnl, wx.ID_ANY, 'Exit', (10, 10))
        Button2 = wx.Button(pnl, wx.ID_ANY, 'button2', (10, 50))

        self.Bind(wx.EVT_BUTTON,  self.OnExit, exitButton.GetID() )
        #在binding的時候加入ID 代表只有這個bind只限定這個button
        #如果我把這個指名的ID拿掉 也就是把 "exitButton.GetID()"從上面拿掉  你會發現
        #當你按所有的按鈕 都會讓程式結束  也就是所有按鈕的event都會觸發self.OnExit

        

        self.SetTitle("Automatic ids")
        self.Centre()


    def OnExit(self, event):
        self.Close()



#------------------ID的用法-------------------


#------------------Standard ID的用法-------------------
class Example5(wx.Frame):

    def __init__(self, p,t):
        super(Example5, self).__init__(parent=p,title=t)

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        grid = wx.GridSizer(3, 2,1,1)
        #wx.GridSizer(int rows=0, int cols=0, int vgap=0, int hgap=0)

        grid.AddMany([(wx.Button(pnl, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_DELETE), 0, wx.TOP, 9),
            (wx.Button(pnl, wx.ID_SAVE), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_EXIT)),
            (wx.Button(pnl, wx.ID_STOP), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_NEW))])

        self.Bind(wx.EVT_BUTTON, self.OnQuitApp, id=wx.ID_EXIT)

        pnl.SetSizer(grid)
        pnl.SetBackgroundColour('#FF7733')

        self.SetTitle("Standard ids")
        self.Centre()

    def OnQuitApp(self, event):

        self.Close()


        
#------------------Standard ID的用法-------------------
        
#------------------自訂億 ID的用法-------------------

ID_MENU_NEWWW=123
ID_MENU_OPENN=456
ID_MENU_SAVEE=789

class Example6(wx.Frame):

    def __init__(self, p,t):
        super(Example6, self).__init__(parent=p,title=t)

        self.InitUI()

    def InitUI(self):
        self.CreateMenuBar()
        self.CreateStatusBar()

    def CreateMenuBar(self):
        Darren_MB=wx.MenuBar()
        fMenu=wx.Menu()
        fMenu.Append(ID_MENU_NEWWW, 'New')
        fMenu.Append(ID_MENU_OPENN, 'OPENNNN')
        fMenu.Append(ID_MENU_SAVEE, 'SAVE')


        Darren_MB.Append(fMenu,'&File')
        self.SetMenuBar(Darren_MB)  #把menubar裝在自己的wx.Frame的object  "example6"之下

        self.Bind(wx.EVT_MENU,self.DisplayShit,id=123)  #wx.EVT_MENU代表按下menu裡東西的事件
        self.Bind(wx.EVT_MENU,self.DisplayShit,id=456)  #wx.EVT_MENU代表按下menu裡東西的事件
        self.Bind(wx.EVT_MENU,self.DisplayShit,id=789)  #wx.EVT_MENU代表按下menu裡東西的事件


    def DisplayShit(self,e):

        sb=self.GetStatusBar()
        
        eid=e.GetId()

        if eid==123:
            msg='New menu item select!'
        if eid==456:
            msg='OPEN menu item select!'
        if eid==789:
            msg='SAVE menu item select!'


        sb.SetStatusText(msg)

        

#------------------自訂億 ID的用法-------------------

#------------------PAINT Event-------------------
        #好像失敗了
class Example7(wx.Frame):

    def __init__(self, p,t):
        super(Example7, self).__init__(parent=p,title=t)
        self.InitUI()

    def InitUI(self):
        self.count = 0
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self,e):
        self.count=self.count+1
        dc = wx.PaintDC(self)
        text= "Number of paint events: {0}".format(self.count)
        dc.DrawText(text,20,20)
        
        
#------------------PAINT Event-------------------

#------------------FOCUS Event-------------------

class MyWindow(wx.Panel):
        def __init__(self, parent):
            super(MyWindow, self).__init__(parent)

            self.color = '#b3b3b3'

            self.Bind(wx.EVT_PAINT, self.OnQuit)
            #self.Bind(wx.EVT_SIZE, self.OnSize)
            #self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
            #self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
            self.Refresh()
        def OnQuit(self,e):
            print('???')
            

        def OnPaint(self, e):
            print('paint')
            dc = wx.PaintDC(self)

            #dc.SetPen(wx.Pen(self.color))
            x, y = self.GetSize()
            
            dc.DrawRectangle(33, 33, x-50, y-50)  #用這個來畫一個長方形 前兩個參數是position 後兩個是長方形的長寬
 
        def OnSize(self, e):
            print('size')
            #self.Refresh()

        def OnSetFocus(self, e):

            self.color = '#ff0000'
            #self.Refresh()

        def OnKillFocus(self, e):

            self.color = '#b3b3b3'
            #self.Refresh()


        

class Example8(wx.Frame):

    def __init__(self, p,t):
        super(Example8, self).__init__(parent=p,title=t)
        self.InitUI()

    def InitUI(self):

        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.RIGHT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 9)])
        self.SetSizer(grid)

    
            

#------------------FOCUS Event-------------------

def main():

    app = wx.App()
    ex = Example8(None,'This is a practice of EVENT')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main() 
