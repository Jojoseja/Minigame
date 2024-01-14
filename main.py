from bottle_randomizer import *

def game_start():
    start = input("Number of bottles: ")
    ans = bottles(start)
    game(ans)


def game(jojo):
    total_bottles = jojo
    answer = str(input("Answer: "))
    num = -1
    counter = 0
    for i in answer:
        num += 1
        if i == total_bottles[num]:
            counter += 1
    print(f"You have {counter} correct guesses!")
    if len(answer) != len(total_bottles):
        print("Insert an available answer!")
        game(jojo)
    if counter != len(total_bottles):
        print(f"Last Answer was: {answer}")
        game(jojo)
    if counter == len(total_bottles):
        print(f"You win!")


game_start()
