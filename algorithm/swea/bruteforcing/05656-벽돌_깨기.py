def dice(stage):
    # 종료조건
    if stage >= N:
        global arr, ans
        for c in shoot:
            for r in range(H):
                if arr[r][c]:
                    remove(r, c)
                    final()
                    break

        cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    cnt += 1
        ans = min(ans, cnt)
        # 복원
        arr = [list(n_arr[row]) for row in range(H)]
        return
    # 중복을 포함하여 val_c개에서 N개를 뽑는 순열(팩토리얼로 계산됨)
    for col in range(W):
        shoot[stage] = col
        dice(stage + 1)


# 각 구슬에 대해 벽돌이 꺠지는 함수
def remove(r, c):
    now = arr[r][c]
    arr[r][c] = 0
    for i in range(r - now + 1, r + now):
        if 0 <= i < H and arr[i][c] > 0:
            remove(i, c)
    for j in range(c - now + 1, c + now):
        if 0 <= j < W and arr[r][j] > 0:
            remove(r, j)


# 벽돌이 제거된 후 벽돌이 내려와 정리되는 함수
def final():
    # arr의 마지막 행에서부터의 모든 요소에 대해
    for i in range(H - 2, -1, -1):
        for j in range(W):
            # 현재 0이 아니고 아랫줄이 0이라면
            if arr[i][j] and not arr[i + 1][j]:
                r = i
                # 다음 줄이 경계밖이거나 값이 있을 때까지 행을 늘려 내려가고
                while r + 1 < H and not arr[r + 1][j]:
                    r += 1
                # 끝까지 내려간 곳의 값을 현재 값으로 바꾼 후, 현재 값은 0으로 바꾼다.
                arr[r][j], arr[i][j] = arr[i][j], 0


T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # 계속 판을 갖고 결과를 보고 복원해야 하므로 원본을 만들어 놓는다.
    n_arr = [list(arr[row]) for row in range(H)]
    ans = W * H
    shoot = [0] * N
    dice(0)
    if ans < 0:
        ans = 0
    print('#%d %d' % (t, ans))
