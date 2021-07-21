# SW Expert Academy 6207
# 섭씨(℃)를 화씨(℉)로 변환하는 프로그램을 작성하십시오.

a = float(input())
print("%0.2f ℃ =>  %0.2f ℉" % (a, 32 + a * 9 / 5))