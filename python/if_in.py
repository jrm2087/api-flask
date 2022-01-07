movies_watched = {'Matrix', 'Her', 'Green Book'}
user_movie = input('Ingrese pelicula: ')

if user_movie in movies_watched:
    print(f'Yo vi {user_movie} también.')
else:
    print('No he visto la pelicula')
