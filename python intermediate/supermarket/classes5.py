class Product:
    def __init__(self, name: str, price: float, quantity: int) -> object:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price = price * quantity


class Costumer:
    def __init__(
        self, costumer_name: str, shopping_list: list, final_price: float
    ) -> object:
        self.costumer_name = costumer_name
        self.shopping_list = shopping_list
        self.final_price = final_price
        self.products = []

    def add_product(self, product: Product) -> None:
        """
        this function adds products to the costumer list
        input: product
        returns: None
        """
        if product.name in self.shopping_list:
            self.shopping_list[
                self.shopping_list.index(product.name) + 1
            ] += product.quantity

            for prod in self.products:
                if prod.name == product.name:
                    prod.quantity += product.quantity
        else:
            self.shopping_list.append(product.name)
            self.shopping_list.append(product.quantity)
            self.products.append(product)

        self.final_price += product.total_price

    def remove_products(self, product_name: str, quantity: int) -> None:
        """
        this function removes product from shopping list
        input: name and quantity
        output: None
        """
        if product_name in self.shopping_list:
            index = self.shopping_list.index(product_name)
            self.shopping_list[index + 1] -= quantity

            for prod in self.products:
                if prod.name == product_name:
                    price = quantity * prod.price
                    prod.quantity -= quantity

                    if prod.quantity <= 0:
                        self.products.remove(prod)

            self.final_price -= price

            if self.shopping_list[index + 1] <= 0:
                del self.shopping_list[index + 1]
                del self.shopping_list[index]
        else:
            print("product not found!")


class Register:
    def __init__(self) -> object:
        self.profit = 0.0
        self.total_list = []

    def checkout_costumer(self, costumer: Costumer) -> None:
        """
        this function checkouts a costumer
        input: costumer
        returns: None
        """
        self.profit += costumer.final_price
        self.total_list.append([costumer.costumer_name, costumer.final_price])

    def print_summary(self) -> None:
        """
        this function prints shopping list
        input: None
        return: None
        """
        print(f"total profit today: {self.profit}. \n {self.total_list}")
