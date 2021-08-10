"""
# 점점 커지는 당근의 개수
연속으로 당근의 크기가 커진 경우 그 개수를 알려준다
당근의 크기가 수확한 순서 : 연속으로 커지는 당근의 갯수는 최대 얼마인지 확인하기 위한 프로그램
연속으로 커지지않는 경우 구간의 최소 길이는 1

테스트케이스의 개수 t, 다음 줄 부터 테스트케이스별로 첫 줄에 당근 개수 N, 다음 줄 당근의 크기 C

# 테스트케이스번호와 연속으로 커지는 당근 개수의 최대값을 출력
"""

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    c = list(map(int, input().split()))

    cnt = 1
    size = 1

    for i in range(n - 1):
        if c[i] < c[i + 1]:
            cnt += 1

            if cnt > size:
                size = cnt
        else:
            cnt = 1

    print(f'#{tc} {size}')