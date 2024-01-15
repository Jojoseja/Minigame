from bottle_randomizer import *


# Game start func where I input the number of bottles
def game_start():
    num_bot = input("Number of bottles: ")
    cor_guess = cor_ans(num_bot)
    game(cor_guess)


# Func for starting over
def start_over():
    comment = input("Do you want another round? y/n:")
    try:
        if comment == "y":
            game_start()
    finally:
        pass


# Func for the game itself
def game(cor_guess):
    cor_guess = cor_guess
    guess = True
    correct = 0
    check = -1
    while guess:
        try:
            ans = str(input("Answer: "))
            if not ans.isdigit():
                print(f"Try a number with {len(str(cor_guess))} figures")
            if len(ans) != len(str(cor_guess)):
                print(f"Try a number with {len(str(cor_guess))} figures")
            break
        except ValueError:
            print("Try a number! ")
    for i in ans:
        check += 1
        if i == cor_guess[check]:
            correct += 1
    if correct == len(ans):
        print("you win")
        start_over()
    else:
        print(f"you have {correct} figures!")
        game(cor_guess)


game_start()
