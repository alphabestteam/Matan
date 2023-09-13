

import socket

class apis:
    def open_account(ip_addr: str, port: int, full_name: str, starting_balance: int):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((ip_addr, port))
        message = f"1"
        my_socket.sendall(bytes(message, "utf-8"))
        my_socket.recv(2028)
        message = f"{full_name} {starting_balance}"
        my_socket.sendall(bytes(message, "utf-8"))
        my_socket.detach()


    def withdraw_deposit(ip_addr: str, port: int, full_name: str, account_number: str, amount: int):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((ip_addr, port))
        message = "2"
        my_socket.sendall(bytes(message, "utf-8"))
        my_socket.recv(2028)
        message = f"{full_name} {account_number} {amount}"
        my_socket.sendall(bytes(message, "utf-8"))
        my_socket.detach()

    
    def send(ip_addr: str, port: int, full_name: str, account_number: str, amount: int, rec_full_name: str, rec_account_number: str):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((ip_addr, port))
        message = "3"
        my_socket.sendall(bytes(message, "utf-8"))
        my_socket.recv(2028)
        message = f"{full_name} {account_number} {amount} {rec_full_name} {rec_account_number}"
        my_socket.sendall(bytes(message, "utf-8"))
        my_socket.detach()


def main():
    # apis.open_account("127.0.0.1", 1111, "test api1", 100)
    apis.withdraw_deposit("127.0.0.1", 1111, "test api1", "72363398", 100)

if __name__ == "__main__":
    main()