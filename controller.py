import models
import wx
from new_circuit import NewCircuitWindow

class Controller:
	def __init__(self, app):
		self.new_circuit = NewCircuitWindow(None)

		def AddCircuit(event):
			print(self.new_circuit.getFieldsAsDict())

		self.new_circuit.accept_btn.Bind(wx.EVT_BUTTON, self.AddCircuit)

	def AddCircuit(self, event):
		print(self.new_circuit.getFieldsAsDict())


if __name__ == "__main__":
	app = wx.App(False)
	controller = Controller(app)
	app.MainLoop()