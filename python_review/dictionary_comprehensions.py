users = [
    (0, 'joser', 'pass'),
    (1, 'jdrleal', '1234'),
    (2, 'dario', '5678'),
    (3, 'jdrodriguez', '91011'),
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input('username: ')
password_input = input('password: ')

_, username, password = username_mapping[username_input]

if password_input == password:
    print('correct')
else:
    print('error')
