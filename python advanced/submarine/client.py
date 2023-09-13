import socket
from param import IP, PORT


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))

    while True:
        data = my_socket.recv(2028).decode("utf-8")
        print(str(data))

        if data:
            message = input("enter message: ")
            my_socket.sendall(bytes(message, "utf-8"))


if __name__ == "__main__":
    main()