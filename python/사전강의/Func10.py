# # SW Expert Academy 6329
# 카운트다운 함수를 정의하고, countdown(0), countdown(10)을 순서대로 실행하십시오.
# 0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.

def countdown(k):
    if k <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    for i in range(k, 0, -1):
        print(i)


countdown(0)
countdown(10)
