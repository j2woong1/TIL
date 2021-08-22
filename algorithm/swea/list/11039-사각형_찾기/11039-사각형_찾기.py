"""
# 사각형 찾기
사각형의 가로 세로 칸수를 곱한 값을 출력하는 프로그램을 만드시오.
사각형이 여러 개인 경우 곱이 가장 큰 경우를 출력

첫 줄에 테스트케이스 개수 T가 주어진다.
다음 줄부터 테스트케이스 별로 첫 줄에 N, N 줄에 걸쳐 N개의 0또는 1이 주어진다.

#에 이어 1번 부터인 테스트케이스번호, 빈칸에 이어 답을 출력
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_square = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                width, height = 0, 0
                for k in range(N - i):
                    if arr[i+k][j] == 1:
                        width += 1
                for l in range(N - j):
                    if arr[i][j+l] == 1:
                        height += 1
                square = width * height
                if max_square < square:
                    max_square = square

                for m in range(width):
                    for n in range(height):
                        arr[i+m][j+n] = 2

    print(f'#{tc} {max_square}')