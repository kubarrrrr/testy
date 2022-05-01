
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

while True:
    koszyk.append(pulka_sklepowa[int(input('podaj nr '))])
    koniec = input('chcesz zakonczyc zakupy? ')
    if koniec == 'tak':
        break

ceny = []
for x, y in koszyk:
    ceny.append(y)

produkty = []
for x, y in koszyk:
    produkty.append(x)

    
suma = sum(ceny)
print(f'w Twoim koszyku znajdują się następujące produkty: {produkty}')
print(f'do zaplaty {suma}')
    