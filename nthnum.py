def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def nth_num(n, sum):
    num = 0
    while num < n:
        num += 1
        if sum == sum_digits(num):
            return num
    return -1