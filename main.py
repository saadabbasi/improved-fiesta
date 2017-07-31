import wx
import models
from datalist import DataList

class MainWindow(wx.Frame):
	def __init__(self, parent, title):

		wx.Frame.__init__(self, parent, title = title, size=(600,800))
		panel = wx.Panel(self, wx.ID_ANY)
		self.lb = DataList(panel)
		self.add_tube()
		self.Show(True)

	def add_tube(self):
		theTube = models.Tubes.get(models.Tubes.id == 1)
		self.lb.Append([theTube.location, '', '', theTube.type + " " + theTube.diameter, '', theTube.length])

app = wx.App(False)
frame = MainWindow(None, "Hello World")
print(models.Tubes.get(models.Tubes.id == 1).diameter)
app.MainLoop()