def main():
    print(
        """This program is an implementation of the Rosenberg
    Self-Stability Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with tha statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.
    """
    )

    statements_dict = {
        "1. I feel that I am a person of worth, at least on an equal plane with others.": 1,
        "2. I feel that I have a number of good qualities.": 1,
        "3. All in all, I am inclined to feel that I am a failure.": -1,
        "4. I am able to do things as well as most other people.": 1,
        "5. I feel I do not have much to be proud of.": -1,
        "6. I take a positive attitude toward myself.": 1,
        "7. On the whole, I am satisfied with myself.": 1,
        "8. I wish I could be more respect for myself.": -1,
        "9. I certainly feel useless at times.": -1,
        "10. At times I think I am no good at all.": -1,
    }

    total_score = 0

    for key in statements_dict:
        print(key)
        choice = input("Enter D, d, a, or A: ")
        score = get_score(choice, statements_dict[key])
        total_score += score

    print("Your total score is:", total_score)


def get_score(choice, statement_score):
    """
    Prints the statement.
    Asks for a response.
    Returns the score of a statement.

    Parameter:
        statement: Statement from the statement list.
        statement_score: Score from the statement list.

    Returns:
        score: Score of the choice.
    """

    positive_dict = {
        "D": 0,
        "d": 1,
        "a": 2,
        "A": 3,
    }

    negative_dict = {
        "D": 3,
        "d": 2,
        "a": 1,
        "A": 0,
    }

    if statement_score == 1:
        score = positive_dict[choice]
    elif statement_score == -1:
        score = negative_dict[choice]

    return score


if __name__ == "__main__":
    main()
