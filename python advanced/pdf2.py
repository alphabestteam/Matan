

def words_length(*args: str) -> int:
    """
    this function returns the length of words combined
    input: str args
    return: length -> int
    """
    sum_words = 0

    for word in args:
        sum_words += len(word)

    return sum_words


def total_ages(**kwargs):
    """
    this function returns the sum of ages and prints them out 
    input = variables of persons
    return = sum of ages
    """
    age_sum = 0

    for key, value in kwargs.items():  
        age_sum += value
        print(f"{key} : {value}")

    return age_sum



def main():
    print(words_length("matan", "hello"))
    print(total_ages(matan=5, timmy=7))

if __name__ == "__main__":
    main()