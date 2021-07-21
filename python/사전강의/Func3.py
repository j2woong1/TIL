# SW Expert Academy 6321
# 소수를 검사
# 소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력

# 소수판별 함수
def PrimeNumber(k):
    # 2보다 0이나 1이라면 소수가 아니므로 리턴
    if k == 1:
        return False
    # 2부터 루트k까지 반복하며 체크
    # float은 범위표시로 못들어가므로 반올림한값에 +1을 해준다.
    # +1을 한이유는 두번째 인자값은 그값 이전까지이기 때문이다.
    k_root = round(k ** 0.5) + 1
    for i in range(2, k_root):
        # k가 i에 나누어 떨어진다면 소수가 아님
        if not (k % i):
            return False
    return True

num = int(input())
if PrimeNumber(num):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")