## Stack

### 계산기

- 문자열 계산식
  - `A * B - C / D`
  - `(6 + 5 * (2- 8) / 2)`

1. 중위표기법 수식 -> 후위표기법으로
   1. 방법 1
      - 우선 순위에 따라 괄호를 사용하여 다시 표현 : `( (A * B) - (C / D))`
      - 각 연산자를 대응하는 오른쪽 괄호 뒤로 이동 : `( (A B) * (C D) /) -`
      - 괄호 제거 : `AB*CD/-`
   2. `stack`
      - 토큰을 읽음
      - 토큰이 피연산자이면 토큰 출력
      - 토슨이 연산자이면
        - 우선순위가 높으면 `stack`에 push
        - 안높으면 연산자 우선순위가 토큰 우선순위보다 작을 때까지 `stack`에서 pop, 토큰 연산자 push
        - `top`에 연산자 없으면 push
      - 오른쪽 괄호 `)`면 
        - `stack` `top`에 왼쪽 괄호 `(`가 올 때까지 `stack` pop 수행
        - pop한 연산자 출력
        - 왼쪽 괄호 만나면 pop만
      - `stack`에 남아 있는 연산자 모두 pop 후 출력
        - `stack` 밖 왼쪽 괄호 : 우선순위 가장 높음
        - `stack` 안 왼쪽 괄호 : 우선순위 가장 낮음
2. 후기표기법 수식 -> `stack`으로 계산

![image-20210824103523540](stack2.assets/image-20210824103523540.png)

![image-20210824103616682](stack2.assets/image-20210824103616682.png)

![image-20210824103640061](stack2.assets/image-20210824103640061.png)

![image-20210824103732569](stack2.assets/image-20210824103732569.png)

![image-20210824103758473](stack2.assets/image-20210824103758473.png)

![image-20210824103814190](stack2.assets/image-20210824103814190.png)

![image-20210824103828703](stack2.assets/image-20210824103828703.png)

![image-20210824103839379](stack2.assets/image-20210824103839379.png)

![image-20210824103849993](stack2.assets/image-20210824103849993.png)

![image-20210824103900553](stack2.assets/image-20210824103900553.png)

![image-20210824103911230](stack2.assets/image-20210824103911230.png)

![image-20210824103922922](stack2.assets/image-20210824103922922.png)

![image-20210824103934016](stack2.assets/image-20210824103934016.png)

![image-20210824103945177](stack2.assets/image-20210824103945177.png)

![image-20210824103955482](stack2.assets/image-20210824103955482.png)

- 거꾸로

![image-20210824104501553](stack2.assets/image-20210824104501553.png)

![image-20210824104512039](stack2.assets/image-20210824104512039.png)

![image-20210824104521716](stack2.assets/image-20210824104521716.png)

![image-20210824104536738](stack2.assets/image-20210824104536738.png)

![image-20210824104546104](stack2.assets/image-20210824104546104.png)

![image-20210824104556417](stack2.assets/image-20210824104556417.png)

![image-20210824104608323](stack2.assets/image-20210824104608323.png)

- `eval`
  - 문자열 수식 계산

### 백트래킹

- 해를 찾는 도중에 해가 아니면 되돌아가서 다시 해를 찾는 기법
- `최적화 (optimization)`, `결정 (decision)` (문제 조건 만족해가 존재 여부 -> yes, no) 
- 유망성 점검 (Promising) -> Backtracking, Pruning (가지치기, 유망하지 않는 경로 -> 고려 X)

1. 상태 공간 Tree DFS
2. Promising
3. Backtracking

#### 미로 찾기

![image-20210824104951792](stack2.assets/image-20210824104951792.png)

![image-20210824105012819](stack2.assets/image-20210824105012819.png)

- `stack`으로 경로 역으로 돌아감

![image-20210824105051960](stack2.assets/image-20210824105051960.png)

- `stack`으로 다시 경로 찾음

![image-20210824105116839](stack2.assets/image-20210824105116839.png)

#### DFS와의 차이

|                           백트래킹                           |                  DFS                  |
| :----------------------------------------------------------: | :-----------------------------------: |
| 경로가 해결책으로 이어지지 않으면<br />경로 따라가지 않아서 시도 횟수 줄임 |            모든 경로 추적             |
|                     가지치기 (Prunning)                      | N! 가지 경우의 수<br />-> 처리 불가능 |
|                   불필요한 경로 조기 차단                    |            모든 후보 검사             |
| N! 가지 경우의 수<br />-> 경우의 수 감소, 최악 : 지수함수 시간 => 처리 불가능 |                                       |

#### N-Queen

- n * n 정사각형 안에 n개 queen 배치
- 모든 queen : 일직선, 대각선에 아무것도 X

```pseudocode
def checknode(v): # node
    if promising(v):
    if there is a solution at v:
    	write the solution
    else:
    	for u in each child of v:
    		checknode(u)
```

![image-20210824105849259](stack2.assets/image-20210824105849259.png)

![image-20210824105916358](stack2.assets/image-20210824105916358.png)

#### 부분집합 구하기

