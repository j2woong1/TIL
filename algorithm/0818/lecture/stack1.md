# Stack	

- 자료를 쌓아 올린 -> 선형 구조

  - `c` : 배열
  - 마지막 삽입 원소 위치 : `top`

- 연산

  - 삽입 : `push`

  ```python
  def push(item):
      s.append(item)
  ```

  - 삭제 : `pop`

  ```python
  def pop():
      if len(s) == 0:
          # underflow
          return
      else:
          return s.pop(-1)
  ```

  - `isEmpty`
  - `top` `item` : `peek`

- LIFO

## 재귀 호출

- factorial

```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

![image-20210818142540159](stack1.assets/image-20210818142540159.png)

## Memoization

- 이전 계산 값 메모리에 저장

```python
# 재귀
def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
```

## Dynamic Programming

- 최적화 문제 해결
- 입력 크기 작은 문제 모두 해결 -> 큰 크기 해결

```python
# 순회 
def fibo2(n):
    f = [0, 1]
    
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
        
    return f[n]
```

## Depth First Search (깊이 우선 탐색)

- 비선형구조 그래프
- LIFO 스택 : 되돌아가서 다시 탐색

```python
visited[], stack[] 초기화
DFS(v)
	v 방문;
    visited[v] <- true;
    do {
        if (v의 인접 정점 중 방문 안한 w 찾기)
        	push(v);
        while(w) {
            w 방문;
            visited[w] <- true;
            push(w);
            v <- w;
            v의 인접 정점 중 방문 안한 w 찾기
        }
        v <- pop(stack);
    } while (v)
end DFS
```

초기 : `visited` `false`로 초기화, 공백 스택

```python
A 방문;
visited[A] <- true;
```

![image-20210818150447672](stack1.assets/image-20210818150447672.png)

```python
push(A);
B 방문;
visited[B] <- true;
```

![image-20210818150602449](stack1.assets/image-20210818150602449.png)

```python
push(B);
D 방문;
visited[D] <- true
```

![image-20210818150643203](stack1.assets/image-20210818150643203.png)

```python
push(D);
F 방문;
visited[F] <- true;
```

![image-20210818150720166](stack1.assets/image-20210818150720166.png)

```python
push(F);
E 방문;
visited[E] <- true;
```

![image-20210818150920056](stack1.assets/image-20210818150920056.png)

```python
push(E);
C 방문
visited[C] <- true;
```

![image-20210818150956876](stack1.assets/image-20210818150956876.png)

```python
pop(stack);
```

![image-20210818151048516](stack1.assets/image-20210818151048516.png)

![image-20210818151101264](stack1.assets/image-20210818151101264.png)

```python
push(F);
G 방문;
visited[G] <- true;
```

![image-20210818151135235](stack1.assets/image-20210818151135235.png)

```python
pop(stack);
```

![image-20210818151208481](stack1.assets/image-20210818151208481.png)

![image-20210818151221206](stack1.assets/image-20210818151221206.png)

![image-20210818151242587](stack1.assets/image-20210818151242587.png)

![image-20210818151255685](stack1.assets/image-20210818151255685.png)

