def fib(n):
    prev = 0
    otherprev = 0
    current = 1
    overall = [1]
    for i in range(n-1):
        overall.append(current+prev)
        otherprev = current
        current+=prev
        prev = otherprev
    return overall