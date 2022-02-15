from random import uniform, choice


def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_number(numbers)
    print(numbers)
    append_random_number(numbers, 3)
    print(numbers)

    words = []
    print(words)
    append_random_words(words)
    print(words)
    append_random_words(words, 3)
    print(words)


def append_random_words(list, quantity=1):
    """
    Chooses a random word from a list and appends it to the list

    Parameters:
        list: list of words where the word will be append to
        quantity: number of random words to append

    Returns:
        None
    """
    random_word_lst = ["hello", "world", "python", "programming", "is", "fun"]
    for _ in range(quantity):
        list.append(choice(random_word_lst))


def append_random_numbers(list, quantity=1):
    """
    Appends a random number to the list

    Parameters:
        list: list of numbers
        quantity: number of random numbers to append

    Returns:
        None
    """
    for _ in range(quantity):
        list.append(round(uniform(0, 100), 2))


if __name__ == "__main__":
    main()
