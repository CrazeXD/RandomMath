import time
import sys

import intersect
import calculatepi
import constantratio
import doppler
from nthnum import nth_num
import pascalstriangle
import pascalwrap
from primefac import primefac
import pythagorean
import walls
import DPythagorean
import fibseq
import flip
import refraction
import vitheorem
import facfind
import mid
import doppler
import slope
import trianglerotate
import dilate
import areaoftriangle
import fma

print("Welcome to Random Math Functions!")
print("Usage: Type h, help, or ? to print out options.")
packages = ["Fibbonaci Sequence", "List the factors of a number", "List the prime factor of a number", "Find the nth number whose digits add up to a certain number", "Slope of a line", "Constant Ratio of Exponential Function", "Calculate Pi Using RNG",
            "Find the intersection of 2 lines", "Generate a Pascals Triangle", "Find (a+b)^n", "Find the roots of a quadratic equation", "Schoolyard Fence Problem", "Pythagorean Theorem", "Shortest Path 3D Coordinates", "Coin Flip",
            "Find the area of a triangle", "Rotate a triangle 90 degrees", "Dilate a triangle", "Midpoint", "Refraction", "Doppler Effect", "F=ma", "Exit"]
dicoptions = {}
length = len(packages)
for i in range(1, length + 1):
    j = str(i)
    print(f"{j}.", packages[i - 1])
    dicoptions[i] = packages[i - 1]
