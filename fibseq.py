def fib(n):
    prev = 1
    current = prev
    output = ""
    for i in range(n):
        output+=str(current)
        output+=""
        prev = current
        current = current+prev
    return(output)

print(fib(10))