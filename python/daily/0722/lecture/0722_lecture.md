# 1. 큰 값 반환

```python
def my_max(*args):
    result = args[0]
    for value in args:
        if value > result:
            result = value
    return result

# Same
def my_max(*args):
    result = args[0]
    for i in range(1, len(args)):
        if args[i] > result:
            result = args[i]
    return result
```



# 2. 리스트 두개 더하여 값이 큰 리스트

```python
def my_list_max(a, b):
    if sum(a) > sum(b):
        return a
    else:
        return b

def my_list_max2(*numbers):
    max = 0
    answer = 0
    for number in numbers:
        if sum(number) > max:
            max = sum(number)
            answer = number
    return answer


print(my_list_max2([10, 3], [5, 91], [10, 4], [1, 2]))
```



# 3. 원기둥 부피

```python
def cylinder(r, h):
    return r**2 * 3.14 * h

print(cylinder(5, 2)) # 157
print(cylinder(2, 5)) # 62.8
```



# 4. 기본 인자 값

```python
def greeting(name='익명'):
    return f'{name}, 안녕?'
    
greeting()
greeting('철수') # '철수, 안녕?'
-
def greeting(age, name='john'):
    return f'{name}은 {age}살입니다.'

greeting(1)
greeting(2, 'json') # 'json은 2살입니다.'
```



# 5. 키워드 인자

```python
def greeting(age, name):
    return f'{name}은 {age}살입니다.'

greeting(name='철수', age=24) # '철수은 24살입니다.'
greeting(24, name='철수') # same
```



# 6. 가변(임의) 인자 리스트

```python
def my_func(*args):
    return args
    
print(my_func(1, 2)) # (1, 2)
print(type(my_func(1, 2))) # <class 'tuple'>
```



# 7. 가변(임의) 키워드 인자

```python
hi = dict(한국어='안녕', 영어='hi')
print(hi) # {'한국어': '안녕', '영어': 'hi'}

dict([(1, 1), (2, 2)]) # {1: 1, 2: 2}
dict(((1,1), (2,2))) # same

def my_dict(**kwargs):
    return kwargs

print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')) # {'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
```

## 1. URL 생성기

```python
def my_url(**kwargs):
    url = 'https://api.go.kr?'
    print(kwargs)
    for name, value in kwargs.items():
        url += f'{name}={value}&'
    return url


print(my_url(sidoname='서울', key='asdf'))
# {'sidoname': '서울', 'key': 'asdf'}
# https://api.go.kr?sidoname=서울&key=asdf&
```



# 8. 재귀 함수

## 1. 팩토리얼

```python
# 반복
def fact(n):
    result = 1
    while n > 1:
        result *= n 
        n -= 1
    return result

# 재귀
def factorial(n):
    if n == 1: # n이 1일 때
        return 1 # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n-1) # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
```

## 2. 피보나치

```python
# 재귀
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
# 반복
def fib_loop(n):
    if n < 2:
        return n
    
    result = [0, 1]
    for i in range(2, n+1): # list에 0의 값이 포함되어 있기 때문에 자리를 차지해서 +1만큼 계산을 더함.
        result.append(result[i-1] + result[i-2])
        # result.append(result[len(result)-1] + result[len(result)-2])
    return result[-1]

def fib_loop_2(n):
    if n < 2: 
        return n
    
    a, b = 0, 1
    # 우리가 0번째 값 a 와 첫 번째 값 b 를 계속 반복하면서 원하는 값을 만들텐데, 
    # n 이 2일 때는 단 한 번(n-1)만 계산하면 원하는 값을 만들 수 있기 때문
    for i in range(n-1):
        a, b = b, a+b # 새로 만든 b 에 이전의 a, b 값을 더해 새로운 피보나치 값을 만들어 나간다.
    return b

# while
def fib_while(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    return b
    
fib_while(30)
```

