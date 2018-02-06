import random
my_random_number = random.randint(1, 10)
print("I am thinking of a number form 1 to 10")
guesses = 0
while guesses < 5:
    print("You have", 5 - guesses, "guesses left")
    guesses += 1
    raw_input = input("What's the number?")
    guess_number = int(raw_input)
    print(guess_number)
    if guess_number == my_random_number:
        print("Yes! You win!")
        continue_play = input("Do you want to play again?""Y/N").upper()
        if continue_play == "Y":
            guesses = 0
        else:
            print ("Bye!")
            break
    else:
        if guess_number < my_random_number:
            print(guess_number, "is too low.")
        else:
            print(guess_number, "is too high.")
    if guesses == 5:
        print("You are out of guesses")
        continue_play1 = input("Do you want to play again?""Y/N").upper()
        if continue_play1 == "Y":
            guesses = 0
        else:
            print("Bye")
