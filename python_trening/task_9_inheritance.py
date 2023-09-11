class Mammal:
    className = 'Млекопитающее'

class Dog(Mammal):
    species = 'Canis lupus'

dog = Dog()#создание объекта по дочернему классу
print(dog.className) #Млекопитающее