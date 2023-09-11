class Button:
    type: str = 'Кнопка' #атрибут класса - это константа для этого класса
    def __init__(self, text, link):
        self.text = text
        self.link = link


#создаем экземпляры класса
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

#Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
print(home.type)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)
print(catalog_msk.type)

class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc
    def click(self): # метод
        return "Клик по локатору - {}".format(self.loc)

# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

# Вызываем метод
print(home_two.click())

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
