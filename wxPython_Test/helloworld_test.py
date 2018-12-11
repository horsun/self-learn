import wx

app = wx.App()
# 新建一个窗体 frame
frame = wx.Frame(None, title='basic frame test', size=(300, 400))

# 新建一个panel基于frame 窗体
panel = wx.Panel(frame)

# 新建一个label标签在panel上
label = wx.StaticText(panel, label='Hello World!!!')

frame.Show()
app.MainLoop()
