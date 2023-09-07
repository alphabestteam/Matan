

import math
import random


def sum_numbers(num1=0, num2=0) -> int:
    """
    this function returns the sum of 2 numbers
    input: two numbers
    return: sum of two numbers
    """
    return num1 + num2


def greating(name: str) -> None:
    """
    this function greats you!
    input: name -> str
    returns: None
    """
    print(f"Hello {name}!, Great to see u")


def quadratic(a=0, b=0, c=0) -> None:
    """
    function that returns the solutions of parabolic formula
    input = a, b and c
    returns = None
    """
    delta = b ** 2 - (4 * a * c)

    if delta < 0: 
        print("no real solutions")

    else:
        solution1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
        solution2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
        
        if solution1 == solution2:
            print("the solution is: " + str(solution1))
        else: 
            string = "the solutions are {} and {}".format(solution1, solution2)
            print(string)


def random_int(num1: int, num2: int) -> int:
    """
    this function generates a random number in the given range
    input: num1, num2 -> int ranges
    returns: the generated number
    """
    return random.randint(num1, num2)


def random_float(num1: float, num2: float) -> float:
    """
    this function generates a random number in the given range
    input: num1, num2 -> float ranges
    returns: the generated number
    """
    return random.uniform(num1, num2)



def main():
    # print(sum_numbers(8, 7))
    # greating("matan")
    # quadratic(2, 2)
    # print(random_int(12, 19))
    # print(random_float(12.7, 12.9))


if __name__ == "__main__":
    main()