# number = 7
# user_input = input('Quieres jugar? (y/n): ').lower()

# while True:  # user_input != 'n':
#
#     user_input = input('Quieres jugar? (y/n): ').lower()
#
#     if user_input == 'n':
#         break
#
#     user_number = int(input('Ingrese número: '))
#     if user_number == number:
#         print('Tu número es correcto')
#     elif abs(number - user_number) in (1, -1):
#         print('Error. Numero incorrecto')
#     else:
#         print('Error. Lo sentimos')

# friends = ['jose', 'dario', 'lucy']
#
# for friend in range(4):  # friends:
#     print(f'{friend} es mi amigo.')


grades = [87, 89, 94, 61, 99]
total = sum(grades)  # 0
amount = len(grades)

# for grade in grades:
#     total += grade

print('AVG:', total / amount)
