# numbers = [87, 29, 89]
# doubled = [x * 2 for x in numbers]
#
# print(numbers)
# print(doubled)


friends = ['jose', 'farouk', 'carolina', 'annie', 'lucy', 'javier']
start_j = [f for f in friends if f.startswith('j')]

print(friends)
print(start_j)
print(friends is start_j)
print('friends ', id(friends), 'start_j:', id(start_j))
