from pascalstriangle import generate_triangle
import sys
import time

def wrap():
    triangle = []

    try:
        exponent = int(input("Enter the exponent:\n"))
    except:
        print("Not a valid input")
        sys.exit()

    exptriangle = generate_triangle(exponent, triangle)

    expression = ''


    change = 0
    while exponent-change>0:
        expression+= f'{exptriangle[exponent][change]}a^{exponent-change}*b^{change} + '
        change+=1
    expression += f'a^0*b^{exponent}'
    print(expression)
