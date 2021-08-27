def in_order(node):
    # 왼쪽
    if len(arr[node]) >= 3:
        in_order(int(arr[node][2]))
    # root
    print(arr[node][1], end="")
    # 오른쪽
    if len(arr[node]) == 4:
        in_order(int(arr[node][3]))


T = 10
for tc in range(1, T + 1):
    N = int(input())  # 정점의 총 수
    arr = [[]] + [input().split() for _ in range(N)]

    print("#{}".format(tc), end=" ")
    in_order(1)
    print()
