# 가진 돈 n과 돈을 받으러 온 생명체의 수 m
# 첫째 줄에 생명체 하나에게 돌아가는 돈의 양
# 두 번째 줄에는 1원씩 분배할 수 없는 남는 돈을 출력

n, m = map(int, input().split())

print(n // m)
print(n % m)