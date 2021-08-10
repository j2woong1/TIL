"""
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
"""

t = int(input())

for tc in range(1, t + 1):
    # 카드 장 수
    # 한줄로 들어오는 숫자를 따로따로 분리
    # [4, 9, 6, 7, 9] 이런식
    n = int(input())
    nums = list(map(int, input()))

    # 0~9(10개)까지니까 각 숫자의 갯수를 담아줄 cnt리스트 만듬
    cnt = [0] * 10
    # 자기 자신에 해당하는 cnt의 idx값에 들어가서 +1 해주기
    for num in nums:
        cnt[num] += 1
    # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # 제일 큰 값을 cnt의 0번째로 지정하고
    max_cnt = cnt[0]
    # 위에서 0번째를 max_cnt_val정했으니까 1번째 인덱스부터 max_cnt_val와 값 비교
    for i in range(1, 10):
        # 카드 장수가 같은 경우도 봐줘야하니까 = 넣어야하고
        if cnt[i] >= max_cnt:
            # 카드 장수가 같으면 그 해당 인덱스 값을 res라는 새로운 변수에 저장
            ans = i
            max_cnt = cnt[i]
    print(f"#{tc} {ans} {max_cnt}")
