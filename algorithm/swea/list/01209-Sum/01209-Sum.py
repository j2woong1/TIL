"""
# Sum
100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
총 10개의 테스트 케이스
동일한 최댓값이 있을 경우, 하나의 값만 출력

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력
"""

for t in range(1, 11):
    n = int(input())
    arr = []
    for _ in range(100):
        arr += [list(map(int, input().split()))]

    arr_max = arr_sum = 0
    for i in range(100):
        for j in range(100):
            arr_sum += arr[i][j]
        if arr_max < arr_sum:
            arr_max = arr_sum
        arr_sum = 0

    for i in range(100):
        for j in range(100):
            arr_sum += arr[j][i]  # i, j 위치를 바꾼다.
        if arr_max < arr_sum:
            arr_max = arr_sum
        arr_sum = 0

    for i in range(100):
        arr_sum += arr[i][i]
    if arr_max < arr_sum:
        arr_max = arr_sum
    arr_sum = 0

    for i in range(100):
        arr_sum += arr[i][99 - i]
    if arr_max < arr_sum:
        arr_max = arr_sum

    print(f"#{t} {arr_max}")
