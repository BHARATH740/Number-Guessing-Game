import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
print("Guess the number!!!")
GUESS = random.randint(0,101)
difficulty = input("Choose a difficulty. Type 'easy' and 'hard': ")
crt_guess = False

# print(GUESS)
def is_crt():
    guess = int(input("Make a guess: "))
    if guess<GUESS:
        print("Too low")
        print("Guess again.")
        return False
    elif guess>GUESS:
        print("Too high")
        print("Guess again.")
        return False
    elif guess == GUESS:
        return True   

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")
while attempts > 0:
    if not crt_guess :
        crt_guess=is_crt()
        attempts -= 1
        if not crt_guess:
            print(f"You have {attempts} attempts remaining to guess the number.")
            
    else :
        print("Hurray! You got it!! Your guess is correct!!!")
        break

if not crt_guess :
    print("You Lose!!.You ran out of attempts.")


input()