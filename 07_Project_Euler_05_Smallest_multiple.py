import math
prime_numbers=[]
num_to_mul=[]
numbers=[]
def is_prime_number(n):
    for i in range(2,n):
        if n%i==0: return False
    return True

for x in range(2,21):
    if is_prime_number(x)==True: 
        prime_numbers.append(x)

for i in range(20,1,-1):
    n=i
    del numbers[:]
    numbers=[]
    while(n>1):
        for x in prime_numbers:
            if n%x==0:
                n=n/x
                numbers.append(x)
        for x in numbers:
            if x not in num_to_mul:
                num_to_mul.append(x)
            elif num_to_mul.count(x)<numbers.count(x) and num_to_mul.count(x)>0:
                for y in range(0,(numbers.count(x)-num_to_mul.count(x))):
                	    num_to_mul.append(x)
multiple=1
for x in num_to_mul:
    multiple*=x
print(multiple)        