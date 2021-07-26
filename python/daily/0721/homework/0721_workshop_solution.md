# 2. Dictionary List 합 구하기

```python
dict_list_sum([{'name' : 'kim', 'age' : 12},
               {'name' : 'lee', 'age' : 4}])

def dict_list_sum(infos):
		age_sum = 0
		for info in infos:
				age_sum += info['age']
		return age_sum
```



# 3. 2차원 List 전체 합 구하기

```python
all_list_sum([1], [2, 3], [4, 5, 6], [7, 8, 9, 10])

def all_list_sum(num_lists):
		lists_sum = 0
		for num_list in num_lists:
				for num in num_list:
						lists_sum += num
		return lists_sum
```

