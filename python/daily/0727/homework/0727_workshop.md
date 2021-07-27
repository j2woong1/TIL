# 1. 중복

```python
# 중복 문자 list

def duplicated_letters(word):
    duplicates = []

    for c in word:
        if (word.count(c) > 1) and (c not in duplicates):
            duplicates.append(c)

    return duplicates


print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
```



# 2. 소대소대

```python
# 소문자, 대문자 번갈아서

def low_and_up(word):
    new = ''
    for i in range(len(word)):
        if not i % 2:
            new += word[i]
        else:
            new += word[i].upper()

    return new


print(low_and_up('apple'))  
print(low_and_up('banana'))
```



# 3. 숫자의 의미

```python
# 0~9 list -> 연속 숫자 제거, 기존 순서 유지

def lonely(nums):
    result = []

    for i, num in enumerate(nums):
        if i == 0:
            result.append(num)
        if result[-1] != num:
            result.append(num)
    return result


print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
```

