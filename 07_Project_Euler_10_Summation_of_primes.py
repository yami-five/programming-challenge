import time
start_time=time.time()
list_of_primes=[2,3,5,7,11,13,17,19]
def is_prime(n):
    if n%2!=0:
        if n%3!=0:
            if n%5!=0:
                if n%7!=0:
                    if n%11!=0:
                        if n%13!=0:
                            if n%17!=0:
                                if n%19!=0:
                                    for i in list_of_primes:
                                        if n%i==0: return False
                                else: return False
                            else: return False
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False
    else: return False
    print(n)
    return True
for i in range(2,2000000):
    if is_prime(i)==True:
        list_of_primes.append(i)
sum=1
for i in list_of_primes:
    sum+=i
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))