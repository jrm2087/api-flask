import functools

user = {'username': 'jose', 'role': 'admin'}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['role'] == access_level:
                return func(*args, **kwargs)
            else:
                return f'No {access_level} permisions for {user["username"]}'

        return secure_function

    return decorator


@make_secure
def get_password(panel):
    if panel == 'admin':
        return '8789'
    elif panel == 'billing':
        return 'Super password'


@make_secure('admin')
def get_admin_password():
    return 'admin: 1234'


@make_secure('guest')
def get_dashboard_password():
    return 'user: user_password'


print(get_admin_password())
print(get_dashboard_password())

user = {'username': 'dario', 'role': 'admin'}

print(get_admin_password())
print(get_dashboard_password())

# print(get_password('billing'))
