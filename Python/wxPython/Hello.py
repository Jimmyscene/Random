import wx
class MyApp(wx.App):
	def OnInit(self):
		wx.MessageBox("Hello wxPython")
		return True
if __name__ == '__main__':
	app = MyApp(False)
	app.MainLoop()