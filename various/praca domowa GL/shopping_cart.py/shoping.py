# inside: products, price, stock
shop = {'potatos': [5, 99], 'oranges': [15, 99]}

# shows enumerated, avaliable products
index = 0
for key, value in shop.items():
    index += 1
    print(index, key)

basket = []
total = []

# add product name to basket or quits
def add_to_basket():
    action = input('what would you like to buy? ')
    while action != 'quit':
        if action in shop:
            basket.append(action)
            action = input('Splendid! The product has been added to your basket. Maybe something else? type [quit] for ending the application ')
        else:
            action = input('We are terribly sorry, but the product you are tryingto add is currently unavaliable. Please try to add something else, or type [quit] for summary of your purchuase ')

add_to_basket()

print(f'These are your purchased goods', basket)

action = input('woud you like to add something else? [yes] or [no] or [remove]')


def remove_from_basket():
    if action == 'remove':
        basket.remove(input('which product would you like to remove? '))


# takes price values fromthe list
def final_price():
    if action == 'yes':
        add_to_basket()
        print("that's alle the goods you purchuased: ", basket)
        
        for items in basket:
            total.append(shop[items][0])


    else:
        for items in basket:
            total.append(shop[items][0])

# updates quantity of of product in in stock
def in_stock():
    for item in basket:
        shop[item][1] -= 1
    return shop
    

remove_from_basket()
final_price()
amount_to_pay = sum(total)
print(in_stock())

# tax for the goods added to the price
def tax_to_pay(x, tax):
    price_with_tax = x * tax
    return(price_with_tax)

price = tax_to_pay(amount_to_pay, 1.08)
print('in your basket: ', basket)
print('Amount of money to pay: ', price)