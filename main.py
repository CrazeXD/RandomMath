import calculatepi, constantratio, pascalwrap, walls, pascalstriangle
import sys
print("Welcome to Random Math Functions!")
print("Usage: Type h to print out options.")
packages = ["Constant Ratio of Exponential Function", "Calculate Pi Using RNG", "Generate a Pascals Triangle", "Find (a+b)^n", "Schoolyard Fence Problem", "Exit"]
dicoptions = {}
length = len(packages)
for i in range(1, length+1):
    j = str(i)
    print(f"{j}.", packages[i-1])
    dicoptions[i] = packages[i-1]
while True:
    options = input("> ")
    #Print out all the options
    if options == "h":
        dicoptions = {}
        for i in range(1, length+1):
            j = str(i)
            print(f"{j}.", packages[i-1])
            dicoptions[i] = packages[i-1]
    elif options == str(length) or options == '':
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
