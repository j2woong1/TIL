# SW Expert Academy 6238
# 1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.

result = ""
for i in range(1, 101):
    if i & 1:
        result += "%d, " % i
print(result[0:len(result) - 2])
