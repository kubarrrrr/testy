def czy_to_kobieta(imie):
    if imie == 'Kuba':
        return False
    elif imie[-1] == 'a':
        return True
    else:
        return False


wynik = czy_to_kobieta(imie='Magda')
print(wynik)
wynik = czy_to_kobieta(imie='Kuba')
print(wynik)
wynik = czy_to_kobieta(imie='Jaś')
print(wynik)

# czy_to_kobieta(imie='Roza')

# czy_to_kobieta(imie='Turek')
# czy_to_kobieta(imie='Kuba')