#!/usr/bin/env python3
import wx
from new_circuit import NewCircuitWindow
from connector_list import ConnectorWindow
import models


def get_connector(location):
    try:
        return models.Connectors.get(location=location)
    except models.Connectors.DoesNotExist:
        return None

class Controller:
    def __init__(self):
        self.new_circuit = NewCircuitWindow(None, self)
        self.connector_window = ConnectorWindow(None, self)
        self.new_circuit.accept_btn.Bind(wx.EVT_BUTTON, self.AddCircuit)

    def get_dwg_part_number(self, location):
        conn = get_connector(location)
        if conn:
            return conn.dwg_part_number
        return None

    def AddCircuit(self, event):
        fields = self.new_circuit.getFieldsAsDict()
        try:
            models.addCircuit(fields)
        except models.Connectors.DoesNotExist:
            print("Connector not found")

if __name__ == "__main__":
    app = wx.App(False)
    controller = Controller()
    app.MainLoop()
