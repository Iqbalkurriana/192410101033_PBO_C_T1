import wx
import helloWxGui

class subClass(helloWxGui.MyFrame1):
	def __init__(self, parent):
		helloWxGui.MyFrame1.__init__(self,parent)
	
	def m_button1OnButtonClick( self, event ):
		print('''		HELLO WX 
		Iqbal Kurriana Putra 
		192410101033''')
		

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()
