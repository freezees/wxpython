import wx
import wx.lib.newevent

MyEvent, EVT_MY_EVENT = wx.lib.newevent.NewEvent()

EVT_ANOTHER_EVENT_TYPE = wx.NewEventType()
EVT_ANOTHER_EVENT = wx.PyEventBinder(EVT_ANOTHER_EVENT_TYPE, 1)

class EventTest(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(210, 200))

        wx.Button(self, 1, 'NewEvent', (50, 10), (110, -1))
        wx.Button(self, 2, 'PyCommandEvent', (50, 60), (110, -1))
        wx.Button(self, 3, 'Close', (50, 110), (110, -1))

        self.Bind(wx.EVT_BUTTON, self.OnNewEvent, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnPyCommandEvent, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=3)

        self.Bind(EVT_MY_EVENT, self.NewEventHandler)
        self.Bind(EVT_ANOTHER_EVENT, self.PyCommandEventHandler)

        self.Centre()
        self.ShowModal()
        self.Destroy()

    def OnNewEvent(self, event):
        evt = MyEvent(SomeData="5566",pig=(5,6))
        wx.PostEvent(self, evt)

    def OnPyCommandEvent(self, event):
        evt = wx.PyCommandEvent(EVT_ANOTHER_EVENT_TYPE, wx.ID_ANY)
        evt.SetClientData(("PyCommandEvent", 22, "bbb"))
        wx.PostEvent(self, evt)

    def NewEventHandler(self, evt=None):
        print ("NewEvent Data: {0} {1}".format(evt.SomeData,evt.pig))

    def PyCommandEventHandler(self, evt=None):
        print ("PyCommandEvent Data:", evt.GetClientData())

    def OnClose(self, event):
        self.Close(True)

if __name__ == "__main__":
    app = wx.App(0)
    EventTest(None, -1, 'Event Test')
    app.MainLoop()
