# 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어가 회문이면 True 회문이 아니면 False를 반환하는 함수를 작성하시오.

def is_pal_while(word):
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
    return True

# 재귀
# def is_pal_recursive(word):
#     # 1. 종료조건 선언
#     if len(word) <= 1:
#         return True
#     # 2. 양 끝이 같으면 => 다음 subword를 넣어 함수 호출
#     if word[0] == word[-1]:
#         return is_pal_recursive(word[1:-1])
#     # 2-1. 다르면 => False
#     else:
#         return False
