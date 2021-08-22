# 1213. String

> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE&problemTitle=string&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
>
> 주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.
>
> Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.
>
> 위 문장에서 ti 를 검색하면, 답은 4이다.
>
> **[제약 사항]**
>
> 총 10개의 테스트 케이스가 주어진다.
>
> 문장의 길이는 1000자를 넘어가지 않는다.
>
> 한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.
>
> 한 문장에서는 하나의 문자열만 검색한다. 
>
> **[입력]**
>
> 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.
>
> 1
> ti
> Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasics ...
> 2
> ing
> Thedoublehelixformsthestructuralbasisofsemi-conservativeDNAreplication.1,2Less ...
> ...
>
> **[출력]**
>
> \#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
>
> \#1 4
> \#2 2
> ...

- 풀이

```python
T = int(input())

for tc in range(1, T + 1):
    order = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    n = input()
    arr = input().split()

    for i in arr:
        order[i] += 1
    ans = ''

    for key, value in order.items():
        tmp = ' '.join([key] * value)
        ans += tmp + ' '  # zro 다음 one 을 출력할 때 띄어쓰기

    print(f"#{tc}")
    print(ans[:len(ans) - 1])  # 마지막에 띄어쓰기가 포함되어 있으므로 삭제
```

