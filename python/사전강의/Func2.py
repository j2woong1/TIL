# SW Expert Academy 6320
# 다음과 같이 사용자 2명의 가위, 바위, 보

lis = ["가위", "바위", "보"]


def Check(a, b):
    if a == b:
        print("비겼습니다!")
    elif (a == lis[0] and b == lis[1]) or (b == lis[0] and a == lis[1]):
        print("바위가 이겼습니다!")
    elif (a == lis[0] and b == lis[2]) or (b == lis[0] and a == lis[2]):
        print("가위가 이겼습니다!")
    elif (a == lis[1] and b == lis[2]) or (b == lis[1] and a == lis[2]):
        print("보가 이겼습니다!")


name1, name2 = input(), input()
t1, t2 = input(), input()
Check(t1, t2)
