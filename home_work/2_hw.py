def task_1(a: int, b: float, c: str, d: list, e: bool)->str:
    return a, type(a), b, type(b), c, type(c), d, type(d), e, type(e)
print(task_1( 1,   0.1, 'ok', [1, 2], True))

def task_2(a = [1, 2, 3, 5, 8, 13, 21])->list:
    return a[0:3]
print(task_2())
#Фибоначчи

def task_3(a:int) -> int:
    return a**2
print(task_3(3))
