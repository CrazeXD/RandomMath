import random

def calcpi(n):
    circle = 0
    square = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        x=x**2
        y = y**2
        xy = x+y
        xy = xy**0.5
        if xy <=1:
            circle+=1
            square+=1
        else:
            square+=1

    cs = circle/square
    pi = cs*4
    return pi

#print(calcpi(int(input("How many points would you like to use?\n"))))
