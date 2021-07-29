# 1. Circle 인스턴스 만들기

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumstance(self):
        return 2 * self.pi * self.r

    def center(self):
        return self.x, self.y

cir = Circle(3, 2, 4)
print(cir.area())  # 28.259999999999998
print(cir.circumstance()) # 18.84
```



# 2. Dog와 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('멍멍이')
dog.walk()  # 멍멍이! 달린다!
dog.bark()  # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk()  # 구구! 걷는다!
bird.eat()  # 구구! 먹는다!
bird.fly()  # 구구! 푸드덕!
```



# 3. 오류의 종류

- `ZeroDivisionError` 0으로 나누었을 때

- `NameError` 정의된 변수가 없을 때

- `TypeError` 타입이 맞지 않을 때

- `IndexError` 인덱스 범위를 벗어났을 때

- `KeyError` 키가 존재하지 않을 때

- `ModuleNotFoundError` 해당 모듈을 찾지 못했을 때

- `ImportError` 임포트를 했을때 오류가 발생했을 때