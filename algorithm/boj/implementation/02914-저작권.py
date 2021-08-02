# 첫째 줄에 앨범에 수록된 곡의 개수 A와 평균값 I
# 첫째 줄에 적어도 몇 곡이 저작권

A, I = map(int, input().split())
print(A * (I - 1) + 1)