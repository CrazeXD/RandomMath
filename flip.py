import random

def flip(n):
    x = 0
    y = 0
    for i in range(n):
        val = random.randint(0, 1)
        if val == 0:
            x+=1
        else:
            y+=1
    return [x, y]