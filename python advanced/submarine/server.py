

import socket
from playing_board_class import Playing_board
from point_class import Point
from ship_class import Ship
from param import IP, PORT


class Server:
    def __init__(self, ip_addr: str, port: int) -> None:
        self.ip_addr = ip_addr
        self.port = port


    def ship_adder(self, playing_board: Playing_board, conn: socket.socket, size: int) -> None:
        """
        function that adds ships to playing board through connection
        needs socket, playing board connection and size
        returns None
        """
        conn.sendall(bytes(f"Enter a size {size} ship: : start_x start_y end_x end_y)".encode("utf-8")))
        points = str(conn.recv(2028).decode("utf-8")).split(" ")
        if playing_board.is_space(Point(int(points[0]), int(points[1])), Point(int(points[2]), int(points[3]))):
            playing_board.insert_ship(Ship(Point(int(points[0]), int(points[1])), Point(int(points[2]), int(points[3])), size))
        else:
            self.ship_adder(playing_board, conn, size)
        
    
    def start_game(self):
        """
        game logic server start
        """
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.bind((self.ip_addr, self.port))
        my_socket.listen()
        print("Waiting for player1...")

        conn1, addr1 = my_socket.accept()
        print("player 1 connected!")
        player_1 = Playing_board()

        print("Waiting for player2...")
        conn2, addr2 = my_socket.accept()
        print("player 2 connected!")
        player_2 = Playing_board()

        self.ship_adder(player_1, conn1, 2)
        self.ship_adder(player_1, conn1, 3)
        self.ship_adder(player_1, conn1, 3)
        self.ship_adder(player_1, conn1, 4)
        self.ship_adder(player_1, conn1, 5)

        self.ship_adder(player_2, conn2, 2)
        self.ship_adder(player_2, conn2, 3)
        self.ship_adder(player_2, conn2, 3)
        self.ship_adder(player_2, conn2, 4)
        self.ship_adder(player_2, conn2, 5)

        while True:
            conn1.sendall(bytes("enter point to hit: x y".encode("utf-8")))
            points = str(conn1.recv(2028).decode("utf-8")).split(" ")
            conn1.sendall(player_2.hit_function(Point(int(points[0]), int(points[1]))).encode("utf-8"))
            if player_2.is_empty():
                conn1.sendall(bytes("player1 wins!!!".encode("utf-8")))
                conn2.sendall(bytes("player1 wins!!!".encode("utf-8")))
                break

            conn2.sendall(bytes("enter point to hit: x y".encode("utf-8")))
            points = str(conn2.recv(2028).decode("utf-8")).split(" ")
            conn2.sendall(player_1.hit_function(Point(int(points[0]), int(points[1]))).encode("utf-8"))
            if player_1.is_empty():
                conn1.sendall(bytes("player2 wins!!!".encode("utf-8")))
                conn2.sendall(bytes("player2 wins!!!".encode("utf-8")))
                break

        my_socket.close()

    
def main():
    game = Server(IP, PORT)
    game.start_game()
    
    
if __name__ == "__main__":
    main()
