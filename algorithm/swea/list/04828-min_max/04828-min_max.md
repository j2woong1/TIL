# 4828. Min Max

> https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg#
>
> N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
>
>
> **[입력]**
>
> 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
>
> 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
>
> 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
>
> 3 
>
> 5 
>
> 477162 658880 751280 927930 297191 
>
> 5 
>
> 565469 851600 460874 148692 111090 
>
> 10 
>
> 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
>
> **[출력]**
>
> 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
>
> #1 630739 
>
> #2 740510 
>
> #3 838110

- 풀이

```python
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
```

- 다른 풀이 1

```python
T = int(input())
for tc in range(T):
    N = int(input())
    a_i = list(map(int, input().split()))
    max_a = a_i[0]
    min_a = a_i[0]
    for i in range(len(a_i)):
        if a_i[i] > max_a:
            max_a = a_i[i]
        elif a_i[i] < min_a:
            min_a = a_i[i]
    a_dif = max_a - min_a
    print(f'#{tc+1} {a_dif}')
```

- 다른 풀이 2

```python
T = int(input())
 
for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = 0
    min_num = 1000001
 
    for j in range(N):
        if numbers[j] < min_num:
            min_num = numbers[j]
 
    for k in range(N):
        if numbers[k] > max_num:
            max_num = numbers[k]
     
    print(f'#{i+1} {max_num-min_num}')
```

