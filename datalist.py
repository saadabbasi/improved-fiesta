import wx
import wx.lib.mixins.listctrl as listmix
import wx.lib.agw.ultimatelistctrl as ULC
import models
from ObjectListView import ObjectListView

class DataList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin, listmix.ColumnSorterMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__( self, parent, -1, size=(600,800), style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
		self.InsertColumn(0, "Loc")
		self.InsertColumn(1, "Part Dwg #")
		self.InsertColumn(2, "Identified Part #")
		self.InsertColumn(3, "Description")
		self.InsertColumn(4, "Maker")
		self.InsertColumn(5, "Qty")


class TerminalList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin, listmix.ColumnSorterMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__( self, parent, -1, size=(600,100), style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
		self.InsertColumn(0, "P/N")
		self.InsertColumn(1, "Wire Seal P/N")
		self.InsertColumn(2, "Circuit")
		self.InsertColumn(3, "Wire")

class OLVCircuitList(ObjectListView):
	def __init__(self, parent):
		ObjectListView.__init__(self, parent, wx.ID_ANY, style = wx.LC_REPORT|wx.LC_VIRTUAL, cellEditMode = ObjectListView.CELLEDIT_DOUBLECLICK)

	def OnGetItemText(self, item, column):
		theCkt = models.Circuits.get(models.Circuits.id == item+1)
		if column == 1:
			return theCkt.circuit_a
		elif column == 2:
			return theCkt.circuit_b
		elif column == 3:
			return theCkt.wire_type
		elif column == 4:
			return theCkt.wire_colour
		elif column == 5:
			return theCkt.wire_gauge
		elif column == 0:
			return str(theCkt.id)

class UltimateCircuitList(ULC.UltimateListCtrl):
	def __init__(self, parent):
		ULC.UltimateListCtrl.__init__(self, parent, wx.ID_ANY, size = (600,600), agwStyle = ULC.ULC_REPORT|ULC.ULC_VIRTUAL)
		# listmix.TextEditMixin.__init__(self)
		self.InsertColumn(0, "id")
		self.InsertColumn(1, "CKT A")
		self.InsertColumn(2, "CKT B")
		self.InsertColumn(3, "Wire Type")
		self.InsertColumn(4, "Wire Colour")
		self.InsertColumn(5, "Wire Gauge")

		self.Bind(ULC.EVT_LIST_BEGIN_LABEL_EDIT, self.OnClick, self)
		self.SetItemCount(6)

	def OnClick(self, event):
		print("OK")

	def OnGetItemText(self, item, column):
		theCkt = models.Circuits.get(models.Circuits.id == item+1)
		if column == 1:
			return theCkt.circuit_a
		elif column == 2:
			return theCkt.circuit_b
		elif column == 3:
			return theCkt.wire_type
		elif column == 4:
			return theCkt.wire_colour
		elif column == 5:
			return theCkt.wire_gauge
		elif column == 0:
			return str(theCkt.id)

	def OnGetItemTextColour(self, item, column):
		return None

	def OnGetItemToolTip(self, item, column):
		return "Rabbia"

class CircuitList(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin, listmix.ColumnSorterMixin, listmix.TextEditMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__( self, parent, -1, size=(600,600), style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.LC_HRULES)
		listmix.TextEditMixin.__init__(self)

		helvetica_Font = wx.Font(10,wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Helvetica')
		self.SetFont(helvetica_Font)

		self.InsertColumn(0, "id")
		self.InsertColumn(1, "CKT A")
		self.InsertColumn(2, "CKT B")
		self.InsertColumn(3, "Wire Type")
		self.InsertColumn(4, "Wire Colour")
		self.InsertColumn(5, "Wire Gauge")
		self.SetItemCount(5)

		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self)

	def SetVirtualData(self, curRow, curCol, text):
		theId = self.GetItemText(curRow,col=0)
		theCkt = models.Circuits.get(models.Circuits.id == theId)
		if curCol == 1:
			theCkt.circuit_a = text
		elif curCol == 2:
			theCkt.circuit_b = text
		theCkt.save()

	def OnClick(self, event):
		currentItem = event.GetIndex()
		print(self.GetItemText(currentItem))

	def OnGetItemText(self, item, column):
		theCkt = models.Circuits.get(models.Circuits.id == item+1)
		if column == 1:
			return theCkt.circuit_a
		elif column == 2:
			return theCkt.circuit_b
		elif column == 3:
			return theCkt.wire_type
		elif column == 4:
			return theCkt.wire_colour
		elif column == 5:
			return theCkt.wire_gauge
		elif column == 0:
			return str(theCkt.id)

		return "X"
		# return ("(" + str(item) + "," + str(column)+")")
	
	def OnGetItemAttr(self, item):
		return None

	def OnGetItemImage(self, item):
		return -1