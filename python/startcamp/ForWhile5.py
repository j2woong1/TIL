# SW Expert Academy 6240
# 1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.

result = 0
for i in range(1, 101):
    if not (i % 3):
        result += i
print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(result))
