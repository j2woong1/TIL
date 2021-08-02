# 첫째 줄에 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수
# 첫째 줄에 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력

chess = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i] - white[i], end=' ')
