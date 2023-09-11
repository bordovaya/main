class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        return "Автомобиль заведен"
    def stop(self):
        return "Автомобиль заглушен"
    def get_year(self):
        print(self.year)
    def get_type(self):
        print(self.type)
    def get_color(self):
        print(self.color)
A_1 = Car('red', 'bus', '2020')
A_1.get_year()
A_1.get_type()
A_1.get_color()
print(A_1.start())
print(A_1.stop())
