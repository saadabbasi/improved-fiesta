import wx
from namedpanel import NamedPanel
from datalist import CircuitList


class NewCircuitWindow(wx.Frame):
	def __init__(self, parent, controller):
		wx.Frame.__init__(self, parent, title = "New Circuit", size=(1200,300))
		self.controller = controller
		panel = wx.Panel(self, wx.ID_ANY, style = wx.RAISED_BORDER)

		self.circuitlist = CircuitList(panel)
		hbox_circuitlist = wx.BoxSizer(wx.HORIZONTAL)
		hbox_circuitlist.Add(self.circuitlist, border = 8)


		vbox1 = wx.BoxSizer(wx.VERTICAL)

		st1 = wx.StaticText(panel, -1, label = "Connector P/N:")
		self.connector_part_num_from = wx.TextCtrl(panel, size = (150,-1))

		st2 = wx.StaticText(panel, -1, label = "Terminal P/N:")
		self.terminal_part_num_from = wx.TextCtrl(panel, size = (150, -1))

		vbox1.Add(st1,flag = wx.LEFT, border = 8)
		vbox1.Add(self.connector_part_num_from,flag = wx.LEFT, border = 8)
		vbox1.Add(st2,flag = wx.LEFT, border = 8)
		vbox1.Add(self.terminal_part_num_from,flag = wx.LEFT, border = 8)

		vbox2 = wx.BoxSizer(wx.VERTICAL)
		st3 = wx.StaticText(panel, -1, label = "Location:")
		self.location_from = wx.TextCtrl(panel)
		self.location_from.Bind(wx.EVT_KILL_FOCUS, lambda event: self.location_lostfocus(event, self.connector_part_num_from, self.location_from),self.location_from)

		st4 = wx.StaticText(panel, -1, label = "Slot:")
		self.slot_from = wx.TextCtrl(panel)

		st_cktA = wx.StaticText(panel, -1, label = "Circuit A")
		self.cktA = wx.TextCtrl(panel)

		vbox2.Add(st3,flag = wx.LEFT, border = 8)
		vbox2.Add(self.location_from,flag = wx.LEFT, border = 8)
		vbox2.Add(st4,flag = wx.LEFT, border = 8)
		vbox2.Add(self.slot_from,flag = wx.LEFT, border = 8)
		vbox2.Add(st_cktA, flag = wx.LEFT, border = 8)
		vbox2.Add(self.cktA, flag = wx.LEFT, border = 8)

		sb = wx.StaticBox(panel, label = 'FROM')
		hbox1 = wx.StaticBoxSizer(sb,wx.HORIZONTAL)
		hbox1.Add(vbox1, flag = wx.LEFT)
		hbox1.Add(vbox2, flag = wx.LEFT)
		

		st5 = wx.StaticText(panel, -1, label = "Type:")
		self.wire_type = wx.Choice(panel, wx.ID_ANY, 
			choices = ['AV', 'AVS', 'AVSS', 'AVX', 'CIVUS', 'CHFUS'])
		st_wire_size = wx.StaticText(panel, -1, label = "Size (mm. sq)")
		self.wire_size = wx.Choice(panel, wx.ID_ANY,
			choices = ['0.13', '0.22', '0.30', '0.50', '0.75', '1.00', '1.25', '2.00', '3.00', '5.00', '8.00', '10.00', '15.00'])
		st_wirecolour = wx.StaticText(panel, -1, label = "Colour")
		self.wire_color = wx.TextCtrl(panel)


		sbwire = wx.StaticBox(panel, label = "Wire Info")
		vbox3 = wx.StaticBoxSizer(sbwire,wx.VERTICAL)
		vbox3.Add(st5, flag = wx.LEFT|wx.RIGHT, border = 10)
		vbox3.Add(self.wire_type, flag = wx.LEFT|wx.RIGHT, border = 10)
		vbox3.Add(st_wire_size, flag = wx.LEFT|wx.RIGHT, border = 10)
		vbox3.Add(self.wire_size, flag = wx.LEFT|wx.RIGHT, border = 10)
		vbox3.Add(st_wirecolour, flag = wx.LEFT|wx.RIGHT, border = 10)
		vbox3.Add(self.wire_color,flag = wx.LEFT|wx.RIGHT, border = 10)

		st6 = wx.StaticText(panel, -1, label = "Connector P/N:")
		self.connector_part_num_to = wx.TextCtrl(panel, size = (150,-1))


		st7 = wx.StaticText(panel, -1, label = "Terminal P/N:")
		self.terminal_part_num_to = wx.TextCtrl(panel, size = (150, -1))

		vbox4 = wx.BoxSizer(wx.VERTICAL)
		vbox4.Add(st6,flag = wx.LEFT, border = 8)
		vbox4.Add(self.connector_part_num_to,flag = wx.LEFT, border = 8)
		vbox4.Add(st7,flag = wx.LEFT, border = 8)
		vbox4.Add(self.terminal_part_num_to,flag = wx.LEFT, border = 8)

		vbox5 = wx.BoxSizer(wx.VERTICAL)
		st8 = wx.StaticText(panel, -1, label = "Location:")
		self.location_to = wx.TextCtrl(panel)
		self.location_to.Bind(wx.EVT_KILL_FOCUS, lambda event: self.location_lostfocus(event, self.connector_part_num_to, self.location_to),self.location_to)

		st9 = wx.StaticText(panel, -1, label = "Slot:")
		self.slot_to = wx.TextCtrl(panel)

		st_cktB = wx.StaticText(panel, -1, label = "Circuit B")
		self.cktB = wx.TextCtrl(panel)

		
		vbox5.Add(st8,flag = wx.LEFT, border = 8)
		vbox5.Add(self.location_to,flag = wx.LEFT, border = 8)
		vbox5.Add(st9,flag = wx.LEFT, border = 8)
		vbox5.Add(self.slot_to,flag = wx.LEFT, border = 8)
		vbox5.Add(st_cktB, flag = wx.LEFT, border = 8)
		vbox5.Add(self.cktB, flag = wx.LEFT, border = 8)


		sb2 = wx.StaticBox(panel, label = "To")
		hbox3 = wx.StaticBoxSizer(sb2,wx.HORIZONTAL)
		hbox3.Add(vbox4, flag = wx.LEFT)
		hbox3.Add(vbox5, flag = wx.LEFT)

		hbox_master = wx.BoxSizer(wx.HORIZONTAL)
		hbox_master.Add(hbox1, flag = wx.LEFT)
		hbox_master.Add(vbox3, flag = wx.LEFT)
		hbox_master.Add(hbox3, flag = wx.LEFT)

		self.accept_btn = wx.Button(panel, wx.ID_ANY, label = "OK")
		self.cancel_btn = wx.Button(panel, wx.ID_ANY, label = "Cancel")

		hbox_button_row = wx.BoxSizer(wx.HORIZONTAL)
		hbox_button_row.Add(self.accept_btn, flag = wx.TOP|wx.BOTTOM, border = 8)
		hbox_button_row.Add(self.cancel_btn, flag = wx.TOP|wx.BOTTOM, border = 8)

		panel_box = wx.BoxSizer(wx.VERTICAL)
		panel_box.Add(hbox_circuitlist)
		panel_box.Add(hbox_master)
		panel_box.Add(hbox_button_row)

		panel.SetSizerAndFit(panel_box)

		panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
		panel_sizer.Add(panel)
		self.SetSizerAndFit(panel_sizer)
		self.Center()
		self.Show(True)


	def location_lostfocus(self, event, connector_field ,location_field):
		location = location_field.GetValue()
		dwg_part_number = self.controller.get_dwg_part_number(location)
		if dwg_part_number:
			connector_field.SetValue(dwg_part_number)
		else:
			connector_field.SetValue("Location Not Found!")
			location_field.SetFocus()

	def getFieldsAsDict(self):

		fields = {'from_terminal':self.terminal_part_num_from.GetValue(),
			'from_location':self.location_from.GetValue(),
			'from_slot':self.slot_from.GetValue(),
			'from_circuit':self.cktA.GetValue(),
			'to_terminal':self.terminal_part_num_to.GetValue(),
			'to_location':self.location_to.GetValue(),
			'to_slot':self.slot_to.GetValue(),
			'to_circuit':self.cktB.GetValue(),
			'wire_gauge':self.wire_size.GetString(self.wire_size.GetCurrentSelection()),
			'wire_type':self.wire_type.GetString(self.wire_type.GetCurrentSelection()),
			'wire_color':self.wire_color.GetValue(),
			}

		return fields
