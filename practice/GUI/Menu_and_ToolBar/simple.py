import wx



#---------關於wx.Frame---------------
#wx.Frame的constructor長這樣
#wx.Frame(wx.Window parent, int id=-1, string title='', wx.Point pos=wx.DefaultPosition, 
#    wx.Size size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, string name="frame")
#---------關於wx.Frame---------------


#--------練習修改視窗大小和置中--------------
class example1(wx.Frame):
    def __init__(self,parent,t,x,y):
        super(example1,self).__init__(parent,title=t,size=(x,y))
        self.Centre()
#--------練習修改視窗大小和置中--------------


#--------一個不能最小化的視窗--------------
class example2(wx.Frame):
    def __init__(self,parent,t):
        super(example2,self).__init__(parent,title=t,style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
	| wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
#如果要上他可以最小話就把MINIMIZE_BOX補上就可以了
#--------一個不能最小化的視窗--------------

#------------移動視窗--------------
class example3(wx.Frame):    
    def __init__(self,parent,t):
        super(example3, self).__init__(parent, title=t,size=(300, 200))
        self.Move((100,300))
        
#------------移動視窗--------------

#------------建立manubar和裡面的manu和manuitem--------------
class example4(wx.Frame):    
    def __init__(self,parent,t):
        super(example4, self).__init__(parent, title=t,size=(300, 400))
        self.Centre()
        self.InitUIIII()
        
    def InitUIIII(self):
        menubar=wx.MenuBar()                 #建立MenuBar物件
        fileMenu=wx.Menu()                   #建立Menu物件

        fileItem=fileMenu.Append(wx.ID_EXIT,'Quit','just quit application!')
        #把內容物添加到fileMenu裡面，第一個參數是該menu item的ID  如果填wx.ID_EXIT的話
        #他會自動填寫，第2個參數是menu item顯示的文字, 第三個參數是說明用當游標一過去時

        menubar.Append(fileMenu,'&File')
        #這行是把menu添加到menubar裡面 並且給這個menu一個標題叫做File
        #那File前面的&是怎麼回是?  他是用來標示快捷鍵用的 可以用Alt+F就可以開啟這個menu
        #當按下Alt的時候 會發現F底下有底線~
        #也可以用'Fi&le'這樣快速鍵就要變成按Alt+L

        self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)
        #這裡把這個menuitem和OnQuit這個字定義的method連接再一起
        #這個method可以讓他關掉application
        
        self.SetMenuBar(menubar)
        #當menubar的功能和function設定好了後 呼叫method SetMenuBar() 這是屬於wx.Frame的
        #我想就是在這一步驟把menubar裝上example4這個frame上面
                     
    def OnQuit(self,e):   #對使用者的動作做出反應的方法需要兩個引數。第一個是方法定義於其中的那個物件。
                          #第二個是產生的事件。本例中，我們什麼也不做，只是簡單的關閉我們的程式：
        self.Close()
    
#------------建立manubar和裡面的manu和manuitem--------------

#------------自己玩menubar--------------
class example5(wx.Frame):    
    def __init__(self,parent,t):
        super(example5, self).__init__(parent, title=t,size=(300, 400))
        self.Centre()
        self.InitUIIII()
        
    def InitUIIII(self):
        menubar=wx.MenuBar()                 #建立MenuBar物件
        fileMenu=wx.Menu()                   #建立Menu物件

        fileItem=fileMenu.Append(wx.ID_EXIT,'Quit','just quit application!')
        fileItem2=fileMenu.Append(wx.ID_EXIT,'shaking!','shaking!')

        menubar.Append(fileMenu,'&File')

        self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)
        self.Bind(wx.EVT_MENU,self.shaking,fileItem)
        
        self.SetMenuBar(menubar)

    def OnQuit(self,e):
        self.Close()
    def shaking(self,event=None):
        for i in range(3000):
            self.Move((300,0))
            self.Move((321,123))
            self.Move((0,300))
            
    
