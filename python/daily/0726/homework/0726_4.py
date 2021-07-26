def only_square_area(num1, num2):
    square = []

    for i in num1:
        for j in num2:
            if i == j:
                square.append(i ** 2)
    return square


print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
