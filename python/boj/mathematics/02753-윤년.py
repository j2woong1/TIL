# 윤년이면 1, 아니면 0을 출력
# 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수

yr = int(input())

if (yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0:
    print(1)
else:
    print(0)