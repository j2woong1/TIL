[TOC]



# Python

## 데이터 타입

- 숫자
  - int (정수)
    - 2진수 : 0b
    - 8진수 : 0o
    - 16진수 : 0x
  - float (부동소수점, 실수)
  - complex (복소수)
    - 허수부 : j
  
- 문자열 (String)
  - 이스케이프 시퀀스
  
  - String Interpolation
    - `%-formatting`
      - `%d` : 정수
      - `%f` : 실수
      - `%s` : 문자열
    
    ```python
    print('Hello, %s' % name)
    print('내 성적은 %d' % score)
    print('내 성적은 %f' % score)
    
    """
    Hello, 정지웅
    내 성적은 4
    내 성적은 4.300000
    """
    ```
    
    - `str.format`
    
    ```python
    print('Hello, {}! 성적은 {}'.format(name, score))
    
    """
    Hello, 정지웅! 성적은 4.3
    """
    ```
    
    - `f-strings`
    
    ```python
    print(f'Hello, {name}! 성적은 {score}')
    
    """
    Hello, 정지웅! 성적은 4.3
    """
    ```
    
    ```python
    import datetime
    today = datetime.datetime.now()
    print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
    
    """
    오늘은 21년 08월 08일 Sunday
    """
    ```
    
    
  
- 참/거짓 (Boolean)

  - True, False

- None



## 컨테이너

- 여러 개 값 저장 (객체)

### 시퀀스형

- 순서 O : ordered -> 정렬
- list, tuple, range, string, binary

#### List

- []

#### Tuple

- immutable
- (), ,

#### Range

- `range(n)` : 0부터 n-1까지
- `range(n, m)` : n부터 m-1까지
- `range(n, m, s)` : n부터 m-1까지 s만큼 증가

#### 연산자/함수

- in, not in
- `+` (concatenation) : range는 TypeError
- `*` (반복) : range는 TypeError
- indexing : 인덱스 없으면 IndexError
- slicing : `[n:m:s]` n부터 m-1까지 s만큼 증가
- 길이 : len
- min, max : 문자열은 ASCII 코드
- count

### 비시퀀스형

- unordered
- set, dictionary

#### Set

- {} : 빈 세트 -> set()
- 집합, 중복 X
- `-` : 차집합 / `\` : 합집합 / `&` : 교집합

```python
my_list = ['서울', ' 서울', '대전', '광주'
          '서울', '대전', '부산', '부산']
len(set(my_list)) # 개수

"""
4
"""

set(my_list) # random하게 출력
```

#### Dictionary

- 'key': 'value'
- {}
- key : immutable -> string, integer, float, boolean, tuple, range
- value : 모든 값



## 제어문

### 조건문

- if 
- 조건 표현식

```python
<true> if <expression> else <false>
```

### 반복문

#### while

- 종료 조건

```python
n = 0
total = 0
user_input = int(input())

while n <= user_input:
	total += n
	n += 1 
print(total) # 1부터 n까지 총합
```

#### for

- 모두 순회하면 종료 : iterable (string, tuple, list, range)

```python
chars = input()

for char in chars:
	print(char) # input 한 글자씩 출력
```

```python
for i in range(1, 31):
	if i % 2:
		print(i) # 1부터 30까지 홀수
```

- 리스트 순회

```python
members = ['민수', '영희', '철수']

for i in range(len(members))
	print(f'{i+1}번 {members[i]}')
    
"""
1번 민수
2번 영희
3번 철수
"""
    
for idx, member in enumerate(members):
    print(idx, member)
    
"""
0 민수
1 영희
2 철수
"""
```

#### 반복 제어

- break : 종료
- continue : 이후 코드 수행 X, 다음 반복 수행
- for-else : 끝까지 실행 후 else 실행
- pass : 아무것도 X



## 함수

```python
def cube(num):
    cubed = num ** 3
    return cubed # 세 제곱
```

### Output

#### Return

- 하나의 객체
- 복수 return : 하나의 tuple
- 명시적 return 값 X : Nonetype

```python
def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return (area, perimeter) # 사각형 넓이, 둘레
```

### Input

- 위치 인자 (Positional Argument)

```python
def add(x, y):
    # x = 2; y = 3
    return x + y    
add(2, 3)
```

- 기본 인자 값 (Default Arguments Values)

```python
def add(x, y=0):
    # x = 2
    return x + y    
add(2)

def add(x=0, y) # 이건 안됨 : non-default argument follows default argument
```

- 키워드 인자 (Keyword Arguments)

```python
def add(x, y):
    return x + y 
add(x=2, y=5)
add(2, y=5)
add(x=2, 5) # 이건 안됨 : positional argument follows keyword argument
```

- 가변 인자 리스트 (Arbitray Argument Lists) : tuple

```python
def my_max(*args):
    result = args[0]
    for i in range(1, len(args)):
        if args[i] > result:
            result = args[i]
    return result
