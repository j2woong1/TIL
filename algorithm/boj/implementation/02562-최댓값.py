# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지

nums = []
for num in range(9):
    nums.append(int(input()))

print(max(nums))
print(nums.index(max(nums))+1)

