# def add(x, y):
#     return x + y
#
#
# # add(8, 9)
# result = add(8, 9)
# print(result)

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return 'the number cannot be zero.'


result = divide(5, 8)
print(result)

result = divide(5, 0)
print(result)
