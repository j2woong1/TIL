# SW Expert Academy 6221
# 가위 바위 보 게임

man1 = input()
man2 = input()
case = ["가위", "바위", "보"] # ["가위", "바위", "보"] 리스트

if case.index(man1) < case.index(man2):
    if case.index(man1) == 0 and case.index(man2) == 2:
        print("Result : Man1 Win1") # Man1이 이겼을 경우 Result : Man1 Win!
    else:
        print("Result : Man2 Win!")
if case.index(man1) > case.index(man2):
    if case.index(man1) == 2 and case.index(man2) == 0:
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
if case.index(man1) == case.index(man2): # 비긴 경우는 Result : Draw
    print("Result : Draw")
