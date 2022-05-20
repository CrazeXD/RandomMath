'''Find the sum of the digits of a number'''
def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

'''Program to find the nth number whose digits add to a given number'''
def nth_num(n, sum):
    num = 0
    while num < n:
        num += 1
        if sum == sum_digits(num):
            return num
    return -1