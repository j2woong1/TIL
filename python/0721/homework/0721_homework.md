# 1. Built-In 함수

- abs, all, any, ascii, bin



# 2. 정중앙 문자

```python
str1 = input()
str2 = input()

def get_middle_char(str):
    mid = len(str) // 2
    return str[mid] if len(str) % 2 else str[mid - 1 : mid +1]

print(get_middle_char(str1))
print(get_middle_char(str2))
```



# 3. 위치 인자, 키워드 인자

- (4)

  ```python
  ssaft(name = '길동', '구미')
  ```



# 4. 반환값

- 10



# 5. 가변 인자 리스트

```python
lst = list(map(int, input().split()))

def my_avg(lst):
    return (sum(lst) / len(lst))

print(my_avg(lst))
```

