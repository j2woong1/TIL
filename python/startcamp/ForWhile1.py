# SW Expert Academy 6230
# 60 이상일 때 합격 메시지를 출력하고, 60 미만일 때 불합격 메시지

result = [88, 30, 61, 55, 95]
for i in range(0, 5):
    if result[i] >= 60:
        ispass = "합격"
    else:
        ispass = "불합격"
    print("%d번 학생은 %d점으로 %s입니다." % (i + 1, result[i], ispass))
