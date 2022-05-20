def intersect(slope, yint, slope2, yint2):
    if slope == slope2:
        return "Parallel lines"
    elif slope == 0:
        return "Vertical line"
    elif slope2 == 0:
        return "Vertical line"
    elif yint == yint2 and slope == slope2:
        return "Same line"
    else:
        x = (yint2 - yint) / (slope - slope2)
        y = slope * x + yint
        return [x, y]