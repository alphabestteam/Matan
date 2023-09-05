

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

def main():
    my_sum = sum([num for num in range(1, 101)])
    print(my_sum)

    print(prime(5))
    print(prime(6))
    print(prime(7))
    print(prime(14))
    print(prime(152))
    print(prime(60693))


if __name__ == "__main__":
    main()