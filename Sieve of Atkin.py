from random import randint
import time
import math
counter=2000000
prime_numbers1=[]
prime_numbers2=[]
def is_prime_atkin(n):
    if n==2 or n==3 or n==5: return True
    elif n%2!=0:
        if n%3!=0:
            if n%5!=0:
                if n%7!=0:
                    if n%11!=0:
                        for i in range(2,math.floor(math.sqrt(n))):
                            if n%i==0 and n!=i:return False
                    else: return False
                else: return False
            else: return False
        else: return False
    else: return False
    return True
start_time=time.time()
for i in range(2,counter):
    if is_prime_atkin(i)==True:
        prime_numbers1.append(i)
print("--- %s seconds ---" % (time.time() - start_time))
print(max(prime_numbers1))

