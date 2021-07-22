# 파이썬 내장 함수 `all()`을 직접 구현한 `my_all()`을 작성하시오.

def my_all(elements):
    # 1. 변수 초기화
    result = True
    # 2. 반복
    for element in elements:
        # 3. 조건 - 요소가 참이 아니라면
        # 해당 값이 참인지 거짓인지 알기 위해서는 bool 즉 아래와 같이 생각할 수 있는데,
        # if bool(element) == False:
        # 거짓인지 확인하는 것은 not True를 확인하는 것이다.
        # if not bool(element):
        # if에서는 자동 형변환이 발생한다.
        # 따라서, 다음과 같이 작성할 수 있다.
        if not element:
            result = False
            # 4. 한번이라도 발생하면 종료시켜야 하기 때문에, break
            break
    # 5. 반환
    return result

# 그럼 이제 비어있는 경우는 어떻게 처리될까?
# 아니다. 비어있다면 반복문이 돌지 않을 것이고, 바로 result에 True가 반환된다.
# 즉 이 로직에서는 따로 예외처리를 할 필요가 없다.

# 함수는 return과 함께 호출이 종료된다.
# 즉, 함수라면 아래와 같이 작성이 가능하다.
# def my_all(elements):
#     for element in elements:
#         # 하나라도 거짓이면,
#         if not element:
#             # False 반환
#             return False
#     # False 반환된 적이 없다면, 모두 참이므로 True
#     return True

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))