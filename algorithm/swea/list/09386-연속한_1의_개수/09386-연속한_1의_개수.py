"""
# 연속한 1의 개수
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력

첫 줄에 테스트케이스 개수 t
다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N
다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공

#과 테스트케이스 번호, 빈칸에 이어 답을 출력
"""

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    seq = input()  # 0, 1 수열

    long_one = 0  # 제일 긴 1의 연속을 저장
    length = 0  # 현재 연속된 1의 길이를 저장

    for i in range(len(seq)):
        # 만약에 현재 요소가 1이면 length 1 증가
        if seq[i] == '1':
            length += 1
        # 0이면 max와 비교해서 더 크면 max에 length 저장
        else:
            if long_one < length:
                long_one = length
            # cnt를 0으로
            length = 0
    if long_one < length:
        long_one = length
    print(f'#{tc} {long_one}')
