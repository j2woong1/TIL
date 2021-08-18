"""
# 파스칼의 삼각형
첫 번째 줄은 항상 숫자 1
두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력

첫 줄에 테스트 케이스의 개수 T
각 테스트 케이스에는 N

각 줄은 '#t' 로 시작, 다음 줄부터 파스칼의 삼각형을 출력
처음 숫자가 나오기 전까지의 빈 칸은 생략, 숫자들 사이에는 한 칸의 빈칸 출력
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    pascal = list([0] * x for x in range(1, N + 1))  # 이차원 리스트 생성
    for i in range(N):
        for j in range(len(pascal[i])):  # i번째 리스트의 갯수만큼
            if j == 0:  # 첫번째 idx 1
                pascal[i][j] = 1
            if j == len(pascal[i]) - 1:  # 마지막 idx 1
                pascal[i][j] = 1
            elif j > 0:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    print(f'#{tc}')
    for a in pascal:  # 이차원 리스트 프린트
        for b in a:
            print(b, end=' ')
        print()
