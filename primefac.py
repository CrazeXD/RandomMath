def primefac(n):
    if n == 1:
        return [1]
    else:
        for i in range(2,n+1):
            if n%i == 0:
                return [i] + primefac(n//i)