def get_admin_password():
    return '8789'


def make_function(func):
    def secure_function():
        if user['role'] == 'admin':
            return func()
        else:
            return f'No admin permisions for {user["username"]}'

    return secure_function


get_admin_password = make_function(get_admin_password)
user = {'username': 'jose', 'role': 'admin'}
print(get_admin_password())

# def secure_get_admin():
#     if user['role'] == 'admin':
#         return '8789'


# print(secure_get_admin())
# print(get_admin_password())
