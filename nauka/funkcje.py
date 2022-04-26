def czy_to_kobieta(imie):
    if imie == 'Kuba':
        return False
    elif imie[-1] == 'a':
        return True
    else:
        return False


wynik = czy_to_kobieta(input('podaj swoje '))
if wynik == True:
    print('to kobieta')
