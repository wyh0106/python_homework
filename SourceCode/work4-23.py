

class Car():
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.dis = 10

    def return_info(self):
        info = str(self.year) + ' ' + self.brand + ' ' + self.color
        return info.title()

    def read_num(self):
        print("the car already runed has " + str(self.dis) + ' KM')

    def increase_dis(self, km):
        if km>=self.dis:
            self.dis = km
        else:
            print("Data Error!")

    def plus_dis(self, num):
        if num >= 0:
            self.dis += num
        else:
            print("Data Error!")

# my_car = Car('hongqi', 'black', 1968)
# print(my_car.return_info())

# my_car.increase_dis(500)
# my_car.increase_dis(600)

# my_car.plus_dis(-30)
# my_car.plus_dis(100)

# my_car.read_num()
class Battery():
    def __init__(self,battery_vol = 70):
        self.battery_vol = battery_vol

    def describe_battery(self):
        print(str(self.battery_vol) + '%')

class Ele_car(Car):
    def __init__(self, brand, color, year):
        super().__init__(brand, color, year)
        self.battery = Battery()
    


my_tesla = Ele_car('tesla', 'model', 2019)
print(my_tesla.return_info())
my_tesla.battery.describe_battery()