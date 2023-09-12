

import os
import json
import socket
import random
from Costumer_class import Costumer


class Bank:
    def __init__(self, path: str) -> None:
        directory = path
        self.costumers = []

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            if os.path.isfile(filepath):
                with open(filepath, "r") as file:
                    data = file.read()

                costumer_dict = json.loads(data)
                name = costumer_dict["name"]
                account_number = costumer_dict["account_number"]
                total_balance = costumer_dict["total_balance"]
                self.costumers.append(Costumer(name, account_number, total_balance))



    def money_change(self, name: str, account_number: str, amount: int) -> bool:
        """
        function that preforms money change
        input: name of costumer , account number and amount
        return if it came through
        """
        place = -1
        flag = False

        for i in range(0, len(self.costumers)):
            if self.costumers[i].name == name and self.costumers[i].account_number == account_number:
                print("here")
                self.costumers[i].total_balance += amount
                place = i
                flag = True
                break

        if flag:
            with open(f"costumers/costumer{place}.json", "w") as file:
                json.dump(
                    {
                        "name": name,
                        "account_number": account_number,
                        "total_balance": self.costumers[place].total_balance
                    },
                    file
                )
            return True
        else: 
            print("error , costumer not found")
            return False


    def start_listen(self, ip_addr: str, port: int) -> None:
        """ 
        function that starts listening on the socket
        input : ip addr and port
        return: None
        """
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.bind((ip_addr, port))
        my_socket.listen()
        print("Waiting for connection...")
        conn, addr = my_socket.accept()
        print("connected")

        while True:
            conn.sendall(
                bytes("(1) Open a new account \n(2) Deposit/ Withdraw \n(3) Send money".encode("utf-8"))
            )
            selection = str(conn.recv(2028).decode("utf-8"))

            if selection == "1":
                conn.sendall(
                    bytes("Send full name and start balance: example: Matan Gino 123".encode("utf-8"))
                )
                my_data = conn.recv(2028).decode("utf-8")
                data = str(my_data).split(" ")
                name = f"{data[0]} {data[1]}"
                balance = int(data[2])
                account_number = str(random.randint(10000000, 99999999))

                self.costumers.append(Costumer(name, account_number, balance))
                filepath = os.path.join(
                    "costumers", f"costumer{len(self.costumers) - 1}.json"
                )

                with open(filepath, "w") as file:
                    json.dump(
                        {
                            "name": name,
                            "account_number": account_number,
                            "total_balance": balance
                        },
                        file
                    )

            if selection == "2":
                conn.sendall(
                    bytes(
                        "Send full name and account number and amount of money (negetive to withdraw): example: Matan Gino 10000000 -100".encode("utf-8")
                    )
                )
                my_data = conn.recv(2028).decode("utf-8")
                data = str(my_data).split(" ")
                name = f"{data[0]} {data[1]}"
                account_number = data[2]
                amount = int(data[3])
                Bank.money_change(self, name, account_number, amount)

            if selection == "3":
                conn.sendall(
                    bytes(
                        "Send full name and account number and amount of money and full name and account number to receive : example: Matan Gino 10000000 100 blah jsdji 1200000".encode("utf-8")
                    )

                )
                my_data = conn.recv(2028).decode("utf-8")
                data = str(my_data).split(" ")
                name = f"{data[0]} {data[1]}"
                account_number = data[2]
                amount = int(data[3])
                send_name = f"{data[4]} {data[5]}"
                send_account_number = data[6]

                if amount > 0:
                    if Bank.money_change(self, name, account_number, (amount * -1)):
                        Bank.money_change(self, send_name, send_account_number, amount)
                    else: 
                        print("error")


def main():
    ip_addr = "127.0.0.1"
    port = 1111

    test = Bank("costumers/")
    test.start_listen(ip_addr, port)


if __name__ == "__main__":
    main()