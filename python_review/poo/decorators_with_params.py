import functools

user = {'username': 'jose', 'role': 'admin'}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user['role'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No admin permisions for {user["username"]}'

    return secure_function


@make_secure
def get_password(panel):
    if panel == 'admin':
        return '8789'
    elif panel == 'billing':
        return 'Super password'


print(get_password('billing'))
