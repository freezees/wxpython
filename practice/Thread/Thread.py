import time
from threading import *
import wx

# Button definitions
ID_START = wx.NewId()
ID_STOP = wx.NewId()

# Define notification event for thread completion
EVT_RESULT_ID = 99 #為自創EVENT定義新ID 例如EVT


def EVT_RESULT1(win, func):  #這東西我覺得跟bind很像  今天之所以不在MainFrame裡面做  是因為要做成global 所以
    """Define Result Event."""
    
    win.Connect( -1,-1,99, func)

    
def EVT_RESULT2(win, func):  #這東西我覺得跟bind很像  今天之所以不在MainFrame裡面做  是因為要做成global 所以
    """Define Result Event."""
    
    win.Connect( -1,-1,55, func)
    
    #win.Connect(-1, -1, EVT_RESULT_ID, func)
    #這個.connect method是 wx.EvtHandler的(wx.Window的媽媽，)wx.EvtHandler是一個class可以用來接收win的event
    #Connect(self, id, lastId, eventType, func)
    #Make an entry in the dynamic event table for an event binding.

class ResultEvent(wx.PyEvent):  #字創的EVENT?
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(99)
        self.data = data

# Thread class that executes processing
class WorkerThread(Thread):
    """Worker Thread Class."""
    def __init__(self,notify_window): #這個notify_window是把self.frame(instance of MainFrame)這個東西傳進來
        """Init Worker Thread Class."""
        Thread.__init__(self)
        #super(WorkerThread,self).__init__(self)
        
        self.nw = notify_window
        self._want_abort = 0
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()

    def run(self):  #這是build in method
        """Run Worker Thread."""
        # This is the code executing in the new thread. Simulation of
        # a long process (well, 10s here) as a simple loop - you will
        # need to structure your processing so that you periodically
        # peek at the abort variable
        for i in range(10):
            time.sleep(1)
            print(i)
            if self._want_abort:
                # Use a result of None to acknowledge the abort (of
                # course you can use whatever you'd like or even
                # a separate event type)
                wx.PostEvent(self.nw, ResultEvent(None))
                
                return
        # Here's where the result would be returned (this is an
        # example fixed result of the number 10, but it could be
        # any Python object)
        wx.MessageBox("complete!!", 'Info~~', wx.OK | wx.ICON_ERROR)
    def pp(self,e):
        print("pp")

    def abort(self):
        """abort worker thread."""
        # Method for use by main thread to signal an abort
        self._want_abort = 1

# GUI Frame class that spins off the worker thread
class MainFrame(wx.Frame):
    """Class MainFrame."""
    def __init__(self, parent, id):
        """Create the MainFrame."""
        wx.Frame.__init__(self, parent, id, 'Thread Test')

        # Dumb sample frame with two buttons
        wx.Button(self, ID_START, 'Start', pos=(0,0))
        wx.Button(self, ID_STOP, 'Stop', pos=(0,50))
        self.status = wx.StaticText(self, -1, '', pos=(0,150))

        self.Bind(wx.EVT_BUTTON, self.OnStart, id=ID_START)
        self.Bind(wx.EVT_BUTTON, self.OnStop, id=ID_STOP)


        # Set up event handler for any worker thread results
        EVT_RESULT2(self,self.OnResult)
        EVT_RESULT1(self,self.OnResult)
        # And indicate we don't have a worker thread yet
        self.worker = None
        wx.Button(self, label='Test', pos=(0,100), id=55)
        self.Bind(wx.EVT_BUTTON, self.Test,id=55)


    def Test(self,e):
        wx.MessageBox(".connect是這樣用的阿", 'Info', wx.OK | wx.ICON_INFORMATION)
        
    def OnStart(self, event):
        """Start Computation."""
        # Trigger the worker thread unless it's already busy
        if not self.worker:
            self.status.SetLabel('Starting computation')
            self.worker = WorkerThread(self)

    def OnStop(self, event):
        """Stop Computation."""
        # Flag the worker thread to stop if running
        if self.worker:
            self.status.SetLabel('Trying to abort computation')
            self.worker.abort()

    def OnResult(self, event):
        """Show Result status."""
        if event.data is None:
            # Thread aborted (using our convention of None return)
            self.status.SetLabel('Computation aborted')
        else:
            # Process results here
            self.status.SetLabel('Computation Result: %s' % event.data)
        # In either event, the worker is done
        self.worker = None

class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        """Init Main App."""
        self.frame = MainFrame(None, -1)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()
