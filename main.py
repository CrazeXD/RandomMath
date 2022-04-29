import time
import sys

import calculatepi
import constantratio
import pascalstriangle
import pascalwrap
import pythagorean
import sdt
import walls
import DPythagorean
import fibseq
import flip
import refraction

print("Welcome to Random Math Functions!")
print("Usage: Type h to print out options.")
packages = ["Speed-Distance-Time", "Fibbonaci Sequence", "Constant Ratio of Exponential Function", "Calculate Pi Using RNG",
            "Generate a Pascals Triangle", "Find (a+b)^n", "Schoolyard Fence Problem", "Pythagorean Theorem", "Shortest Path 3D Coordinates", "Coin Flip",
            "Refraction", "Exit"]
dicoptions = {}
length = len(packages)
for i in range(1, length + 1):
    j = str(i)
    print(f"{j}.", packages[i - 1])
    dicoptions[i] = packages[i - 1]
while True:
    options = input("> ")
    # Print out all the options
    if options.lower == "h" or options.lower == "help":
        dicoptions = {}
        for i in range(1, length + 1):
            j = str(i)
            print(f"{j}.", packages[i - 1])
            dicoptions[i] = packages[i - 1]
    elif options == str(length) or options == '':
        print("Thank you for using Random Math Functions!")
        time.sleep(2)
        sys.exit()
    else:
        choice = dicoptions.get(int(options))
        if choice == "Constant Ratio of Exponential Function":
            rows = int(input("Enter the number of rows in your table:\n"))
            if rows == 0:
                sys.exit()
            elif rows == 1:
                sys.exit()
            table = []
            obj = constantratio.getratio(rows, table)
            obj.findratios()
            a = obj.checkratio(obj.changes)
            obj.makeequation(a)
        elif choice == "Calculate Pi Using RNG":
            print(calculatepi.calcpi(int(input("How many points would you like to use?\n"))))
        elif choice == "Generate a Pascals Triangle":
            print(pascalstriangle.generate_triangle)
        elif choice == "Find (a+b)^n":
            pascalwrap.wrap()
        elif choice == "Schoolyard Fence Problem":
            length = int(input("What is the length? \n"))
            width = int(input("What is the width? \n"))
            start = int(input("Where are you starting from?\n"))
            location = input("Are you starting from W or L?\n")
            obj = walls.TouchAllWalls(length, width, start, location)
            obj.starters()
            print(obj.solve())
        elif choice == "Pythagorean Theorem":
            side1 = int(input("What is the length of the first side?\n"))
            side2 = int(input("What is the length of the second side?\n"))
            hypotenuse = input(
                "Are you solving for the hypotenuse or a side? Press enter or y for hypotenuse, n for a side: \n")
            if hypotenuse == "" or hypotenuse.lower == "y":
                print(pythagorean.calculate(side1, side2))
            elif hypotenuse.lower == "n":
                print(pythagorean.calculate(side1, side2, False))
            else:
                print("Not a valid option.")
        elif choice == "Speed-Distance-Time":
            newchoice = input("What do you want to calculate: Speed, Distance, or Time?\n")
            if newchoice.lower == "speed":
                distance = int(input("Enter the distance:\n"))
                time = int(input("Enter the time:\n"))
                print(sdt.speed(distance, time))
            elif newchoice.lower == "time":
                distance = int(input("Enter the distance:\n"))
                speed = int(input("Enter the speed:\n"))
                print(sdt.time(speed, distance))
            elif newchoice.lower == "distance":
                speed = int(input("Enter the speed:\n"))
                time = int(input("Enter the time:\n"))
                print(sdt.distance(speed, time))
            else:
                print("Syntax error: The input must be either 'speed' 'distance' or 'time.' ")
        elif choice == "Shortest Path 3D Coordinates":
            x1 = int(input("What is the first x coordinate?"))
            x2 = int(input("What is the second x coordinate?"))
            y1 = int(input("What is the first y coordinate?"))
            y2 = int(input("What is the second y coordinate?"))
            z1 = int(input("What is the first z coordinate?"))
            z2 = int(input("What is the second z coordinate?"))
            print(DPythagorean.hypotenuse(x1, y1, z1, x2, y2, z2))
        elif choice == "Fibbonaci Sequence":
            print(fibseq.fib(int(input("How many numbers should the program generate?\n"))))
        elif choice == "Coin Flip":
            amt = int(input("How many times would you like to flip?"))
            print(flip(amt))
        elif choice == "Refraction":
            pchoice = int(input("Would you like to find an index or an angle? 1 for index, 2 for angle:\n"))
            if pchoice == 1:
                print(refraction.index(int(input("What is the refractive index of the medium the beam is coming from?\n")), int(input("At what angle is the beam coming from?\n")), int(input("At what angle is the beam exiting?\n"))))
            elif pchoice == 2:
                print(refraction.angle(int(input("What is the refractive index of the medium the beam is coming from?\n")), int(input("What is the refractive index of the medium the beam is exiting from?\n")), int(input("At what angle is the beam coming from?\n"))))

