# 첫째 줄에 1m2당 사람의 수 L, 파티가 열렸던 곳의 넓이 P
# 둘째 줄에는 각 기사에 실려있는 참가자의 수

L, P = map(int, input().split())
nums = list(map(int, input().split()))
party = L * P

for i in nums:
    print(i - party, end=' ')
