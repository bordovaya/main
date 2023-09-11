class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        return "Автомобиль заведен"
    def stop(self):
        return "Автомобиль заглушен"
    def get_year(self, year_new):
        self.year = year_new
    def get_type(self, type_new):
        self.type = type_new
    def get_color(self, color_new):
        self.color = color_new

