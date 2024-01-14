import random
# answer = var; range -> (1, var+1)


def bottles(num_bot):
    number_bottles = int(num_bot)
    kawai = ""
    correct_guess = ""
    for i in range(1, number_bottles + 1):
        kawai += str(i)
    game = True
    while game:
        awa = str(random.randrange(1, len(kawai) + 1))
        if awa not in correct_guess:
            correct_guess += str(awa)
        if len(correct_guess) == len(kawai):
            game = False
    return correct_guess
