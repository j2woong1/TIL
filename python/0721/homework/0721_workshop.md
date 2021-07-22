# 1. List 합 구하기

```python
number = [1,2,3,4,5]

def list_sum(number):
    sum = 0
    for n in number:
        sum = sum + n
    return sum

print(list_sum(number))
```



# 2. Dictionary List 합 구하기





# 3. 2차원 List 전체 합 구하기

```python
n = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

def all_list_sum(n):
    sum = 0
    for i in n:
        if type(i) == list:
            sum += all_list_sum(i)
        else:
            sum += i
    return sum

print(all_list_sum(n))
```

