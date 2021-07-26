# 1. 세로 출력

```python
num = int(input())

for i in range(num):
    print(i+1)
```



# 2. 거꾸로 세로 출력

```python
n = int(input())

for i in range(n, -1, -1):
    print(n)
    n -= 1
```



# 3. N줄 덧셈

```python
n = int(input())
sum = 0

for i in range(1,n+1):
    sum += i

print(sum)
```

