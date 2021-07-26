def my_list_max2(*numbers):
    max = 0
    answer = 0
    for number in numbers:
        if sum(number) > max:
            max = sum(number)
            answer = number
    return answer


print(my_list_max2([10, 3], [5, 91], [10, 4], [1, 2]))