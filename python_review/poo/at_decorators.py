import functools

user = {'username': 'jose', 'role': 'admin'}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user['role'] == 'admin':
            return func()
        else:
            return f'No admin permisions for {user["username"]}'

    return secure_function


@make_secure
def get_admin_password():
    return '8789'


# get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
print(get_admin_password.__name__)
