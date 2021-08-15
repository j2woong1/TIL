"""
# GNS
이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
작은 수부터 차례로 정렬하여 출력

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
그 다음 줄에 # 기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력
"""

T = int(input())

for tc in range(1, T + 1):
    order = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    n = input()
    arr = input().split()

    for i in arr:
        order[i] += 1
    ans = ''

    for key, value in order.items():
        tmp = ' '.join([key] * value)
        ans += tmp + ' '  # zro 다음 one 을 출력할 때 띄어쓰기

    print(f"#{tc}")
    print(ans[:len(ans) - 1])  # 마지막에 띄어쓰기가 포함되어 있으므로 삭제
