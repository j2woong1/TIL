# 가장 큰 수와 가장 작은 수의 차이를 출력

def get_max(num):
    my_max = num[0]
    for i in range(1, len(num)):
        if my_max < num[i]:
            my_max = num[i]
    return my_max


def get_min(num):
    my_min = num[0]
    for i in range(1, len(num)):
        if my_min > num[i]:
            my_min = num[i]
    return my_min


t = int(input())
for t in range(1, t + 1):
    n = int(input())
    num = list(map(int, input().split()))
    ans = get_max(num) - get_min(num)
    print(f'#{t} {ans}')
