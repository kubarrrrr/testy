wybor_gracza1 = input('Gracz1 podaj swoj wybor : ')
wybor_gracza2 = input('Gracz2 podaj swoj wybor : ')

if wybor_gracza1 == 'papier':
    if wybor_gracza2 == 'kamien':
        print('Gracz1 wygral')
    elif wybor_gracza2 == 'nozyczki':
        print('Gracz2 wygral')
    elif wybor_gracza2 == 'papier':
        print('remis')
    else:
        print('zly komunikat')

if wybor_gracza1 == 'kamien':
    if wybor_gracza2 == 'papier':
        print('Gracz2 wygral')
    elif wybor_gracza2 == 'nozyczki':
        print('Gracz1 wygral')
    elif wybor_gracza2 == 'kamien':
        print('remis')
    else:
        print('zly komunikat')

if wybor_gracza1 == 'nozyczki':
    if wybor_gracza2 == 'papier':
        print('Gracz2 wygral')
    elif wybor_gracza2 == 'nozyczki':
        print('remis')
    elif wybor_gracza2 == 'kamien':
        print('Gracz2 wygral')
    else:
        print('zly komunikat')


# if wybor_gracza1 == 'kamien':
#     if wybor_gracza2 == 'nozyczki':
#         print('Gracz1 wygral')

# if wybor_gracza1 == 'nozyczki':
#     if wybor_gracza2 == 'papier':
#         print('Gracz1 wygral')      