# SW Expert Academy 6324
# 리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고 중복 항목을 제거

def list_to_set(k):
    # set의 특성을 이용하여 중복제거
    temp = set(k)
    # list로 재변환
    return list(temp)

k = [1, 2, 3, 4, 3, 2, 1]
print(k)
print(list_to_set(k))