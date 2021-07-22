def my_max(*args):
    result = args[0]
    for value in args:
        if value > result:
            result = value
    return result


# def my_max(*args):
#     result = args[0]
#     for i in range(1, len(args)):
#         if args[i] > result:
#             result = args[i]
#     return result
print(my_max(-1, -2, -3, -4))
