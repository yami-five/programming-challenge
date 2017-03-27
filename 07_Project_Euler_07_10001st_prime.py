import math
prime_numbers=[]
def is_prime_number(n):
    if len(prime_numbers)==0:
        return True
    else:
        for x in prime_numbers:
            if n%x==0:
                return False
    return True
counter=5000
number=1
while(counter!=10001):
    number+=1
    if is_prime_number(number)==True:
        prime_numbers.append(number)
        counter+=1
    
print("10001st prime number is ",number)