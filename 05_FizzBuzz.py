for x in range(1,100):
    if x%3==0 and x%5==0: print("FizzBuzz")
    elif x%5==0: print("Buzz")
    elif x%3==0: print("Fizz")
    else: print(x)