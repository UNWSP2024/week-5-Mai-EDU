# Program #2: Math Quiz
# Programmer: Mai Lillie
# Date: 10/4/24

#Gives us random operator
import random

#main program
def math_quiz():
    n1 = random.randint(1, 1000)
    n2 = random.randint(1, 1000)
    total = n1 + n2
    print("What is", n1, "+", n2,)
    answer = int(input("Answer: "))
    if answer == total:
        print("Congratulations, that's correct!")
    else:
        print("Incorrect. The correct answer is", total,)

#runs the program
math_quiz()
