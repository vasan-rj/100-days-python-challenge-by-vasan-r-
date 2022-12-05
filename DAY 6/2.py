def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)

print(f'the factorial of 4 is {fact(4)}')