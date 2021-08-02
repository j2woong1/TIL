# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed

scale = list(map(int, input().split()))

if scale == sorted(scale):
    print('ascending')
elif scale == sorted(scale, reverse=True):
    print('descending')
else:
    print('mixed')
