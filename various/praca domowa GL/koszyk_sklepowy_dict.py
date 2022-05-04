
pulka_sklepowa = {'1': {'papier_toal': 1.5},
             '2': {'wodka': 20},
             '3': {'kasza': 11}, 
             '4': {'sol': 3}, 
             '5': {'konserwa': 5},
             '6': {'gwozdzie': 12}}
print(' \n W naszym sklepie znajdziesz tylko najpotrzebniejsze produkty :-)\n ')

for key, value in pulka_sklepowa.items():
    print(key, value)

koszyk = {}

while True:
    koszyk.update(pulka_sklepowa[input('Podaj numer produktu: ')])
    koniec = input('czy to wszystko? ')
    if koniec == 'tak':
        break

def naleznosc():
    kasa = koszyk.values()
    suma = sum(kasa)
    return(suma)

print(koszyk)
print(f'do zaplaty {naleznosc()}')

