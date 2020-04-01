import random


number = random.randint(1, 100)
print("Guess the number I am thinking of")
while 1 == 1:
    try:
        guessed = input(' ')
        if int(guessed) == number:
            print("congratulations you guessed correctly")
            break

        elif int(guessed) > number:
            print(f'The number is less than {guessed}')

        else:
            print(f'The number is more than {guessed}')
    except ValueError:
        print("sorry this is not a number")
