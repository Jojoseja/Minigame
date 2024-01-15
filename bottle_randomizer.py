import random
# Func for number of bottles given a number of "bottles"


def cor_ans(num_bot):
    com = ""
    cor_gue = ""
    for i in range(1, num_bot + 1):
        com += str(i)
    game = True
    while game:
        num = str(random.randrange(1, len(com) + 1))
        if num not in cor_gue:
            cor_gue += str(num)
        if len(cor_gue) == len(com):
            game = False
    return cor_gue
