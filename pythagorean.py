def calculate(side1, side2, hypotenuse=True):
    if hypotenuse:
        side1 = side1**2
        side2 = side2**2
        total = side1+side2
        return total**0.5
    else:
        if side1>side2:
            side1 = side1**2
            side2 = side2**2
            total = side1-side2
            return total**0.5
        elif side2<side1:
            side1 = side1**2
            side2 = side2**2
            total = side2-side1
            return total**0.5
