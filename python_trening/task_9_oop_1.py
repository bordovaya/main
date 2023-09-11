class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
search = Input('Локатор' , 'Текст')
f_1 = Input('Лок1','текст1')
f_2 = Button('Лок2','текст2')
f_3 = Title('Лок3','текст3')
f_4 = Link('Лок4','текст4')
print(search.loc)
print(f_1.loc, f_1.text)
print(f_2.loc, f_2.text)
print(f_3.loc, f_3.text)
print(f_4.loc, f_4.text)


