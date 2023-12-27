def sum_of_squares(n):
    sum = 0
    for i in range(1, n+ 1):
        sum += (i*i)
    return sum
    
n = int(input("enter any number : "))
result = sum_of_squares(n)
print(result)