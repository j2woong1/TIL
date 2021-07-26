# 1. Python 예약어

- False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield



# 2. 실수 비교

```python
import math
math.isclose(num1,num2)
```



# 3. 이스케이프 시퀀스

- 줄 바꿈 : \n
- 탭 : \t
- 백슬래시 : \\\



# 4. String Interpolation

```python
print('안녕, {}야'.format(name))
```



# 5. 형 변환

(5) int('3.5')



# 6. 네모 출력





# 7. 이스케이프 시퀀스 응용

```python
print('\"파일은 C:\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다.\'cd를 써서 git bash로 들어가 봐야지\'')
```



# 8. 근의 공식

```python
import math

a = int(input())
b = int(input())
c = int(input())

x1 = ((-b + (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)
x2 = ((-b - (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)

print(x1)
print(x2)
```