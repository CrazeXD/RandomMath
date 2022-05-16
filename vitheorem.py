def vitheorem(a, b, c):
    plus = -b/a
    times = c/a
    insidesqrt = plus**2
    insidesqrt-=4*times
    insidesqrt**=0.5
    insidesqrt+=plus
    insidesqrt/=2
    x2 = insidesqrt
    x1 = plus-x2
    if x1 == x2 and c>=0:
        return [x1, x2, -1*x1, -1*x2]
    return [x1, x2]