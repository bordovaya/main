class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def perimeter(self):
        return 2 * (self.x + self.y)
    def area(self):
        return self.x * self.y
R_1 = Rectangle(1, 2)
print(R_1.perimeter())
print(R_1.area())
R_2 = Rectangle(2, 3)
print(R_2.perimeter())
print(R_2.area())
R_3 = Rectangle(3, 4)
print(R_3.perimeter())
print(R_3.area())

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b
f = Math(1, 2)
print(f.addition())
print(f.multiplication())
print(f.division())
print(f.subtraction())



class Button:
    type: str = 'Кнопка'
    loc: str = ''
    def __init__(self, text):
        self.text = text
    def click(self):
        return "Клик по кнопке - {}".format(self.text)
Text_Box = Button('Text Box')
print(Text_Box.text)
print(Text_Box.click())

Check_Box = Button('Check Box')
print(Check_Box.text)
print(Check_Box.click())

Radio_Button = Button('Radio Button')
print(Radio_Button.text)
print(Radio_Button.click())

Web_Tales = Button('Web Tales')
print(Web_Tales.text)
print(Web_Tales.click())

Buttons = Button('Buttons')
print(Buttons.text)
print(Buttons.click())

Links = Button('Links')
print(Links.text)
print(Links.click())

Broken_Links = Button('Broken Links')
print(Broken_Links.text)
print(Broken_Links.click())

Upload_and_Download = Button('Upload and Download')
print(Upload_and_Download.text)
print(Upload_and_Download.click())

Dynamic_Properties = Button('Dynamic Properties')
print(Dynamic_Properties.text)
print(Dynamic_Properties.click())