import math

values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
cnt = len(values)
mean = sum(values) / cnt
sum_var = sum(pow(value - mean, 2) for value in values) / cnt
std_dev = math.sqrt(sum_var)
print(std_dev)

import statistics
    
values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
statistics.pstdev(values)
print('')

num1 = 0
num2 = 1


def func1(a, b):
    return a + b


def func2(a, b):
    return a - b


def func3(a, b):
    return func1(a, 5) + func2(5, b)


result = func3(num1, num2)
print(result)
