# 1. Function

## 1. 표준편차

```python
# 1

import math

values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
cnt = len(values)
mean = sum(values) / cnt
sum_var = sum(pow(value - mean, 2) for value in values) / cnt
std_dev = math.sqrt(sum_var)
print(std_dev)

# 2

import statistics

values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
statistics.pstdev(values)
print('')

num1 = 0
num2 = 1
```

## 2. 예시

```python
def func1(a, b):
    return a + b


def func2(a, b):
    return a - b


def func3(a, b):
    return func1(a, 5) + func2(5, b)


result = func3(num1, num2)
print(result) # 9
```

## 3. 세제곱

```python
def cube(a):
    return a ** 3


n1 = cube(int(input()))
n2 = cube(int(input()))

print(n1)
print(n2)
```



# 2. Output

## 1. 리턴

- 복수 객체 : 하나의 tuple
- 명시적 value X () : None 

```python
horizon = int(input())
vertical = int(input())


def rectangle(horizon, vertical):
    round = 2 * horizon + 2 * vertical
    area = horizon * vertical
    return round, area


result = rectangle(horizon, vertical)

print(result)
```



# 3. Input

## 1. 위치 인자 (Positional Argument)

```python
def add(x, y):
	return x + y
add(2, 3)
```

## 2. 기본 인자 값 (Default Arguments Values)

```python
def add(x, y = 0):
	return x + y
add(2)
```

## 3. 키워드 인자 (Keyword Arguments)

```python
def add(x, y):
	return x + y
add(x=2, y=5)
add(2, y=5)
```

## 4. 가변 인자 리스트 (Arbitrary Argument Lists)

```python
# 튜플 처리
def add(*args):
	for arg in args:
		print(arg)
add(2)
add(2, 3, 4, 5)
```

## 5. 가변 키워드 인자 (Arbitrary Keyword Arguments)

```python
# 딕셔너리
def family(**kwargs):
	for key, value in kwargs:
		print(key, ":", value)
family(father='John', mother='Jane', me='John Jr.')
```

## 6. 주의 사항

```python
def greeting(name='john doe', age): # SyntaxError
add(x=3, 5) # SyntaxError
```



# 4. Scope

## 1. Scope

- 코드 내부 지역 스코프 (local) : 코드 어디에서든 참조
- 그 외 전역 스코프 (global) : 함수 스코프, 함수 내부에서만

## 2. 이름 검색 규칙 (Name Resolution)

### LEGB Rule

- Local Scope : 함수
- Enclosed Scope : 특정 함수 상위 함수
- Global Scope : 함수 밖 변수, Import
- Built-in scope : 내장 함수



# 5. 재귀 함수

## 1. 팩토리얼

```python
a = int(input())


# 반복
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print(fact(a))


# 재귀
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


result = fact(a)
print(result)
```

### 1. 반복문

- n > 1 : 반복문 실행, n은 1씩 감소
- n = 1 : 반복문 종료

### 2. 재귀 함수

- 재귀함수 호출, n 1씩 감소
- n = 1 : 추가 함수 호출 X (base case)

- 최대 재귀 깊이 : 1000번

## 2. 피보나치

```python
a = int(input())


# 반복
def fibo(n):
    if n < 2:
        return n

    a, b = 0, 1

    for i in range(n - 1):
        a, b = b, a + b
    return b


print(fibo(a))


# 재귀
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(a))
```
