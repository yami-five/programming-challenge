import math
import time
def pytha(a,b,c):
    if math.sqrt(a*a+b*b)==c:
        return True
    else: return False
a=199
b=a+1
c=0
check=False
while(a<b and check!=True):
    a+=1
    b=(a+1)
    c=1000
    c-=(b+a)
    while(b<c and check!=True):
        check
        if pytha(a,b,c)==True:
            check=True
        else:
            b+=1
            c=1000
            c-=(b+a)
        time.sleep(0.2)

    print("I'm out")
print("a=",a,"\nb=",b,"\nc=",c,"\na*b*c=",a*b*c)



#print(pytha(3,4,6))
