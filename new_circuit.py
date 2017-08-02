import wx

class NewCircuitWindow(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title = "New Circuit", size=(1200,300))
		panel = wx.Panel(self, wx.ID_ANY)

		vbox1 = wx.BoxSizer(wx.VERTICAL)
		st1 = wx.StaticText(panel, -1, label = "Connector P/N:")
		self.connector_part_num_from = wx.TextCtrl(panel)

		st2 = wx.StaticText(panel, -1, label = "Terminal P/N:")
		self.terminal_part_num_from = wx.TextCtrl(panel)

		vbox1.Add(st1,flag = wx.LEFT, border = 8)
		vbox1.Add(self.connector_part_num_from,flag = wx.LEFT, border = 8)
		vbox1.Add(st2,flag = wx.LEFT, border = 8)
		vbox1.Add(self.terminal_part_num_from,flag = wx.LEFT, border = 8)

		vbox2 = wx.BoxSizer(wx.VERTICAL)
		st3 = wx.StaticText(panel, -1, label = "Location:")
		self.location_from = wx.TextCtrl(panel)

		st4 = wx.StaticText(panel, -1, label = "Slot:")
		self.slot_from = wx.TextCtrl(panel)

		vbox2.Add(st3,flag = wx.LEFT, border = 8)
		vbox2.Add(self.location_from,flag = wx.LEFT, border = 8)
		vbox2.Add(st4,flag = wx.LEFT, border = 8)
		vbox2.Add(self.slot_from,flag = wx.LEFT, border = 8)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(vbox1, flag = wx.LEFT)
		hbox1.Add(vbox2, flag = wx.LEFT)

		st5 = wx.StaticText(panel, -1, label = "Type:")
		self.wire_type = wx.Choice(panel, wx.ID_ANY, 
			choices = ['AV', 'AVS', 'AVSS', 'AVX', 'CIVUS', 'CHFUS'])

		vbox3 = wx.BoxSizer(wx.VERTICAL)
		vbox3.Add(st5, flag = wx.LEFT)
		vbox3.Add(self.wire_type, flag = wx.LEFT)

		st6 = wx.StaticText(panel, -1, label = "Connector P/N:")
		self.connector_part_num_to = wx.TextCtrl(panel)

		st7 = wx.StaticText(panel, -1, label = "Terminal P/N:")
		self.terminal_part_num_to = wx.TextCtrl(panel)

		vbox4 = wx.BoxSizer(wx.VERTICAL)
		vbox4.Add(st6,flag = wx.LEFT, border = 8)
		vbox4.Add(self.connector_part_num_to,flag = wx.LEFT, border = 8)
		vbox4.Add(st7,flag = wx.LEFT, border = 8)
		vbox4.Add(self.terminal_part_num_to,flag = wx.LEFT, border = 8)

		vbox5 = wx.BoxSizer(wx.VERTICAL)
		st8 = wx.StaticText(panel, -1, label = "Location:")
		self.location_to = wx.TextCtrl(panel)

		st9 = wx.StaticText(panel, -1, label = "Slot:")
		self.slot_to = wx.TextCtrl(panel)

		self.accept_btn = wx.Button(panel, wx.ID_ANY, label = "OK")
		vbox5.Add(st8,flag = wx.LEFT, border = 8)
		vbox5.Add(self.location_to,flag = wx.LEFT, border = 8)
		vbox5.Add(st9,flag = wx.LEFT, border = 8)
		vbox5.Add(self.slot_to,flag = wx.LEFT, border = 8)
		vbox5.Add(self.accept_btn)

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(vbox4, flag = wx.LEFT, border = 40)
		hbox3.Add(vbox5, flag = wx.LEFT)

		hbox_master = wx.BoxSizer(wx.HORIZONTAL)
		hbox_master.Add(hbox1, flag = wx.LEFT)
		hbox_master.Add(vbox3, flag = wx.LEFT, border = 40)
		hbox_master.Add(hbox3, flag = wx.LEFT)

		panel.SetSizer(hbox_master)

		self.Show(True)

	def getFieldsAsDict(self):
		from_values = {'from_connector':self.connector_part_num_from.GetValue(),
			'from_terminal':self.terminal_part_num_from.GetValue(),
			'from_location':self.location_from.GetValue(),
			'from_slot':self.slot_from.GetValue()
			}

		to_values = {'to_connector':self.connector_part_num_to.GetValue(),
			'to_terminal':self.terminal_part_num_to.GetValue(),
			'to_location':self.location_to.GetValue(),
			'to_slot':self.slot_to.GetValue()
			}

		return (from_values,to_values)
