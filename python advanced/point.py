

class Point:
    def __init__(self, x: float, y: float) -> object:
        self.x = x
        self.y = y

    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    

    def __eq__(self, __point: object) -> bool:
        return self.x == __point.x and self.y == __point.y
    

    def __add__(self, __point: object) -> object:
        return Point(self.x + __point.x, self.y + __point.y)


def main():
    point_a = Point(3, 5)
    point_b = Point(3, 6)

    #Comparison
    print(point_a == point_b)

    #Print object
    print(point_a)
    print(point_b)

    #sum points
    print(point_a + point_b)


if __name__ == "__main__":
    main()