```

- 가변 키워드 인자 (Arbitrary Keyword Arguments) : dictionary

```python
def my_url(**kwargs):
    url = 'https://api.go.kr?'
    print(kwargs)
    for name, value in kwargs.items():
        url += f'{name}={value}&'
    return url
print(my_url(sidoname='서울', key='asdf'))

"""
https://api.go.kr?sidoname=서울&key=asdf&
"""
```

## 함수 Scope

- 전역 스코프(`global scope`) : 코드 어디에서든 참조할 수 있는 공간
- 지역 스코프(`local scope`) : 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간

- 전역 변수(`global variable`) : 전역 스코프에 정의된 변수
- 지역 변수(`local variable`) : 로컬 스코프에 정의된 변수

#### 이름 검색 규칙

- LEGB Rule
  - Local Scope : 함수
  - Enclosed scope : 특정 함수 상위 함수
  - Global Scope : 함수 밖 변수, import
  - Built-In Scope : 내장 함수, 속성

#### Global

```python
a = 10
def func1():
    global a
    a = 3

print(a) # 10
print(func1()) # 3
```

#### Nonlocal

```python
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    print(func2(x)) # 2
print(func1(x)) # 0
```



## 재귀 함수

```python
# 반복
def fact(n):
    result = 1
    while n > 1:
        result *= n 
        n -= 1
    return result

"""
n > 1: 반복문, n 1씩 감소
n = 1: 반복문 X
"""

# 재귀
def factorial(n):
    if n == 1: # n이 1일 때
        return 1 # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n-1) # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함

"""
재귀 함수 호출, n 1씩 감소
n = 1: 함수 호출 X
"""
```

```python
# 반복
def fib_loop(n):
    if n < 2:
        return n
    
    result = [0, 1]
    for i in range(2, n+1): # list에 0의 값이 포함되어 있기 때문에 자리를 차지해서 +1만큼 계산을 더함.
        result.append(result[i-1] + result[i-2])
        # result.append(result[len(result)-1] + result[len(result)-2])
    return result[-1] # list 의 마지막 값 출력

def fib_loop_2(n):
    if n < 2: 
        return n
    
    a, b = 0, 1
    # 우리가 0번째 값 a 와 첫 번째 값 b 를 계속 반복하면서 원하는 값을 만들텐데, 
    # n 이 2일 때는 단 한 번(n-1)만 계산하면 원하는 값을 만들 수 있기 때문
    for i in range(n-1):
        a, b = b, a+b # 새로 만든 b 에 이전의 a, b 값을 더해 새로운 피보나치 값을 만들어 나간다.
    return b

# 재귀 
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```

- 재귀 : 입력 값이 커질수록 속도 느림
- 반복 : 속도 빠름



## Error/Exception Handling

### Error

#### Syntax Error

- invalid syntax : `:` 안찍음
- cannot assign to literal
- EOL (End of Line) while scanning string literal : `'` 마무리 덜 됨
- unexpected EOF (End of File) while parsing : `)` 안찍음

### Exception

- ZeroDivisionError
- NameError : not defined
- TypeError : type 불일치, argument 누락, 초과, 불일치
- ValueError : 값 적절 X
- IndexError : index X, 범위 out
- KeyError : key X
- ModuleNotFoundError
- ImportError
- KeyboardInterrupt : 임의로 종료
- IndentationError

### Exception Handling

- try (statement), except (clause)
- 예외 O : except, X : except 없이 종료
- try : 코드 실행
- except : try 문에서 예외 발생 시 실행
- else : try 문에서 예외 발생하지 않으면 실행
- finally : 예외 발생 여부와 관계 없이 항상 실행

### Exception 발생

- raise
- assert



## 데이터 구조

- 순서 O : String, List
- 순서 X : Set, Dictionary

### String

- 문자 나열
- Immutable (변경 X)
- Ordered (순서 O)
- Iterable (순회 O)

#### slicing 

- `s[start:stop:step]`
  - `s[::]` : 그냥 그대로, same with `s[0:len(s):1]`
  - `s[::-1]` : 거꾸로, same with `s[-1:-len(s)+1:-1]`

#### 조회/탐색

- find : 첫 번째 위치, 없으면 -1
- index : 첫 번째 위치, 없으면 ValueError

#### 변경

- replace : 바꿀 글자 새로운 글자로, count
- strip : 제거, 지정 안하면 공백 제거
- split : 특정한 단위로 나눠서 리스트로 반환
- separator.join : Iterable 요소를 separator로 합쳐서 문자열 반환
- capitalize
- title : `'`나 공백 이후 대문자
- upper
- lower
- swapcase

#### 검증

- isalpha
- isupper
- islower
- istitle

