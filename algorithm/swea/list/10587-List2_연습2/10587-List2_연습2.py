"""
# List2_연습2
10개의 정수를 입력 받아 부분 집합의 합이 0이 되는지 확인

첫 줄에 테스트케이스 t, 다음 줄부터 테스트케이스 별로 절대값 1이상 20이하의 정수 10개가 제공

#과 테스트케이스 번호, 빈칸에 이어 부분집합의 합이 0이되는 경우가 있으며 1, 아니면 0을 출력
"""

t = int(input())

for tc in range(1, t + 1):
    nums = list(map(int, input().split()))
    # 총 부분 집합 개수 구하기
    # 1<<N N개의 정수들의 부분집합 총 개수
    # range(1, )은 0은 공집합이기 때문에 제외
    for i in range(1, 1 << 10):
        # 합계 초기화
        ans = 0
        # 부분집합 포함 원소 확인
        for j in range(len(nums)):
            if i & 1 << j:
                # 부분집합의 총합
                ans += nums[j]
        if ans == 0:
            print(f'#{tc} 1')
            break
    # for 문에서 break 걸리지 않고 빠져나왔을 때 실행
    else:
        print(f'#{tc} 0')