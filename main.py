import wx
import models
from datalist import DataList, TerminalList, CircuitList, UltimateCircuitList


class CTSWindow(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title = "Connector Addition", size=(640,480))
		panel = wx.Panel(self, wx.ID_ANY)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(panel, -1, label = "Connector DWG P/N: ")
		st1.Wrap(200)
		self.connector_part_num = wx.TextCtrl(panel)

		st2 = wx.StaticText(panel, -1, label = "Identified P/N:")
		self.identified_part_num = wx.TextCtrl(panel)

		hbox1.Add(st1, flag = wx.RIGHT, border = 8)
		hbox1.Add(self.connector_part_num, border = 8, proportion = 1)
		hbox1.Add(st2, border = 8)
		hbox1.Add(self.identified_part_num, border = 8, proportion = 1)

		st3 = wx.StaticText(panel, -1, label = "Location: ")
		self.location_tc = wx.TextCtrl(panel)

		st4 = wx.StaticText(panel, -1, label = "Colour")
		self.colour_tc = wx.TextCtrl(panel)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(st3, flag = wx.RIGHT, border = 8)
		hbox2.Add(self.location_tc, border = 8, proportion = 1)
		hbox2.Add(st4, flag = wx.RIGHT, border = 8)
		hbox2.Add(self.colour_tc, border = 8, proportion = 1)

		self.TerminalList = TerminalList(panel)

		vbox.Add(hbox1, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = 10)
		vbox.Add(hbox2, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = 10)
		vbox.Add(self.TerminalList, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = 10)
		panel.SetSizer(vbox)
		self.Show(True)

class CircuitWindow(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title = "Circuit Table", size=(600,800))

		panel = wx.Panel(self, wx.ID_ANY)
		vbox = wx.BoxSizer(wx.VERTICAL)
		# self.CircuitList = CircuitList(panel)
		self.CircuitList = UltimateCircuitList(self)
		vbox.Add(self.CircuitList, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, border = 10)
		panel.SetSizer(vbox)
		self.Show(True)

class MainWindow(wx.Frame):
	def __init__(self, parent, title):

		wx.Frame.__init__(self, parent, title = title, size=(600,800))
		panel = wx.Panel(self, wx.ID_ANY)
		self.lb = DataList(panel)
		self.add_tube()
		self.Show(True)

	def add_tube(self):
		theTube = models.Tubes.get(models.Tubes.id == 1)
		self.lb.Append([theTube.location, '', '', theTube.type 
			+ " " + theTube.diameter, '', theTube.length])

app = wx.App(False)
frame = MainWindow(None, "Hello World")
# frame2 = CTSWindow(None)
frame3 = CircuitWindow(None)
print(models.Tubes.get(models.Tubes.id == 1).diameter)
app.MainLoop()