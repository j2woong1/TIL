a = int(input())

#반복
def fibo(n):
    if n < 2:
        return n
    
    a, b = 0,1
    
    for i in range(n-1):
        a, b = b, a+b
    return b

print(fibo(a))

#재귀
# def fibo(n):
#     if n <2:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# print(fibo(a))