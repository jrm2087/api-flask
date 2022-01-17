import logging


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')

    return dividend / divisor


students = [
    {'name': 'jose', 'grades': [87, 88]},
    {'name': 'dario', 'grades': []},
    {'name': 'annie', 'grades': [89, 90]},
]

print('*** average grades program ***')
try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f'{name} avg: {average}')
except ZeroDivisionError as e:
    logging.error(e)
    print(f'Error: {name} has no grades.')
else:
    print(f'-- All student averages calculated.')
finally:
    print('-- End of students average calcularion')
