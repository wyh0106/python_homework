# Copyright © 2020 Room_3033
# All rights reserved.

# created by 魏懿航、代小力、陈建君、杨宸杰 at 05/25/2020

class Phone:
	def __init__(self, Label, Model, ReleaseDate, Length, Width, Thickness, Weight):
		self.Label = Label
		self.Model = Model
		self.Date = ReleaseDate
		self.Length = Length
		self.Width = Width
		self.Thickness = Thickness
		self.Weight = Weight

	def PhoneInfo(self):
		print("The phone's information:\n" + "Label:" + self.Label)
		print("Model:" + self.Model)
		print("Date:" + self.Date)
		print("Length:" + str(self.Length)+'mm')
		print("Width:" + str(self.Width)+'mm')
		print("Weight:" + str(self.Weight)+'g')
		print("Thickness:" + str(self.Thickness) + 'mm' + '\n')

phone1 = Phone(Label = 'xiaomi', Model = 'Mix3', ReleaseDate = '2018/10/25', Length = 157.89, Width = 74.69, Thickness = 8.46, Weight = 218)
phone2 = Phone(Label = 'HuaWei', Model = 'Play4TPro', ReleaseDate = '2020/04/09', Length = 157.4, Width = 73.2, Thickness = 7.75, Weight = 165)
phone3 = Phone(Label = 'Redmi', Model = 'k30 极速版', ReleaseDate = '2020/05/14', Length = 165.3, Width = 76.6, Thickness = 8.79, Weight = 208)
phone4 = Phone(Label = '8848', Model = 'M6 尊享版', ReleaseDate = '2020/03/03', Length = 177, Width = 77, Thickness = 13, Weight = 252)
phone5 = Phone(Label = 'OnePlus（1+）', Model = '8 pro', ReleaseDate = '2020/04/17', Length = 165.3, Width = 74.3, Thickness = 8.5, Weight = 199)
phone6 = Phone(Label = 'xiaomi', Model = 'mi 10', ReleaseDate = '2020/02/X', Length = 162.6, Width = 74.8, Thickness = 8.96, Weight = 208)
phone7 = Phone(Label = 'Apple ', Model = 'iPhone Xs', ReleaseDate = '2018/09/01', Length = 143.6, Width = 70.9, Thickness = 7.7, Weight = 177)
phone8 = Phone(Label = 'SAMSUNG', Model = 'Galaxy Fold', ReleaseDate = '2019/11/1', Length = 160.9, Width = 117.9, Thickness = 15.7, Weight = 276)

phone1.PhoneInfo()
phone2.PhoneInfo()
phone3.PhoneInfo()
phone4.PhoneInfo()
phone5.PhoneInfo()
phone6.PhoneInfo()
phone7.PhoneInfo()
phone8.PhoneInfo()

