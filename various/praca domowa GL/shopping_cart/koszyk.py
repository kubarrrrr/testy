def add_product_to_cart(id: int, qty: int):
    """
    add product to the storage
    :param id:
    :param qty:
    """
    tmp = items[int(id)]
    tmp.cart += 1
    tmp.qty = int(qty)
    tmp.stock -= tmp.qty

pulka_sklepowa = {'1': {'papier_toal': 1.5},
             '2': {'wodka': 20},
             '3': {'kasza': 11}, 
             '4': {'sol': 3}, 
             '5': {'konserwa': 5},
             '6': {'gwozdzie': 12}}


class Zakupy():
    cart = []
    def product(self, id: int, quantity: int, price ):
        self.id = id
        self.quantity = quantity
        self.ptice = price

    def add_product(sefl):
        

    def rem_product(self,):
