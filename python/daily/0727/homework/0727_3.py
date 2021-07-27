def lonely(nums):
    result = []

    for i, num in enumerate(nums):
        if i == 0:
            result.append(num)
        if result[-1] != num:
            result.append(num)
    return result


print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))