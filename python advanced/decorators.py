

import time


def timmer(func):
    def inner(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        t1 = time.time()
        print(f"total running time: {t1 - t0}")
    return inner


@timmer
def print_random():
    print("blahblah")
    time.sleep(1)


def main():
    print_random()


if __name__ == "__main__":
    main()