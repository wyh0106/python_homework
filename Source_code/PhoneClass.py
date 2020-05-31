class Phone:

	def __init__(self, Label, Model, ScreenSize, RAM, BatteryCapacity, CPUCore, Thickness):
		self.Label = Label
		self.Model = Model
		self.ScreenSize = ScreenSize + 'inch'
		self.RAM = RAM + 'GB'
		self.BatteryCapacity = BatteryCapacity + "mA/h"
		self.CPUCore = CPUCore
		self.Thickness = Thickness + 'mm'

