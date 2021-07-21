# SW Expert Academy 6326
# 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한 팩토리얼 값 출력

def factorial(k):
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result

k = int(input())
print(factorial(k))
