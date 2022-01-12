def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg} : {value}')


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, name='jose', age=25)

# print_nicely(name='jose', age=34)

#
#
# named(name='jose', age=34)

# def named(name, age):
#     print(name, age)


# details = {'name': 'jose', 'age': 34}
# named(**details)
