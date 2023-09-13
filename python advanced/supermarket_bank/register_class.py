

from costumer_class import Costumer
from bank.api import apis
import param


class Register:
    def __init__(self, name: str, bank_number="0") -> None:
        self.profit = 0.0
        self.total_list = []
        self.bank_number = bank_number
        self.name = name

        if bank_number == "0":
            apis.open_account(param.IP_ADDR, param.PORT, name, self.profit)


    def checkout_costumer(self, costumer: Costumer) -> None:
        """
        this function checkouts a costumer
        input: costumer
        returns: None
        """
        self.profit += costumer.final_price
        self.total_list.append([costumer.costumer_name, costumer.final_price])
        apis.send(param.IP_ADDR, param.PORT, costumer.costumer_name, costumer.bank_number, costumer.final_price, self.name, self.bank_number)


    def print_summary(self) -> None:
        """
        this function prints shopping list
        input: None
        return: None
        """
        print(f"total profit today: {self.profit}. \n {self.total_list}")