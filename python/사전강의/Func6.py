# SW Expert Academy 6325
# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,임이의 숫자의 포함 여부

def Check_for_existence(k, t):
    print("%d => " % t, end="")
    if t in k:
        print(True)
    else:
        print(False)


k = [2, 4, 6, 8, 10]
print(k)
Check_for_existence(k, 5)
Check_for_existence(k, 10)
