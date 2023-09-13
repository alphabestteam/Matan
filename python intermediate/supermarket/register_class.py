

from costumer_class import Costumer


class Register:
    def __init__(self) -> None:
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