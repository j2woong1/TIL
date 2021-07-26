# SW Expert Academy 6242
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

# 딕셔너리 구조사용
result = {"A": 0, "B": 0, "AB": 0, "O": 0}
students = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# 반복문을 돌면서 딕셔너리 값 증가
for s in students:
    result[s] += 1
print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" % (result["A"], result["O"], result["B"], result["AB"]))
