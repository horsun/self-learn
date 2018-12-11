import wx

TITLE = 'basic_root'


# app_icon ='icon path'
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, TITLE, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()


class MainApp(wx.App):
    def OnInit(self):
        self.SetAppName(TITLE)
        self.Frame = MainFrame()
        self.Frame.Show()
        return True


if __name__ == '__main__':
    app = MainApp(redirect=True, filename='debug.txt')
    app.MainLoop()
