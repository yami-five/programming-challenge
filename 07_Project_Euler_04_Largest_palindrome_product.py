import math
def is_palindrom(n):
    a=len(str(n))-1
    for x in range(0,math.floor(len(str(n))/2)):
        if str(n)[x]!=str(n)[x+a]:
           return False
        a-=2
    print(n)    
    return True
#############################
var=0
for i in range(100,1000):
    for j in range(100,1000):
        if j==100:print(i)
        check=is_palindrom(i*j)
        if check==True:
           if i*j>var:var=i*j
print(var)