try:
    while True:
        options = input("> ")
        # Print out all the options
        if options == "h" or options == "help" or options == "?" or options == "H":
            dicoptions = {}
            for i in range(1, length + 1):
                j = str(i)
                if i<10:
                    print(f"{j}. ", packages[i - 1])
                else:
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
                print(calculatepi.calcpi(int(input("How many points would you like to use? Note: This calculation will never be accurate, unless you used infinity points.\n"))))
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
                hypotenuse = input("Are you solving for the hypotenuse or a side? Press enter or y for hypotenuse, n for a side: \n")
                if hypotenuse == '' or hypotenuse == "y" or hypotenuse == "Y":
                    print(pythagorean.calculate(side1, side2, True))
                elif hypotenuse == "n" or hypotenuse == "N":
                    print(pythagorean.calculate(side1, side2, False))
            elif choice == "Shortest Path 3D Coordinates":
                x1 = int(input("What is the first x coordinate?\n"))
                y1 = int(input("What is the first y coordinate?\n"))
                z1 = int(input("What is the first z coordinate?\n"))
                x2 = int(input("What is the second x coordinate?\n"))
                y2 = int(input("What is the second y coordinate?\n"))
                z2 = int(input("What is the second z coordinate?\n"))
                print(DPythagorean.hypotenuse(x1, y1, z1, x2, y2, z2))
            elif choice == "Fibbonaci Sequence":
                print(fibseq.fib(int(input("How many numbers should the program generate?\n"))))
            elif choice == "Coin Flip":
                amt = int(input("How many times would you like to flip?\n"))
                print(flip.flip(amt))
            elif choice == "Refraction":
                pchoice = int(input("Would you like to find an index or an angle? 1 for index, 2 for angle:\n"))
                if pchoice == 1:
                    print(refraction.index(int(input("What is the refractive index of the medium the beam is coming from?\n")), int(input("At what angle is the beam coming from?\n")), int(input("At what angle is the beam exiting?\n"))))
                elif pchoice == 2:
                    print(refraction.angle(int(input("What is the refractive index of the medium the beam is coming from?\n")), int(input("What is the refractive index of the medium the beam is exiting from?\n")), int(input("At what angle is the beam coming from?\n"))))
            elif choice == "Find the roots of a quadratic equation":
                a = int(input("What is the value of a in the quadratic equation?\n"))
                b = int(input("What is the value of b in the quadratic equation?\n"))
                c = int(input("What is the value of c in the quadratic equation?\n"))
                print(vitheorem.vitheorem(a, b, c))
            elif choice == "List the factors of a number":
                n = int(input("What number do you want to factor?\n"))
                print(facfind.facfind(n))
            elif choice == "Midpoint":
                print(mid.midpoint(int(input("What is the first x coordinate:\n")), int(input("What is the first y coordinate:\n")), int(input("What is the second x coordinate:\n")), int(input("What is the second y coordinate:\n"))))
            elif choice == "Doppler Effect":
                speed = int(input("What is the speed of the moving object/observer in m/s:\n"))
                sos = int(input("What is the speed of sound/light in the medium of which they are traveling in m/s:\n"))
                frequency = int(input("What is the frequency of the sound being emitted in Hz:\n"))
                direction = input("Is the moving emitter/observer heading towards the other emitter/observer(enter y for yes, n for no):\n")
                if direction == "y" or direction == "Y":
                    direction = True
                else:
                    direction = False
                observer = input("Is the observer moving or is the emitter moving(enter o for observer, e for emitter:\n")
                if observer == "o" or observer == "O":
                    observer = True
                else:
                    observer = False
                print(doppler.doppler(speed, sos, frequency, direction, observer))
            elif choice == "Slope of a line":
                print(slope.slope(int(input("What is the first x coordinate:\n")), int(input("What is the first y coordinate:\n")), int(input("What is the second x coordinate:\n")), int(input("What is the second y coordinate:\n"))))
            elif choice == "List the prime factor of a number":
                print(primefac(int(input("What is the number you want to factor?\n"))))
            elif choice == "Find the nth number whose digits add up to a certain number":
                print(nth_num(int(input("What is n?\n")), int(input("What is the sum of the digits?\n"))))
            elif choice == "Find the intersection of 2 lines":
                print(intersect.intersect(int(input("What is the first line slope:\n")), int(input("What is the first y intercept:\n")), int(input("What is the second line slope:\n")), int(input("What is the second y intercept:\n"))))
            elif choice == "Rotate a triangle 90 degrees":
                counter = int(input("Is the rotation counterclockwise (1) or clockwise (2)?\n"))
                if counter == 1:
                    counter = True
                elif counter == 2:
                    counter = False
                center = int(input("What is the x coordinate of the center of rotation?\n"))
                center2 = int(input("What is the y coordinate of the center of rotation?\n"))
                print(trianglerotate.trianglerotation(int(input("What is the first x coordinate:\n")), int(input("What is the first y coordinate:\n")), int(input("What is the second x coordinate:\n")), int(input("What is the second y coordinate:\n")), int(input("What is the third x coordinate:\n")), int(input("What is the third y coordinate:\n")), counter))
            elif choice == "Dilate a triangle":
                print(dilate.dilate(int(input("What is the first x coordinate:\n")), int(input("What is the first y coordinate:\n")), int(input("What is the second x coordinate:\n")), int(input("What is the second y coordinate:\n")), int(input("What is the third x coordinate:\n")), int(input("What is the third y coordinate:\n")), int(input("What is the x coordinate of the center of dilatiion?\n")), int(input("What is the y coordinate of the center of dilatiion?\n")), int(input("What is the dilation factor?\n"))))
            elif choice == "Find the area of a triangle":
                print(areaoftriangle.areatriangle(int(input("What is the base:\n")), int(input("What is the height:\n"))))
            elif choice == "F=ma":
              subchoice = input("Are you finding Force(f), Mass(m) Or Acceleration(a)?\n")
              subchoice = subchoice.lower()
              if subchoice == "f":
                print(fma.Force(int(input("What is the mass?\n")), int(input("What is the acceleration?\n"))))
              elif subchoice == "m":
                print(fma.Mass(int(input("What is the force?\n")), int(input("What is the acceleration?\n"))))
              elif subchoice == "a":
                print(fma.Acceleration(int(input("What is the force?\n")), int(input("What is the mass?\n"))))
              else:
                raise ValueError
              
except ValueError:
    print("Error in input. Now terminating process. Thank you for using Random Math Functions!")
    time.sleep(4)
    exit()
    