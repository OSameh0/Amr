def add(ls):
    x = 0
    for number in ls:
        x += number
    return x


def sub(ls):
    x = 0
    for number in ls:
        x -= number
    return x


def multi(ls):
    x = 0
    for number in ls:
        x *= number
    return x


def div(ls):
    x = 1
    for number in ls[0:-2]:
        x /= number
    x = x/number[-1]
    return x
