# 파이썬 내장 함수 `any()`을 직접 구현한 `my_any()` 함수를 작성하시오.

def my_any(elements):
    for element in elements:
        if element:
            return True
    return False

print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0])