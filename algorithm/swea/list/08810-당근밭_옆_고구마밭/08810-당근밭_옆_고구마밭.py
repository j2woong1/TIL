"""
어떤 구역에 이웃한 오른쪽 구역의 고구마 개수가 더 많으면, 두 구역의 모든 고구마가 하나의 줄기에 매달려 있음
두개 이상의 구역에 걸쳐 있는 줄기 ‘긴 줄기’
고구마 밭에는 총 몇 개의 긴 줄기가 있는지, 그리고 가장 긴 줄기에 달린 고구마는 모두 몇개인지 알아내는 프로그램
가장 긴 줄기가 여럿일 때는 고구마의 개수가 많은 쪽을 가장 긴 줄기로 선택
"""

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    c = list(map(int, input().split()))

    ans = list()
    temp = [c[0]]
    max_len, max_sum, cnt = 0, 0, 0

    for i in range(n - 1):
        if c[i] < c[i + 1]:
            temp.append(c[i + 1])
        else:
            ans.append(temp)
            temp = [c[i + 1]]
        if i == n - 2:
            ans.append(temp)

    for stem in ans:
        if len(stem) > 1:
            if max_len < len(stem):
                max_len = len(stem)
                max_sum = sum(stem)
            if len(stem) == max_len:
                if sum(stem) > max_sum:
                    max_sum = sum(stem)
            cnt += 1
    print(f'#{tc} {cnt} {max_sum}')
