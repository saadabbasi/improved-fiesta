import wx
import wx.lib.mixins.listctrl as listmix
import wx.lib.agw.ultimatelistctrl as ULC
import models
from ObjectListView import ObjectListView

class ConnectorList(wx.ListCtrl):
	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, -1, size=(-1,600),style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.LC_VRULES)

		self.InsertColumn(0, "id")
		self.InsertColumn(1, "DWG P/N")
		self.InsertColumn(2, "Identified P/N")
		self.InsertColumn(3, "Color")
		self.InsertColumn(4, "Location")
		self.InsertColumn(5, "Description")

class CircuitList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin, listmix.ColumnSorterMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__( self, parent, -1, size=(-1,600), style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.LC_VRULES)

		helvetica_Font = wx.Font(10,wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Helvetica')
		self.SetFont(helvetica_Font)

		self.InsertColumn(0, "id")
		self.InsertColumn(1, "CKT A")
		self.InsertColumn(2, "CKT B")
		self.InsertColumn(3, "Wire Type")
		self.InsertColumn(4, "Wire Colour")
		self.InsertColumn(5, "Wire Gauge")
		self.SetItemCount(1)

		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self)

	def OnClick(self, event):
		currentItem = event.GetIndex()
		print(self.GetItemText(currentItem))

	def OnGetItemText(self, item, column):
		theCkt = models.Circuits.get(models.Circuits.id == item+1)

		return_values = {1:theCkt.circuit_a,
				2:theCkt.circuit_b,
				3:theCkt.wire_type,
				4:theCkt.wire_colour,
				5:theCkt.wire_gauge,
				0:str(theCkt.id)}

		return return_values[column]
	
	def OnGetItemAttr(self, item):
		return None

	def OnGetItemImage(self, item):
		return -1