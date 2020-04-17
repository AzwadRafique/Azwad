try:

    print("Welcome to Homework Buddy")
    print("Its an app where the graphics are not great")
    print("but it is an app which you will certainly not hate")
    problem = input("Enter a math problem or press q if you want to quit ")


    while problem.upper() != "Q":

        print(f"The answer is {eval(problem)}")
        problem = input("Enter a math problem or press q if you want to quit ")

    if problem.upper() == "Q":
        print("See you next time")


except NameError:
    print("sorry did not catch that please try again")
except SyntaxError:
    print("sorry did not catch that please try again")
