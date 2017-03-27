square_of_sum=0
sum_of_squares=0
for x in range(1,101):
    square_of_sum+=x
    sum_of_squares+=(x*x)
square_of_sum*=square_of_sum
difference=square_of_sum-sum_of_squares
print(difference)