

def series(N: int) -> None:
    """
    demonstrates f(n) = f(n-2) * f(n-1)
    """
    n_1 = 1
    n_2 = 2

    # first two numbers
    yield 1
    yield 2
    
    for _ in range(N - 2):
        yield n_1 * n_2
        save = n_1
        n_1 = n_2
        n_2 = n_1 * save


def main():
    
    for number in series(12):
        print(number)


if __name__ == "__main__":
    main()