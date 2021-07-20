# 1. Mutable & Immutable Container

- Mutable : List, Set, Dictionary
- Immutable : String, Tuple, Range + Int, Float, Bool



# 2. 홀수만 담기

1~50까지 숫자 by using range, slicing

```python
numbers = list(range(1,51))
lst = numbers[0::2]

print(lst)
```



# 3. Dictionary

key : 이름, value : 나이

```python
classroom = {
    "A" : 29, "B" : 27, "C" : 24,
    "D" : 26, "E" : 29, "F" : 27
}
print(classroom)
```



# 4. 네모 출력

반복문

```python
n = 5
m = 9

for i in range(n):
    for j in range(m):
        print("*",end="")
    print()
```



# 5. 조건 표현식

```python
'입실 불가' if temp >= 37.5 else '입실 가능'
```



# 6. 평균 구하기

```python
mean = sum(scores) / len(scores)
print(mean)
```

