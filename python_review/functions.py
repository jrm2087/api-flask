# def hello():
#     print('hello!')
#
# hello()

# def user_age_in_seconds():
#     user_age = int(input('Enter your age: '))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f'Your age in seconds is {age_seconds}.')
#
#
# print('Welcome')
# user_age_in_seconds()
# print('Goodbye')

friends = ['jose', 'dario', 'annie', 'carolina']


def add_friend():
    friend_name = input('Enter your friend name: ')
    friends.append(friend_name)
    # f = friends + [friend_name]
    # friends = friends + [friend_name] # only scope


add_friend()
print(friends)
