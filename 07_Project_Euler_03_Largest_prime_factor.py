import math
def prime_number(n):
    for x in range(2,math.floor(math.sqrt(n))):
        if n%x==0:
            return False
    return True
def prime_factor(n):
    for x in range(2,math.floor(math.sqrt(n))):
        if prime_number(x)==True and n%x==0:
            return x
    return n
x=0
n=600851475143
print("Largest prime factor of", n,"is: ")
while(n>1):
    buff=prime_factor(n)
    if buff == None:
        break
    n=n//buff
    if buff>x:
        x=buff
print(x)
