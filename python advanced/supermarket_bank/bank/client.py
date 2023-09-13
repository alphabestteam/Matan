

import socket


HOST = "127.0.0.1"
PORT = 1111


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((HOST, PORT))

    while True:
        data = my_socket.recv(2028).decode("utf-8")
        print("Received: " + str(data))
        message = input("enter message: ")
        my_socket.sendall(bytes(message, "utf-8"))
        data = my_socket.recv(2028).decode("utf-8")
        print("Received: " + str(data))
        message = input("enter message: ")
        my_socket.sendall(bytes(message, "utf-8"))


if __name__ == "__main__":
    main()