# 1. Built-In 함수

```python
dir(__builtins__)
```



# 2. 정중앙 문자

```python
get_middle_char('ssafy') #=> a
get_middle_char('coding') #=> di

def get_middle_char(word):
    num = len(word) // 2
	
    if len(word) % 2:
        middle = word[num]
    else:
        middle = word[num-1:num+1]
    
    return middle
```



# 5. 가변 인자 리스트

```python
# 1
def my_avg(*args):
    return sum(args) / len(args)

# 2
def my_avg(*args):
    count = 0
    for num in args:
        count += num
    avg = count / len(args)
    return avg
```

