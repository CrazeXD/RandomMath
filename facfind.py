def facfind(n) -> list:
    factors = []
    for i in range(1, n+1):
        if n%i==0:
            factors.append(i)
    return factors