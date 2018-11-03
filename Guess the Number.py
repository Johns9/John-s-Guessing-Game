#https://www.youtube.com/watch?v=duwiPfyRfnw I used this video as inspiration but I added my own spin on it.
import random

print("Welcome!")
print("Guess my number! You will have 5 tries.")

number_of_tries = 5
number_of_tries2 = 0

Player_Won = False

correct_number = random.randint(1, 10)

while number_of_tries > 0:

    number_of_tries -= 1
    number_of_tries2 += 1

    Player_1 = input("Pick a number between 1 and 10.")
    Player_1 = int(Player_1)

    if Player_1 == correct_number:
        print("That's Correct!")
        Player_Won = True
        break

    elif number_of_tries == 0:
        Player_Won = False
        print("You have", number_of_tries, "tries left!")
        break

    elif Player_1 > correct_number:
        print("That's too High! You have", number_of_tries, "tries left! Try again.")

    elif Player_1 < correct_number:
        print("That's too Low! You have", number_of_tries, "tries left! Try again.")


if Player_Won:
    print("You win! It took you", number_of_tries2, "tries to guess my number.")
else:
    print("My correct number was", correct_number,)
    print("Game Over")


