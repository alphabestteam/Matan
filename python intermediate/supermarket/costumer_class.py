

from product_class import Product


class Costumer:
    def __init__(
        self, costumer_name: str, final_price: float
    ) -> None:
        self.costumer_name = costumer_name
        self.final_price = final_price
        self.products = []


    def add_product(self, product: Product) -> None:
        """
        this function adds products to the costumer list
        input: product
        returns: None
        """
        for prod in self.products:
            if prod.name == product.name:
                prod.quantity += product.quantity

        else:
            self.products.append(product)

        self.final_price += product.total_price


    def remove_products(self, product_name: str, quantity: int) -> None:
        """
        this function removes product from shopping list
        input: name and quantity
        output: None
        """
        price = 0

        for prod in self.products:
            if prod.name == product_name:
                price = quantity * prod.price
                prod.quantity -= quantity
                if prod.quantity <= 0:
                    self.products.remove(prod)

        else:
            print("product not found!")

        self.final_price -= price