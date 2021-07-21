# SW Expert Academy 6311
# A는 4점, B는 3점, C는 2점, D는 1점
# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

t_str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
str_list = list(t_str)
t = list(map(lambda c: ord('E') - ord(c), str_list))
print(sum(t))
