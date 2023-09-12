

from persons2 import Person


def two_nums() -> None:
    """ 
    prints two nums into the screen
    """
    flag = False

    try:
        num1 = int(input("enter first number"))
        num2 = int(input("enter second number"))
    except Exception as error:
        print(error)
        flag = True

    if not flag:
        print(f"{num1} {num2}")

    print("finish running!")


def main():
    two_nums()
    sq = [(x ** 2) for x in range(11)]
    person_list = [Person() for x in range(11)]
    person_list_over18 = [person for person in person_list if person.get_age() > 18]


if __name__ == "__main__":
    main()
