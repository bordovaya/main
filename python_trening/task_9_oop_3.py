class Soda:
    def __init__(self, ing=None):
        self.ing = ing
    def show_my_drink(self):
        if self.ing:
            print('Газировка и {self.ing}')
        else:
            print('Обычная газировка')

drink1= Soda()
drink2= Soda('малина')
drink1.show_my_drink()
drink2.show_my_drink()