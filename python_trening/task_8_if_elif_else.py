num_float = 3.4

if num_float >0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
     print('Число отрицательное')

а = 5
permint_print = True
if а > 0 and permint_print:
    print('а - положительное число')
elif not permint_print:
    print('Печать запрещена')


b = 10
if  1 <= b <= 4:
    print('Бакалавр')
elif 5 <= b <= 6:
    print('Магистр')
elif 7 <= b <= 9:
    print('Аспирант')
else:
    print('Введите корректный год обучения')

x = 100
if x > 100 or x < -100:
    print('-')
else:
    print('+')
