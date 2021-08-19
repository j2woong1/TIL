"""
양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다
조망권이 확보된 세대의 수를 반환
"""

for tc in range(10):
    n = int(input())
    height = list(map(int, input().split()))

    ans = 0

    for i in range(2, n - 2):
        build = max(height[i+1], height[i+2], height[i-1], height[i-2])
        if height[i] - build > 0:
            ans += height[i] - build
    print(f'#{tc+1} {ans}')