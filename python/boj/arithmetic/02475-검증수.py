# 첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩
# 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

nums = list(map(int, input().split()))
ans = 0
for i in nums:
    ans += i ** 2

print(ans % 10)