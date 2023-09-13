

from product_class import Product
from costumer_class import Costumer
from register_class import Register
import json


def main():
    today_register = Register()
    random_costumer = Costumer("matan", 0)
    random_costumer.add_product(Product("milk", 12, 3))
    random_costumer.remove_products("milk", 2)
    random_costumer.add_product(Product("cariot", 20, 5))
    today_register.checkout_costumer(random_costumer)
    today_register.print_summary()

    formated_costumer = []

    for product in random_costumer.products:
        formated_costumer.append(
            {"name": product.name, "price": product.price, "units": product.quantity}
        )

    # adding items to the item folder
    count = 1
    for dictionary in formated_costumer:
        name = f"item{count}.json"

        with open(f"items/{name}", "w") as file:
            json.dump(dictionary, file)

        count += 1

    # final file for costumer:
    with open("items/final", "w") as file:
        file.write(f"final price: {random_costumer.final_price} \n")
        for index in range(0, len(random_costumer.products)):
            file.write(f"{random_costumer.products[index].name},  amount: {random_costumer.products[index].quantity} \n")


if __name__ == "__main__":
    main()
