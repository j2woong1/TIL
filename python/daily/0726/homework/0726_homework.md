# 1. 모음 갯수

```python
# count 활용

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for vowel in vowels:
        count += word.count(vowel)
    return count

print(count_vowels('apple'))
print(count_vowels('banana'))
```



# 2. 문자열 조작

- (4) .strip([chars]) 은 특정 문자를 지정하면 , 양쪽에서 해당 문자를 찾아 제거한다 . 특정 문자를 지정하지 않으면 오류가 발생한다 -> 미 지정 시 공백 삭제

- .find(x) : x 의 첫번째 위치 반환, 없으면 1 을 반환
- .split([chars]) : 문자열을 특정 문자를 기준으로 나누어 list 로 반환, 미 지정 시 공백 기준
- .replace(old, new[, count]) : 바꿀 대상 문자를 새로운 문자로 바꿔서 반환



# 3. 정사각형 만들기

```python
# 만들 수 있는 정사각형 넓이

def only_square_area(num1, num2):
    square = []

    for i in num1:
        for j in num2:
            if i == j:
                square.append(i ** 2)
    return square


print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
```