x = 1
y = 2
if x > y:
    print(x)
else:
    print(y)


a = 0
b = 135
if abs(a - b) == 135:
    print('Yes')
else:
    print('No')


c = 9
if c in (1, 2) or c == 12:
    print('Зима')
elif c in (3, 4, 5):
    print('Весна')
elif c in (6, 7, 8):
    print('Лето')
elif c in (9, 10, 11):
    print('Осень')


d = 11
e = 20
f = 30
if d>10 and e>10 and f >10:
    print('Yes')
else:
    print('No')

#f_1 = [-1, 3, 4, 5, 6]
#result = 0
#for elem in f_1[0]<0:
#    result = result + 1
#return result
#    print(f_1[-1, 3, 4, 5, 6])

def dn(l,m):
    return (l*29*12)+(m*29)
print(dn(2,2))




