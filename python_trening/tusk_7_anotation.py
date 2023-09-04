a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return "" * (max(0, width - len(s))) + s

print(indent('123', 123))


def dlina(s: str ='')-> int:
    return len(s)
print(dlina())

def funct(a: list, b: list) ->int:
    return max(len(a), len(b))

def listt(a: list):
    a.append(5)
    return a
print(listt([1, 2, 3, 4]))

def list_sum(a: list):
    return sum(a)
print(list_sum([1, 2, 3, 4]))