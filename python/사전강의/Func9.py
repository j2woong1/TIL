# SW Expert Academy 6328
# 길이가 더 긴 문자열을 출력하는 함수

# 길이비교함수
def len_check(k):
    if len(k[0]) >= len(k[1]):
        print(k[0])
    else:
        print(k[1])

k = input()
# ,단위로 분류해서 리스트 만들기
k = k.split(', ')
len_check(k)