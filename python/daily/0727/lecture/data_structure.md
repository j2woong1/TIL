# Data Structure

## 1. List Comprehension

### 1. 세제곱 리스트

```python
# 반복
numbers = range(1, 11)
cublic_list = []
for i in numbers:
    cubic_list.append(i ** 3)

# list comprehension
[number ** 3 for number in numbers]
```

## 2. List Comprehension + 조건문

### 1. 짝수 리스트

```python
# 반복
even_list = []
for i in range(1,11):
    if i % 2 == 0:
        even_list.append(i)

# list comprehension
list(i for i in range(1,11) if i % 2 == 0)
```

### 2. 곱집합

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']

# 반복
pair = []
for boy in boys:
    for girl in girls:
        pair.append((boy, girl))
        
# list comprehension
list((boy, girl) for boy in boys for girl in girls)
```

### 3. 피타고라스 정리

```python
# 반복
result = []
for x in range(1, 50):
    for y in range(1, 50):
        for z in range(1, 50):
            if x ** 2 + y ** 2 == z ** 2:
                result.append((x, y, z))
                
# list comprehension
list((x, y, z) for x in range(1, 50) for y in range(1, 50) for z in range(1, 50) if x ** 2 + y ** 2 == z ** 2)
```

### 4. 모음 제거

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'

# 반복
result = []
for word in words:
    if word not in vowels:
        result.append(word)
print(''.join(result)) # Lf s t shrt, y nd pythn!
        
# list comprehension
list(word for word in words if word not in vowels)
print(''.join(result))
```



## 2. Built-in Function

### 1. 코딩 테스트

```python
a, b = map(int, input().split())
print(a + b)
```



## 3. Dictionary

### 1. 순회

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}

# A형은 40명입니다.
# B형은 11명입니다.
# AB형은 4명입니다.
# O형은 45명입니다.

# for
for blood_type in blood_types:
    print(f'{blood_type}형은 {blood_types[blood_type]}명입니다.')
    
# key
for blood_type in blood_types.keys():
    print(f'{blood_type}형은 {blood_types[blood_type]}명입니다.')
    
# items
for blood_type, number in blood_types.items():
    print(f'{blood_type}형은 {number}명입니다.')
```

```python
# 검사에 참가한 사람은 총 100명입니다.

# for, dict[key]
for blood_type in blood_types:
    total += blood_types[blood_type]
print(f'검사에 참가한 사람은 총 {total}명입니다.')
    
# values, for
total = 0
for number in blood_types.values():
    total += number
print(f'검사에 참가한 사람은 총 {total}명입니다.')

# sum
total = sum(blood_types.values())
print(f'검사에 참가한 사람은 총 {total}명입니다.')
```

### 2. 구축

```python
# {'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

# dict[key]
title_counter = {}
for title in book_title:
    if title in title_counter:
        title_counter[title] += 1
    else:
        title_counter[title] = 1
        
print(title_counter)

# count
title_counter = {}
for title in book_title:
    title_counter[title] = book_title.count(title)

print(title_counter)

# get
title_counter = {}
for title in book_title:
    title_counter[title] = title_counter.get(title, 0) + 1

print(title_counter)
```



## 4. Comprehension

```python
dusts = {'서울': 72, '인천': 82, '제주': 29, '동해': 45}

result = {key: value for key, value in dusts.items() if value > 80} # {'인천': 82}

result = {key: '나쁨' if value > 80 else '보통' for key, value in dusts.items()} # {'서울': '보통', '인천': '나쁨', '제주': '보통', '동해': '보통'}

result = {key: '매우나쁨' if value > 150 else '나쁨' if value > 80 else '보통' if value > 30 else '좋음' for key, value in dusts.items()} # {'서울': '보통', '인천': '나쁨', '제주': '좋음', '동해': '보통'}
```

