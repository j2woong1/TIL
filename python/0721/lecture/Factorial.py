a = int(input())
#반복
# # def fact(n):
# #     result = 1
# #     while n > 1:
# #         result *= n
# #         n -= 1
# #     return result
# #
# # print(fact(a))


#재귀
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

result = fact(a)
print(result)