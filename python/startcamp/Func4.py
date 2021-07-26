# SW Expert Academy 6323
# 다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.

def fibonacii(k):
    fibo = [1] * k
    for i in range(2, k):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo


k = int(input())
print(fibonacii(k))
