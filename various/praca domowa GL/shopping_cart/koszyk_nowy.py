
shop = [
            ['papier_toal', 1.5, 99],
            ['wódka', 20, 99],
            ['kasza', 11, 99], 
            ['sól', 3, 99], 
            ['konserwa', 5, 99],
            ['gwoździe', 12, 99]]

shop1 = {'1': {'papier_toal': 1.5},
             '2': {'wodka': 20},
             '3': {'kasza': 11}, 
             '4': {'sol': 3}, 
             '5': {'konserwa': 5},
             '6': {'gwozdzie': 12}}

cart = []

index = -1
for x, y, z in shop:
    index += 1
    print(index, x, y)

while True:
    try:
        cart.append(shop[int(input('podaj numer produktu: '))])
        for x, y, z in shop:
            print(x, y)
        print(cart)
        end_loop = input(f'{cart} czy chcesz zakończyć? ')
        if end_loop == 'tak':
            break
        else:
            continue

        
    except:
        print('nieprawidłowe dane')
        while False:
            cart.append(shop[int(input('podaj numer produktu: '))])
            end_loop = input(f'{cart} czy chcesz zakończyć?')
            if end_loop == 'tak':
                break


