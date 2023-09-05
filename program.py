

import math


def prime(number: int) -> bool:
    """
    function that prints if the number is print(prime
    input: number int 
    output: bool 
    """
    for numcheck in range(2, int(number/2)):
        if number % numcheck == 0:        
            return False
        
    return True
  

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

    
    print(prime(5))
    print(prime(6))
    print(prime(7))
    print(prime(14))
    print(prime(152))
    print(prime(60693))
    print(factorial(6.5))
    print(factorial(7))
    print(factorial(8))


if __name__ == "__main__":
    main()