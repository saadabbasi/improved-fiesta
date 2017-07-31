import wx
import wx.lib.mixins.listctrl as listmix

class DataList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin, listmix.ColumnSorterMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__( self, parent, -1, size=(600,800), style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
		self.InsertColumn(0, "Loc")
		self.InsertColumn(1, "Part Dwg #")
		self.InsertColumn(2, "Identified Part #")
		self.InsertColumn(3, "Description")
		self.InsertColumn(4, "Maker")
		self.InsertColumn(5, "Qty")

