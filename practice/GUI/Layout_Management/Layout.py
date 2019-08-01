import wx

#---------------------把照片放在panel上的固定位置--------------------
class example1(wx.Frame):
    def __init__(self,parent,ti):
        super(example1,self).__init__(parent=parent,title=ti,size=(1100,700))
        self.initUI()

    def initUI(self):
        panel = wx.Panel(self)                 #裝在這個frame上的panel
        panel.SetBackgroundColour("yellow")        #設定顏色
        yabi = wx.StaticBitmap(panel, wx.ID_ANY,  wx.Bitmap("yabi1.jpg", wx.BITMAP_TYPE_ANY))
        #把照片放在panel上
        yabi.SetPosition((20, 50))  #設定照片的絕對位置
#---------------------把照片放在panel上的固定位置--------------------

#---------------------使用sizer 就是可以縮東西--------------------
class example2(wx.Frame):
    def __init__(self,parent,ti):
        super(example2,self).__init__(parent=parent,title=ti,size=(1100,700))
        self.initUI()

    def initUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049') #先把背景弄一個顏色

        vbox=wx.BoxSizer(wx.VERTICAL)        #定義上下放的sizer

        mid_panel=wx.Panel(panel)
        mid_panel.SetBackgroundColour('#ededed')  #在建立一個有色的面板
  
        vbox.Add(mid_panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 22)
        #把面板放入sizer 並且設定邊界的距離是22  ，如果把wx.ALL改成wx.TOP就代表只有上面有邊界
        #有wx.TOP wx.BOTTOM  wx.RIGHT  wx.LEFT wx.ALL可以選
        #wx.EXPAND
        panel.SetSizer(vbox)

    def OnQuit(self,e):
        self.Close()

#---------------------使用sizer 就是可以縮東西--------------------


#----------------------sizer進階應用-------------------
class example3(wx.Frame):
    def __init__(self,parent,ti):
        super(example3,self).__init__(parent=parent,title=ti,size=(1100,700))
        self.initUI()

    def initUI(self):
        panel=wx.Panel(self)
        
        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)                         #把font大小改成9

        vbox=wx.BoxSizer(wx.VERTICAL)
       #-------------------------hbox1----------------------------------  
        hbox1=wx.BoxSizer(wx.HORIZONTAL)
        st1=wx.StaticText(panel,label='Class Name')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        # Add是BoxSizer的Method
        #Add(self, item, proportion=0, flag=0, border=0, userData=None)
        #用來把child item安裝到sizer上
        #下面來解釋一下每個參數在做什麼
        # 1. item: 可以是wx.windows的instance(instance=object),另外一個sizer object
        #          或是spacer
        # 2. Proportion(integer): 用來表示child tool可不可以隨著sizer一起改變形狀
        #                         當他=0代表不隨之改變，=1代表可以跟著改變, =2代表比其他child改得更多
        # 3. Flag: wx.EXPAND: item會把分配給他的space塞滿

        
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)  #proportion=1代表大小隨之起舞
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))   #這在幹嘛  用來加入分隔的 是一個長方形框(x,y)  
        #-------------------------hbox2----------------------------------  
        hbox2=wx.BoxSizer(wx.HORIZONTAL)
        st2=wx.StaticText(panel,label='Matching class')
        st2.SetFont(font)
        hbox2.Add(st2)

        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))             
        #-------------------------hbox3---------------------------------- 
        hbox3=wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel,style=wx.TE_MULTILINE,size=(500,260))  #大的布告欄
        #這個TextCtrl支援許多style 如下(不只這些)
        #wx.HSCROLL: 會出現水平的滾動軸
        #wx.TE_NO_VSCROLL:絕對不會出現vertical滾動軸
        #wx.TE_CENTRE:文字出現在中間
        #當size填(-1,-1)代表是default size
        #pos=-1代表是default的位置
        hbox3.Add(tc2, proportion=0)   
        
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 25))
        #-------------------------hbox4----------------------------------

        hbox4=wx.BoxSizer(wx.HORIZONTAL)
        cb1=wx.CheckBox(panel,label='Case Sensitive')  #parent=panel代表是parent window  不可以是NONE       
        cb1.SetFont(font)   #因為cb1的爸爸是wx.control  而wx.Control的爸爸是wx.Window 是所以可以用wx.Window的method
        cb1.SetForegroundColour('yellow')  #我去查wx.Window還有什麼method可用
        hbox4.Add(cb1,proportion=1)
        cb2 = wx.CheckBox(panel, label='Nested Classes')
        cb2.SetFont(font)
        hbox4.Add(cb2,proportion=1)
        cb3 = wx.CheckBox(panel, label='Math Classes')
        cb3.SetFont(font)
        hbox4.Add(cb3,proportion=1)
        
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 25))

        #-------------------------hbox5----------------------------------

        hbox5=wx.BoxSizer(wx.HORIZONTAL)
        bt1=wx.Button(panel,label='OK',size=(66,33))
        hbox5.Add(bt1,proportion=1)
        bt2=wx.Button(panel,label='Delete',size=(66,33))
        hbox5.Add(bt2,proportion=1,flag=wx.LEFT|wx.BOTTOM,border=5)

        vbox.Add(hbox5, proportion=1,flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)



        panel.SetBackgroundColour('#FF7733')  #代表R紅色=0xFF B藍色=0x77 G綠色=0x33 每個顏色是0~255階
        panel.SetSizer(vbox) #Sets the window to have the given layout sizer.
                             #wx.Panel的爸爸是wx.control的爸爸是wx.Window 這是wx.Window的method


