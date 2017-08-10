#!/usr/bin/env python3
import wx
from datalist import ConnectorList

class ConnectorWindow(wx.Frame):
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=bad-whitespace
    def __init__(self, parent, controller):
        flds = [('Loc:','location'), ('Drawing P/N','dwg_num'), ('Identified P/N','iden_num'), ('Color','color')]
        wx.Frame.__init__(self, parent, title = "Connector List")
        self.panel = wx.Panel(self, wx.ID_ANY, style = wx.RAISED_BORDER)

        self.connector_list = ConnectorList(self.panel)

        self.make_fields(flds)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.connector_list)
        self.vbox.Add(self.fld_hbox)
        self.panel.SetSizerAndFit(self.vbox)

        self.Show(True)
        
    def make_fields(self, flds):
        self.flds = {}
        sb = {}
        self.fld_hbox = wx.BoxSizer(wx.HORIZONTAL)
        for fld in flds:
            self.flds[fld[1]] = wx.TextCtrl(self.panel)
            sb[fld[1]] = wx.StaticText(self.panel, -1, label = fld[0])
            fld_vbox = wx.BoxSizer(wx.VERTICAL)
            fld_vbox.Add(sb[fld[1]])
            fld_vbox.Add(self.flds[fld[1]])
            self.fld_hbox.Add(fld_vbox)
