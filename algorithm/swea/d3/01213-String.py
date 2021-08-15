"""
# String
특정한 문자열의 개수를 반환하는 프로그램을 작성

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고
그 다음 줄에는 찾을 문자열,
그 다음 줄에는 검색할 문장이 주어진다.

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력
"""

t = 0

while t < 10:
    num = int(input())
    words = input()
    sentence = input()

    # 매칭되는 횟수 초기화
    cnt = 0

    # 문장 속에서 문장 길이를 고려하여 단어를 비교
    for i in range(len(sentence) - len(words) + 1):
        # 동일하면 1 추가
        if sentence[i:i + len(words)] == words:
            cnt += 1

    print(f'#{num} {cnt}')
    t += 1