# friends = ['jose', 'dario']
# print('jose' in friends)

# movies_watched = {'Matrix', 'Her', 'Green Book'}
# user_movie = input('Ingrese pelicula: ')
# print(user_movie in movies_watched)

number = 7
user_input = input('Ingresa "y" si quieres jugar: ').lower()

if user_input == 'y':
    user_number = int(input('Ingrese número: '))
    if user_number == number:
        print('TU número es correcto')
    elif abs(number - user_number) in (1, -1):
        print('Error. Numero incorrecto')
    else:
        print('Error. Lo sentimos')
