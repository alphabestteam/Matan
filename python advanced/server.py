

import socket


HOST = "127.0.0.1"
PORT = 1111


def main():

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((HOST, PORT))
    my_socket.listen()
    print("Waiting for connection...")
    conn, addr = my_socket.accept()
    print("connected")

    while True:
        data = conn.recv(2028)

        if data:
            print(f"new message: {str(data)}")
            conn.sendall(bytes((str(data).upper()).encode()))


if __name__ == "__main__":
    main()