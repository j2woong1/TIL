"""
# Flatten
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 : 평탄화
가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내
상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프

총 10개의 테스트 케이스 : 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값

# 부호와 함께 테스트 케이스의 번호를 출력, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력
"""


def get_min_max(nums):
    max_num = nums[0]
    min_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num


def get_ans(dumps, flat):
    # 덤프 횟수만큼 평탄화 진행
    for dump in range(dumps):
        max_num, min_num = get_min_max(flat)
        flat[flat.index(max_num)] -= 1
        flat[flat.index(min_num)] += 1
    # 최종적으로 평탄화 된 것에서 최소, 최대값 구하기
    max_height, min_height = get_min_max(flat)
    return max_height - min_height


t = 10
for tc in range(1, t + 1):
    dump_num = int(input())
    height = list(map(int, input().split()))
    ans = get_ans(dump_num, height)
    print(f'#{tc} {ans}')
