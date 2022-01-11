# def add(x, y):
#     return x + y
#
#
# print(add(5, 9))

# (lambda x, y: x + y)(5, 9)

def double(x):
    return x * 2


sequence = [1, 2, 3, 4, 5]
# doubled = [double(x) for x in sequence]
# doubled = map(double, sequence)
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
