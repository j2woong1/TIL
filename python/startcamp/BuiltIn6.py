# SW Expert Academy 6315
# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해
# 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.

lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: pow(x, 2), lit))
print(result)
