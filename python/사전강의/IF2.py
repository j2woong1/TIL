# SW Expert Academy 6219
# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# (단, 약수가 2개일 경우 소수임을 나타내십시오)

a = int(input())
count = 0
for i in range(1, a + 1):  # 1부터 a까지
    if not (a % i):  # a가 i로 나눠지지 않으면
        print("%d(은)는 %d의 약수입니다." % (i, a))  # %d = 정수
        count += 1
    if count == 2: # 약수가 2개면
        print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (a, a))
