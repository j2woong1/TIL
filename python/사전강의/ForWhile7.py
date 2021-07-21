# SW Expert Academy 6244
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.

students = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result = 0
# 길이가 0이 될때까지 반복
while len(students):
    # 원소를 하나 꺼내서 k에 넣는다, 길이가 1감소됨
    k = students.pop()
    # 원소가 80보다 크다면 결과값에 더한다
    if k >= 80:
        result += k
print(result)
