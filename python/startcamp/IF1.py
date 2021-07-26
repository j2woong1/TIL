# SW Expert Academy 6218
# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오

a = int(input())
for i in range(1, a + 1):
    if not (a % i):
        print("%d(은)는 %d의 약수입니다." % (i, a))