### List

- 순서 O, 인덱스
- Mutable
- Ordered
- Iterable

#### 추가 및 삭제

- append : 추가
- extend : Iterable 항목 추가
- insert : 정해진 위치 i에 값 추가
- remove : 삭제
- pop : 정해진 위치 i 삭제 -> 반환, 지정 X -> 마지막 항목 삭제 -> 반환
- clear

#### 탐색 및 정렬

- index : 해당 index
- count 
- sort : 정렬, 원본 변경
  - sorted : 원본 변경 X
- reverse : 순서 반대로

#### 복사

##### Shallow Copy

- Slice 연산자

```python
a = [1, 2, 3]
b = a[:]
print(a, b)
b[0] = 5
print(a, b)

"""
[1, 2, 3] [1, 2, 3]
[1, 2, 3] [5, 2, 3]
"""
```

- list()

```python
a = [1, 2, 3]
b = list(a)
print(a, b)
b[0] = 5
print(a, b)

"""
[1, 2, 3] [1, 2, 3]
[1, 2, 3] [5, 2, 3]
"""
```

- 주소 참조

```python
a = [1, 2, ['a', 'b']]
b = a[:]
print(a, b)
b[2][0] = 0
print(a, b)

"""
[1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
[1, 2, [0, 'b']] [1, 2, [0, 'b']]
"""
```

##### Deep Copy

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b)
b[2][0] = 0
print(a, b)

"""
[1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
[1, 2, ['a', 'b']] [1, 2, [0, 'b']]
"""
```

#### List Comprehension

- [<expression> for <변수> in <iterable>]
- [<expression> for <변수> in <iterable> if <조건식>]

```python
cubic_list = [x ** 3 for x in numbers] # 세 제곱
```

```python
even_list = [x for x in range(1, 11) if x % 2 == 0] # 1부터 10까지 짝수만
```

#### Built-In Function

##### Map

- Iterable 요소 -> map object

```python
numbers = [1, 2, 3]
result = map(str, numbers)
list(result) # ['1', '2', '3']
```

##### Filter

- Iterable 요소 -> True인 것 : filter object

```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
list(result) # [1, 3]
```

##### Zip

- 복수 Iterable -> tuple 원소 zip object

```python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
list(pair) # [('jane', 'justin'), ('ashley', 'eric')]
```

### Set

- 중복, 순서 X
- Mutable
- Unordered
- Iterable

#### 함수

- add 
- update : 여러 값 추가
- remove : 삭제, 없으면 KeyError
- discard : 삭제, 없어도 에러 X
- pop : 랜덤 제거

### Dictionary

- key, value
- Mutable
- Unordered
- Iterable

#### 함수

- get : key로 value, KeyError X, default 설정 O
- pop : key 있으면 제거, 없으면 Default, Default 없으면 KeyError
- update
- keys(), values(), items()

#### Dictionary Comprehension

- {key: value for <변수> in <iterable>}
- {key: value for <변수> in <iterable> if <조건식>}

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45}
result = {}
for key, value in dusts.items():
    if value > 70:
        result[key] = value
print(result) # {'서울': 72, '대전': 82}

{key: value for key, value in dusts.items() if value > 70}  
# {'서울': 72, '대전': 82}
```



## Module

### Module, Package

```python
def odd(n):
    return bool(n % 2)

def even(n):
    return not bool(n % 2)

import check
check.odd(3)
check.even(3)
```



## OOP

### 객체

- 특정 타입의 instance
- type : operator, method
  - is
  - isinstance : True, TypeError
- attribute : data
- method : function

### Object-Oriented Programming

- 정보 : 속성 (Attribute)
- 행동 : 메서드 (Method)
- 클래스 정의 -> 인스턴스 생성 -> 메서드 호출 -> 속성
- 클래스 : 객체 분류
- 인스턴스 : 예시
- 속성 : 상태/데이터
- 메서드 : 행위(함수)
- self : 인스턴스 자기자신

#### 매직 메서드

- 특수 동작
- `__str__` : 출력 형태 지정
- `__gt__` : greater than

### Class / Instance

#### Instance 변수

- 인스턴스 속성
- 고유 변수
  - 메서드에서 self.<name>으로 정의
  - 인스턴스 생성 이후 <instance>, <name>으로 접근, 할당

#### Class 변수

- 클래스 속성 (Attribute)
- 모든 인스턴스 공유
- <classname>, <name>

#### 메서드

- 인스턴스 메서드
  - 클래스 내부
  - 호출 : self
- 클래스 메서드
  - @classmethod
  - 호출 : cls
- 스태틱 메서드
  - @staticmethod
  - 호출 : 전달 X, 접근,수정 X

#### 상속

- super() : 자식 클래스에서 부모 클래스 사용
- method overriding : 상속 method 재정의