#------------自己玩menubar--------------

#------------另一個建立menu item的方法--------------
APP_EXIT=1
class example6(wx.Frame):    
    def __init__(self,parent,t):
        super(example6, self).__init__(parent, title=t,size=(300, 400))
        self.Centre()
        self.InitUI()
    def InitUI(self):
        menubar=wx.MenuBar()                 #建立MenuBar物件
        fileMenu=wx.Menu()                   #建立Menu物件
        item=wx.MenuItem(fileMenu,APP_EXIT,'&Quit\tCtrl+Q')
        #建立MenuItem物件
        #第一個問你要黏在哪個menu下 第2個不知道幹嘛  第3個是名子八  \t代表空格
        item.SetBitmap(wx.Bitmap('icon1.jpg'))
        #加入自訂的icon!!
        fileMenu.Append(item)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu,'&File')
        self.SetMenuBar(menubar)
    
    def OnQuit(self,e):
        self.Close()

#------------另一個建立menu item的方法--------------



#------------submenu的建立方法--------------

class example7(wx.Frame):    
    def __init__(self,parent,t):
        super(example7, self).__init__(parent, title=t,size=(300, 400))
        self.Centre()
        self.InitUI()
    def InitUI(self):
        menubar=wx.MenuBar()                 #建立MenuBar物件
        
        fileMenu=wx.Menu()                   #建立Menu物件
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()           #加入分隔線----------------

        imp = wx.Menu()                      #imp是新定義的submenu
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')

        fileMenu.AppendMenu(wx.ID_ANY,'&Import',imp)  #把submenu加到fileMenu裡面

        fileMenu.AppendSeparator()           #加入分隔線----------------
        
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        qmi.SetBitmap(wx.Bitmap('icon1.jpg'))
        fileMenu.Append(qmi)
        #加入自訂的icon!!

        menubar.Append(fileMenu,'&File')
        self.SetMenuBar(menubar)
    
    def OnQuit(self,e):
        self.Close()

#------------另一個建立menu item的方法--------------



#------------Menu item "check"型態--------------

class example8(wx.Frame):    
    def __init__(self,parent,t):
        super(example8, self).__init__(parent, title=t,size=(300, 400))
        self.Centre()
        self.InitUI()


    def InitUI(self):
        menubar = wx.MenuBar()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(2, 'Show statusbar','Show Statusbar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar','Show Toolbar', kind=wx.ITEM_CHECK)
        #關鍵就是這兩行  在添加item的時候  多置入參數"kind"
        #當kind=wx,ITEM_CHECK的時候，該item就會變成check item，
        #如果不定義kind，python會帶入default值 也就是kind=wx.ITEM_NORMAL        
        #這個Append() method會retuen一個wx.ItemMenu物件
        # ID的部分可以自己給  像我第一個就給2  第2個我讓python自己random給        
        viewMenu.Check(2, True)
        print(self.shst.GetId())
        viewMenu.Check(self.shtl.GetId(), True)
        print(self.shtl.GetId())
        #當程式剛啟動時 我們要希望status bar和toolbar一開始都是visible的話
        #就要先把這兩個item menu給check  用check()方法

        self.toolbar = self.CreateToolBar()   #這應該是wx.frame的widget 這裡沒有解釋
        self.toolbar.AddTool(1, '', wx.Bitmap('icon1.jpg'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready~~~~~~~~')

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
             self.statusbar.Show()
        else:
             self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()
        
#------------Menu item "check"型態--------------


        
#------------建立popup menu-------------------------------------------
class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, 5566, 'Minimize')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, 6666, 'Close')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)


    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()


