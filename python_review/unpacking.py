def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


#
#
# print(multiply(1, 2, 3))

# def add(x, y):
#     return x + y
#
#
# nums = [3, 5]
# print(add(*nums))
#
# nums = {'x': 20, 'y': 50}
# print(add(**nums))

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return 'operador invalido'


print(apply(1, 2, 3, 4, 5, operator='*'))
