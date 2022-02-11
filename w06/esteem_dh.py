def main():
    print("This program is an implementation of the Rosenberg \nSelf-Esteem Scale. This program will show you ten \nstatements that you could possibly apply to yourself. \nPlease rate how much you agree with each of the \nstatements by responding with one of these four letters:"
          )
    print("")
    print("D means you strongly disagree with the statement. \nd means you disagree with the statement. \na means you agree with the statement. \nA means you strongly agree with the statement.")

    score = 0
    score += question_positive("1. I feel that I am a person of worth, at least on an equal plane with others.")
    score += question_positive("2. I feel that I have a number of good qualities.")
    score += question_negative("3. All in all, I am inclined to feel that I am a failure.")
    score += question_positive("4. I am able to do things as well as most other people.")
    score += question_negative("5. I feel I do not have much to be proud of.")
    score += question_positive("6. I take a positive attitude toward myself.")
    score += question_positive("7. On the whole, I am satisfied with myself.")
    score += question_negative("8. I wish I could have more respect for myself.")
    score += question_negative("9. I certainly feel useless at times.")
    score += question_negative("10. At times I think I am no good at all.")
    
    print(f"Your score is {score}. \nA score below 15 may indicate problematic low self-esteem.")

def question_positive(question):
    print(question)
    response = input("Enter D, d, a, or A: ")
    score = 0
    if response == 'D':
        score = 0
    elif response == "d":
        score = 1
    elif response == 'a':
        score = 2
    elif response =='A':
        score = 3
    return score

def question_negative(question):
    print(question)
    response = input("D, d, a, or A ")
    score = 0
    if response == 'D':
        score = 3
    if response == 'd':
        score = 2
    if response == 'a':
        score = 1
    if response == 'A':
        score = 0
    return score 
    
    
main()

