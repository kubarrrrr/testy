wybor_gracza1 = input('Gracz1 podaj swoj wybor : ')
wybor_gracza2 = input('Gracz2 podaj swoj wybor : ')

if wybor_gracza1 == 'papier' and wybor_gracza2 =='kamien':
    print('Gracz1 wygral')
elif wybor_gracza1 == 'nozyczki' and wybor_gracza2 == 'papier':
        print('Gracz1 wygral')
elif wybor_gracza1 == 'kamien' and wybor_gracza2 == 'nozyczki':
    print('Gracz1 wygral')

# elif wybor_gracza2 == 'papier' and wybor_gracza1 =='kamien':
#     print('Gracz2 wygral')
# elif wybor_gracza2 == 'nozyczki' and wybor_gracza1 == 'papier':
#         print('Gracz2 wygral')
# elif wybor_gracza2 == 'kamien' and wybor_gracza1 == 'nozyczki':
#     print('Gracz2 wygral')
elif wybor_gracza2 == wybor_gracza1:
    print('remis')
else:
    print('gracz2 wygral')