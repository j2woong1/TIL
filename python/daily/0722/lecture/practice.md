# 1. 함수

## 1. ABS 구현

```python
# 숫자형 자료(int, float) : 절댓값, 복소수형 자료(complex) : 해당 자료 크기

def my_abs(x):
    # 1. 복소수이면, 
    if type(x) == complex:
    # if type(x) is complex:
    # if isinstance(x, complex): 비교하는 또다른 방법, OOP 수업에서 다룰 것이다.
        return (x.imag**2 + x.real**2) ** (1/2)
    # 2. 복소수가 아니면,
    else:
        if x == 0:
            return x ** 2
        if x < 0:
            return x * -1
        else:
            return x
```

## 2. ALL 구현

```python
#  iterable(range, list)의 모든 요소가 참이거나 비어있으면 True

# 하나씩 비교하면서, 모든 요소가 참이거나, 비어있으면..!
# 먼저 모든 요소를 순회하면서 (반복문)
# 각 요소가 참이 아니면, (조건문)
# False로 => 즉, 초기값은 True
def my_all(elements):
    # 1. 변수 초기화
    result = True
    # 2. 반복
    for element in elements:
        # 3. 조건 - 요소가 참이 아니라면
        # # 해당 값이 참인지 거짓인지 알기 위해서는 bool 즉 아래와 같이 생각할 수 있는데,
        # if bool(element) == False:
        # # 거짓인지 확인하는 것은 not True를 확인하는 것이다.
        # if not bool(element):
        # # if에서는 자동 형변환이 발생한다.
        # # 따라서, 다음과 같이 작성할 수 있다.
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
def my_all(elements):
    for element in elements:
        # 하나라도 거짓이면,
        if not element:
            # False 반환
            return False
    # False 반환된 적이 없다면, 모두 참이므로 True
    return True
```

## 3. ANY 구현

```python
# iterable(range, list)의 요소 중 하나라도 참이면 True, 비어있으면 False

def my_any(elements):
    for element in elements:
        if element:
            return True
    return False
```

## 4. 달팽이

```python
def snail(height, day, night):
    count = 0
    while True:
        count += 1
        height -= day
        if height <= 0:
            return count
        height += night
```

## 5. 자릿수 더하기

```python
def sum_of_digit(number):
    # 1. 변수 초기화
    total_sum = 0
    # 2. 한자리의 경우 0/10 => 0 즉, False 가 될 때까지.
    while number / 10:
        # 3. 몫과 나머지를 분리하기
        # 아래의 코드는 number, remainder = divmod(number, 10) 으로 변경 가능하다.
        remainder = number % 10
        number = number // 10
        # 4. 나머지를 더하기
        total_sum += remainder
    return total_sum

print(sum_of_digit(1234))

# 재귀
def sum_of_digit(number):
    if number < 10:
        return number
    else:
        number, remainder = divmod(number, 10)
        return sum_of_digit(number) + remainder
```



# 2. 자료 구조

## 1. 회문 판별

```python
# 해당 단어가 회문이면 True 회문이 아니면 False

def is_pal_while(word):
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
    return True

# 재귀
def is_pal_recursive(word):
    # 1. 종료조건 선언
    if len(word) <= 1:
        return True
    # 2. 양 끝이 같으면 => 다음 subword를 넣어 함수 호출
    if word[0] == word[-1]:
        return is_pal_recursive(word[1:-1])
    # 2-1. 다르면 => False
    else:
        return False
```

