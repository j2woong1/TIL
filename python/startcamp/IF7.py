# SW Expert Academy 6227
# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분

arr = []
for i in range(100, 301):
    a = i
    t = False
    for k in range(3):
        if (i % 10) % 2 != 0:
            t = True
            break
        i = i // 10
    if not t:
        arr.append(str(a))  # 조인할때 타입을 맞춰야하므로 string으로 형변환
print(",".join(arr))
