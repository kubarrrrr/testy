pulka_sklepowa = [['papier_toal', 1.5],
             ['wodka', 20],
             ['kasza', 11], 
             ['sol', 3], 
             ['konserwa', 5],
             ['gwozdzie', 12]]

index = -1
for x, y in pulka_sklepowa:
    y = str(y) + 'zł'
    index += 1
    print(index, x, y)

koszyk = []

# while True:    
#     akcja = input('wybierz numer produktu lub zakończ: ')
#     akcja1 = int(akcja)
#     if akcja1 == 1:
#         koszyk.append(pulka_sklepowa(akcja))
#     elif akcja == 'zakończ':
#         break
#     print(koszyk)

while True:
    # koszyk.append(pulka_sklepowa[int(input('podaj nr '))])
    # print(koszyk)
    # akcja = input(f'Wrzuciles do koszyka nastepujace produkty: {koszyk}. Chcesz zakonczyc zakupy? ')
    # if akcja == 'tak':
    #     break
    # elif akcja == int():
    #     koszyk.append(pulka_sklepowa[2])
    # print(koszyk)

koszyk.append(pulka_sklepowa[int(input('podaj nr '))])
    print(koszyk)
    koniec = input(f'Wrzuciles do koszyka nastepujace produkty: {koszyk}. Chcesz zakonczyc zakupy? ')
    if koniec == 'tak':
        break
    elif koniec == int:
        koszyk.append(pulka_sklepowa[int(input('podaj nr '))])



ceny = []
for x, y in koszyk:
    ceny.append(y)

produkty = []
for x, y in koszyk:
    produkty.append(x)

    
suma = sum(ceny)
print(f'\n \n W Twoim koszyku znajdują się następujące produkty: {produkty}')
print(f'do zaplaty {suma}')
    