- powerset : 어떤 집합의 공집합, 자기 자신을 포함한 모든 부분집합
- 원소 개수 n개 -> 개수 : 2^n
- True, False 값을 가지는 항목들로 구성된 n개 list
- `list[i]` : i번째 원소가 부분집합의 값인지 아닌지

```pseudocode
# 부분집합 포함인지 확인, 생성
bit = [0, 0, 0, 0]
for i in range(2):
	bit[0] = i  # 0번째 원소
	for j in range(2):
		bit[1] = j  # 1번째 원소
			for k in range(2):
				bit[2] = k  # 2번째 원소
				for l in range(2):
					bit[3] = l  # 3번째 원소
					print(bit)
```

![image-20210824111347096](stack2.assets/image-20210824111347096.png)

```pseudocode
# powerset 
def backtrack(a, k, input):
	global MAXCANDIDATES
	c = [0] * MAXCANDIDATES
	
	if k == input:
		process_solution(a, k)  # 답이면 원하는 작업
	else:
		k += 1
		ncandidates = contruct_candidates(a, k, input, c)
		for i in range(ncandidates):
			a[k] = c[i]
			backtrack(a, k, input)
			
def contruct_candidates(a, k, input, c):
	c[0] = True
	c[1] = False
	return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3)
```

#### 순열

```pseudocode
# {1, 2, 3}을 포함하는 모든 순열 생성
for i1 in range(1, 4):
	for i2 in range(1, 4):
		if i2 != i1:
			for i3 in range(1, 4):
				if i3 != i1 and i3 != i2:
					print(i1, i2, i3)
```

```pseudocode
def backtrack(a, k, input):
	global MAXCANDIDATES
	c = [0] * MAXCANDIDATES
	
	if k == input:
		for i in range(1, k + 1):
			print(a[i], end="")
		print()
	else:
		k += 1
		ncandidates = contruct_candidates(a, k, input, c)
		for i in range(ncandidates):
			a[k] = c[i]
			backtrack(a, k, input)
			
def contruct_candidates(a, k, input, c):
	in_perm = [False] * NMAX
	
	for i in range(1, k):
		in_perm[a[i]] = True
		
	ncandidates = 0
	for i in range(1, input + 1):
		if in_perm[i] == False:
			c[ncandidates] = i
			ncandidates += 1
	return ncandidates
```

![image-20210824112248569](stack2.assets/image-20210824112248569.png)

### 분할정복

- 분할 (Divide) : 여러개 작은 부분으로
- 정복 (Conquer) : 각각 해결
- 통합 (Combine)

#### 거듭 제곱

- `O(n)`

```pseudocode
def Power(Base, Exponent):
	if Base == 0:
		return 1
	result = 1  # Base^0은 1
	for i in range(Exponent):
		result *= Base
	return result
```

- `O(long 2n)`

```pseudocode
def Power(Base, Exponent):
	if Exponent == 0 or Base == 0:
		return 1
	if Exponent % 2 == 0:
		NewBase = Power(Base, Exponent / 2)
		return NewBase * NewBase
	else:
		NewBase = Power(Base, (Exponent - 1) / 2)
		return (NewBase * NewBase) * Base
```

#### 퀵, 합병 정렬 비교

​	![image-20210824131803150](stack2.assets/image-20210824131803150.png)

```pseudocode
# 퀵 정렬
def quickSort(a, begin, end):
	if begin < end:
		p = partition(a, begin, end)
		quickSort(a, begin, p - 1)
		quickSort(a, p + 1, end)
		
def partition(a, begin, end):
	pivot = (begin + end) // 2
	L = begin
	R = end
	while L < R:
		while(a[L] < a[pivot] and L < R):
			L += 1
		while(a[R] >= a[pivot] and L < R):
			R -= 1
		if L < R:
			if L == pivot:
				pivot = R
			a[L], a[R] = a[R], a[L]
	a[pivot], a[R] = a[R], a[pivot]
	return R
```

- 2를 피봇으로 선택, 퀵 정렬

  ![image-20210824132227118](stack2.assets/image-20210824132227118.png)

  - L 오른쪽 이동 : 크거나 같은 원소, R 왼쪽 이동 : 작은 원소
  - L : 69, R : 피봇보다 작은 원소 X -> 69에서 만남
  - 69를 피봇과 교환

  ![image-20210824132552861](stack2.assets/image-20210824132552861.png)

- 오른쪽 부분 퀵 정렬 : 16 피봇 선택

  - L 30, R 8 교환

  ![image-20210824132824114](stack2.assets/image-20210824132824114.png)

  - 69 피봇 교환

  ![image-20210824141325238](stack2.assets/image-20210824141325238.png)

- 피봇 왼쪽 부분 집합에서 10 피봇

  - ![image-20210824141430759](stack2.assets/image-20210824141430759.png)

- 30 피봇

  - ![image-20210824141530706](stack2.assets/image-20210824141530706.png)
  - ![image-20210824141602930](stack2.assets/image-20210824141602930.png)

- 31 피봇

  - ![image-20210824141634801](stack2.assets/image-20210824141634801.png)

- 최악 : `O(n^2)`, 평균 : `O(nlogn)`

