# 1. N 약수

```python
#1. 내장함수 쓰지 않고 구하기
numbers = [6, 1, 8, 2, 5, 4]

length = 0
for _ in numbers:
    length += 1

center_index = length // 2
sorted_nums = sorted(numbers)
print(sorted_nums[center_index])

# 홀수면
if length % 2:
    # 바로 중앙값 출력하고
    print(sorted_nums[center_index])
# 짝수면
else:
    # 짝수면 가운데 두 값 구해서 평균 
    avg = sum(sorted_nums[center_index-1:center_index+1]) / 2
    print(avg)
```