#----------------------sizer進階應用-------------------


#----------------------wx.GridSizer應用-------------------
class example4(wx.Frame):
    def __init__(self,parent,ti):
        super(example4,self).__init__(parent=parent,title=ti,size=(1100,700))
        self.initUI()       

    def initUI(self):
      
        panel=wx.Panel(self)
       
        menubar = wx.MenuBar()
        fileMenu=wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(panel,id=wx.ID_ANY, style=wx.TE_RIGHT)
        #wx.TextCtrl是一個顯示文字的框框  Style=TE_RIGHT讓字體會靠右

        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.LEFT, border=10)

        gs = wx.GridSizer(5, 4, 10, 10)
        #wx.GridSizer(int rows=1, int cols=0, int vgap=0, int hgap=0)
        #從construcor可以看出 這是一個5x4的grid  彼次間隔都是5

        #~~~~~~這一小段是特製第一個按鈕~~~~~~
        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)
        bt1=wx.Button(panel, label='Cls')
        bt1.SetFont(font)
        #~~~~~~這一小段是特製第一個按鈕~~~~~

        
        gs.AddMany( [ (bt1, 0, wx.EXPAND),  
                     (wx.Button(panel, label='Bck'), 0, wx.EXPAND),
                      (wx.StaticText(panel), wx.EXPAND),
                    (wx.Button(panel, label='Close'), 0, wx.EXPAND),
                    (wx.Button(panel, label='7'), 0, wx.EXPAND),
                    (wx.Button(panel, label='8'), 0, wx.EXPAND),
                    (wx.Button(panel, label='9'), 0, wx.EXPAND),
                    (wx.Button(panel, label='/'), 0, wx.EXPAND),
                    (wx.Button(panel, label='4'), 0, wx.EXPAND),
                    (wx.Button(panel, label='5'), 0, wx.EXPAND),
                    (wx.Button(panel, label='6'), 0, wx.EXPAND),
                    (wx.Button(panel, label='*'), 0, wx.EXPAND),
                    (wx.Button(panel, label='1'), 0, wx.EXPAND),
                    (wx.Button(panel, label='2'), 0, wx.EXPAND),
                    (wx.Button(panel, label='3'), 0, wx.EXPAND),
                    (wx.Button(panel, label='-'), 0, wx.EXPAND),
                    (wx.Button(panel, label='0'), 0, wx.EXPAND),
                    (wx.Button(panel, label='.'), 0, wx.EXPAND),
                    (wx.Button(panel, label='='), 0, wx.EXPAND),
                    (wx.Button(panel, label='+'), 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.LEFT, border=10)

        panel.SetBackgroundColour('#FF7733')
        panel.SetSizer(vbox)
#----------------------wx.GridSizer應用-------------------


#----------------------wx.FlexGridSizer應用-------------------
class example5(wx.Frame):
    def __init__(self,parent,ti):
        super(example5,self).__init__(parent=parent,title=ti,size=(1100,700))
        self.initUI()       

    def initUI(self):
      
        panel=wx.Panel(self)
        hbox=wx.BoxSizer(wx.HORIZONTAL)

        fgs=wx.FlexGridSizer(3,2,9,25)
        title=wx.StaticText(panel,label='Title')
        author=wx.StaticText(panel,label='Author')
        review=wx.StaticText(panel,label='Review')

        tc1=wx.TextCtrl(panel)
        tc2=wx.TextCtrl(panel)
        tc3=wx.TextCtrl(panel,style=wx.TE_MULTILINE)

        fgs.AddMany([(title),(tc1,1,wx.EXPAND),
                    (author),(tc2,1,wx.EXPAND),
                    (review),(tc3,1,wx.EXPAND),])

        fgs.AddGrowableRow(2, 1) #這讓第三個row的高度可以隨windows大小變化
        fgs.AddGrowableCol(1, 1) #這讓第2個column的寬度 可以隨windows大小變化

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
              
        panel.SetBackgroundColour('#EF7733')
        panel.SetSizer(hbox)

        
#----------------------wx.FlexGridSizer應用------------------- 


#----------------------wx.GridBagSizer應用-------------------
class example6(wx.Frame):
    def __init__(self,parent,ti):
        super(example6,self).__init__(parent=parent,title=ti)
        self.initUI()       

    def initUI(self):
        panel=wx.Panel(self) #self=example6這個wx.frame的odject
        s=wx.GridBagSizer(4,4)

        text=wx.StaticText(panel,label='Rename To')
        s.Add(text,pos=(0,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=5) #在4x4的格子中 我占用最坐上角(0,0)

        tc=wx.TextCtrl(panel)
        s.Add(tc,pos=(1,0),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT ,border=5) #在4x4中 占用(1,0) 他的大小有(1,5)這麼大

        buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
        buttonClose = wx.Button(panel, label="Close", size=(90, 28))
        s.Add(buttonOk, pos=(3, 3))
        s.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=10)

        s.AddGrowableRow(2) #讓第3 row的高度可以改變
        s.AddGrowableCol(1) #讓第2 colum的寬度可以改變
        panel.SetSizer(s)
        panel.SetBackgroundColour('#EF7733')
#----------------------wx.GridBagSizer應用-------------------


#----------------------wx.GridBagSizer進階應用-------------------
class example6(wx.Frame):
    def __init__(self,parent,ti):
        super(example6,self).__init__(parent=parent,title=ti)
        self.initUI()
    def initUI(self):
        
        panel=wx.Panel(self) 
        sizer=wx.GridBagSizer(5,5)

        text1 = wx.StaticText(panel, label="Tranzor Factory Automating Test")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('icon1.jpg'))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="Serial Number")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)

        text3 = wx.StaticText(panel, label="Test Case")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND,border=5)

        button1 = wx.Button(panel, label="Browse...")
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)

        text4 = wx.StaticText(panel, label="Extends")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        combo = wx.ComboBox(panel)
        sizer.Add(combo, pos=(4, 1), span=(1, 3),flag=wx.TOP|wx.EXPAND, border=5)

        button2 = wx.Button(panel, label="Browse...")
        sizer.Add(button2, pos=(4, 4), flag=wx.TOP|wx.RIGHT, border=5)

        sb = wx.StaticBox(panel, label="Optional")

        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.CheckBox(panel, label="Including Path Loss"),flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Tx testing only"),flag=wx.LEFT|wx.BOTTOM, border=5)
        
        sizer.Add(boxsizer, pos=(5, 0), span=(1, 5),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        button3 = wx.Button(panel, label='Help')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)
        
        button4 = wx.Button(panel, label="Ok")
        sizer.Add(button4, pos=(7, 3))
        
        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(7, 4), span=(1, 1),flag=wx.BOTTOM|wx.RIGHT, border=10)

        sizer.AddGrowableCol(2)  #讓他可以變胖
        sizer.AddGrowableRow(5)  #讓Optional Attributes那個框框可以變高

        
        panel.SetSizer(sizer)
        sizer.Fit(self)          #加這行會讓整體不會有浪費的空間
        panel.SetBackgroundColour('#AF7733')
        
#----------------------wx.GridBagSizer進階應用------------------- 
if __name__=='__main__':
    MyAPP=wx.App()
    x=example6(None,'Darrens Layout')
    x.Show()
    MyAPP.MainLoop()
