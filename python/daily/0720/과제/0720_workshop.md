# 1. N 약수

정수 n 약수 오름차순

```python
n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i, end = " ")
```



# 2. 중간값 찾기

```python
import statistics

numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

print(statistics.median(numbers))
```



# 3. 내려가는 계단 만들기

```python
n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
```