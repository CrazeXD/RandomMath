import calculatepi, constantratio, pascalwrap, walls
import sys
print("Welcome to Random Math Functions!")
print("Usage: Type h to print out options.")
packages = ["Constant Ratio of Exponential Function", "Calculate Pi Using RNG", "Generate a Pascals Triangle", "Find (a+b)^n", "Schoolyard Fence Problem", "Exit"]

length = len(packages)
while True:
    options = input("> ")
    #Print out all the options
    if options == "h":
        for i in range(1, length+1):
            j = str(i)
            print(f"{j}.", packages[i-1])
    elif options == str(length):
        sys.exit()
