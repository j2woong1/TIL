# 1. Built-in 함수, 메서드

```python
import random
lotto = random.sample(range(1, 46), 6)

result = lotto.sort()
print(lotto, result) # result에 None
print(lotto, sorted(lotto)) # 처음 출력한 lotto를 순서에 맞게 정렬
```



# 2. .extend(), .append()

```python
# append : 값 추가
# extend : iterable 값 추가

cafe = ['starbucks', 'tomntoms', 'hollys']

cafe.append('banapresso') # ['starbucks', 'tomntoms', 'hollys', 'banapresso']

cafe.extend(['wcafe', '빽다방']) # ['starbucks', 'tomntoms', 'hollys', 'wcafe', '빽다방']

cafe.extend('ediya') # ['starbucks', 'tomntoms', 'hollys', 'e', 'd', 'i', 'y', 'a']
```



# 3. 복사

```python
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a) # [1, 2, 5, 4, 5]
print(b) # [1, 2, 5, 4, 5]
```

