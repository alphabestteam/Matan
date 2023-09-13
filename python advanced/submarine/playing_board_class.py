

from ship_class import Ship
from point_class import Point


class Playing_board:
    def __init__(self) -> None:
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    def is_space(self, start_point: Point, end_point: Point) -> bool:
        """
        function that checks if place is available for ship
        input: Two points
        return: bool
        """
        if start_point.y == end_point.y:
            for i in range(start_point.x, end_point.x):
                if self.board[i][end_point.y] != 0:
                    return False
        else:
            for j in range(start_point.y, end_point.y):
                if self.board[end_point.x][j] != 0:
                    return False
                
        return True

    
    def insert_ship(self, ship: Ship) -> None:
        """
        insert ship to playing board
        input: ship of type Ship
        return None
        """
        if ship.horizontal:
            for i in range(ship.start_point.x, ship.end_point.x + 1):
                self.board[i][ship.end_point.y] = ship
        else:
            for j in range(ship.start_point.y, ship.end_point.y + 1):
                self.board[ship.end_point.x][j] = ship

    
    def hit_function(self, point: Point) -> str:
        """
        hit action function
        input: Point to check on
        return: Str with correct message
        """
        if self.board[point.x][point.y] == 0:
            return "miss!"
        else:
            self.board[point.x][point.y].health -= 1
            self.board[point.x][point.y] == 0

            if self.board[point.x][point.y].health == 0:
                return "Ship Destroyed"
            else:
                return "Hit!"
            
        
    def is_empty(self) -> bool:
        """
        returns if the board is empty or not
        """

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    return False
                
        return True
