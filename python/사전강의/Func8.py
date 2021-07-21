# SW Expert Academy 6327
# 숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
# 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

def square(k):
    print("square(%d) => %d" % (int(k), int(k) ** 2))


k = input()
k = k.split(', ')
for i in k:
    square(i)