class example9(wx.Frame):
    
    def __init__(self,parent,t):
        super(example9, self).__init__(parent, title=t,size=(300, 400))
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.SetTitle('Context menu')
        self.Centre()
        
    def OnRightDown(self, e):
        self.PopupMenu(MyPopupMenu(self), e.GetPosition())
        print(e.GetPosition())
        #這行的MyPopupMenu(self)裡面的self 就是example9 這裡告訴MyPopupMenu() example9是你的parent
        #所以剛剛MyPopupMenu裡面的self.parent.Iconize其實就是example9.Iconize   是整個frame縮小 不是Menu縮小
        #第二個參數是popup menu跳出來的位置 因為我希望他跳在游標的所在位置 所以用event object的GetPosition()方法

#------------建立popup menu--------------------------------------------


#--------------------建立toolbar----------------
class example10(wx.Frame):
    def __init__(self,parent,t):
        super(example10,self).__init__(parent, title=t,size=(300, 400))
        self.InitUI()
    def InitUI(self):
        tb1=self.CreateToolBar()
        qtool=tb1.AddTool(wx.ID_ANY,'Quit',wx.Bitmap('icon1.jpg'))
        tb1.Realize()   #這行在linux上不一定需要 可是Windows上一定要
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        tb2=self.CreateToolBar()
        qtool=tb2.AddTool(wx.ID_ANY,'Quit',wx.Bitmap('icon1.jpg'))
        tb2.Realize()   #這行在linux上不一定需要 可是Windows上一定要


        self.Centre()
    def OnQuit(self,e):
        self.Close()                
#--------------------建立toolbar---------------- 


#--------------------建立2個toolbar----------------
class example11(wx.Frame):
    def __init__(self,parent,t):
        super(example11,self).__init__(parent, title=t,size=(300, 400))
        self.InitUI()
    def InitUI(self):
        vbox=wx.BoxSizer(wx.VERTICAL)

        toolbar1=wx.ToolBar(self)
        toolbar1.AddTool(wx.ID_ANY,'',wx.Bitmap('icon1.jpg'))
        toolbar1.AddTool(wx.ID_ANY,'',wx.Bitmap('icon1.jpg'))
        toolbar1.Realize()

        toolbar2=wx.ToolBar(self)
        toolbar2.AddTool(wx.ID_ANY,'',wx.Bitmap('icon2.jpg'))
        toolbar2.Realize()

        vbox.Add(toolbar1,0,wx.EXPAND)
        vbox.Add(toolbar2,0,wx.EXPAND)

        self.SetSizer(vbox)

#--------------------建立2個toolbar----------------    



#--------------------Enable和disable Toolbar的按鈕---------------- 
class example12(wx.Frame):
    def __init__(self,parent,t):
        super(example12,self).__init__(parent, title=t,size=(300, 400))
        self.InitUI()

    def InitUI(self):
        
        self.toolbar=self.CreateToolBar()  
        #之所以什麼東西都要在前面加self.  一定是因為等等要在其他method裡面用!
        tool_undo=self.toolbar.AddTool(wx.ID_UNDO, '', wx.Bitmap('undo.jpg'))
        tool_redo=self.toolbar.AddTool(wx.ID_REDO, '', wx.Bitmap('redo.jpg'))
        self.toolbar.EnableTool(wx.ID_REDO, False) #重點就是這個EnableTool()的method
        self.toolbar.AddSeparator()
        tool_exit=self.toolbar.AddTool(wx.ID_EXIT, '', wx.Bitmap('icon1.jpg'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, tool_exit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tool_undo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, tool_redo)

    def OnUndo(self, e):   #一值按這個按鈕  UNDO按鈕就會不件
        if self.count > 1 and self.count <= 5:
            self.count = self.count - 1

        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, e):
        if self.count < 5 and self.count >= 1:
            self.count = self.count + 1

        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)

        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)


    def OnQuit(self, e):
        self.Close()

#--------------------Enable和disable Toolbar的按鈕---------------- 

 
if __name__=='__main__':
    app=wx.App()
    frame=example12(None,'Darren try try')
    frame.Show()
    app.MainLoop()
