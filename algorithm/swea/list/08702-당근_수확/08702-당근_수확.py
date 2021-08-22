"""
첫번째 일꾼은 1번 영역부터 연속으로 몇 개의 영역을 수확,
두번째 일꾼은 바로 다음부터 N번까지의 영역을 수확할 때,
두 일꾼이 수확한 당근의 수가 비슷하게 구역을 나누려고 합니다.
첫 번째 일꾼이 몇 번 영역까지 수확할 때 두 일꾼이 수확한 당근 개수의 차이가 최소가 되는지 알아내는 프로그램
만약 여러 영역이 가능한 경우 가장 빠른 번호를 선택
"""

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    carrot = list(map(int, input().split()))
    ans = []

    for i in range(n):
        a = sum(carrot[:i + 1])
        b = sum(carrot[i + 1:])
        ans.append((i + 1, abs(a - b)))
    work = 0
    diff = float('inf')

    for r in ans:
        if r[1] < diff:
            work = r[0]
            diff = r[1]
    print(f'#{tc} {work} {diff}')
