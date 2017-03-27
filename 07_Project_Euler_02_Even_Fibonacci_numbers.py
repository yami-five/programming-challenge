def fib(n):
    if n in [1,2]:return 1
    elif n==0: return 0
    else: return fib(n-1)+fib(n-2)
n=int(input("Write n: "))
print(fib(n),)