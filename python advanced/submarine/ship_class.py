

from point_class import Point


class Ship:
    def __init__(self, start_point: Point, end_point: Point, health: int) -> None:
        if (start_point.x == end_point.x and start_point.y != end_point.y) or (start_point.x != end_point.x and start_point.y == end_point.y):
            self.start_point = start_point
            self.end_point = end_point
            self.health = health

            if self.start_point.x == self.end_point.x:
                self.horizontal = False
            else:
                self.horizontal = True 

        else:
            return False
        
    
    def get_length(self) -> int:
        """
        function that returns the length of the ship
        input: self
        return: int
        """
        if self.start_point.x == self.end_point.x:
            return abs(self.start_point.x - self.end_point.x)
        else:
            return abs(self.start_point.y - self.end_point.y)
        