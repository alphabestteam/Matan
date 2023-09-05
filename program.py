

import math

def factorial(num: int) -> int:
    """
    function that returns the factorial value of a number
    input: int-> number
    return: the factorial result
    """
    if type(num)!= int:
        return None
    
    return math.factorial(num)


def main():
    my_sum = sum([num for num in range(1, 101)])
    print(my_sum)

    print(factorial(6.5))
    print(factorial(7))
    print(factorial(8))


if __name__ == "__main__":
    main()