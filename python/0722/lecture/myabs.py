# 파이썬 내장 함수 abs()를 직접 구현한 my_abs()를 작성하시오.

def my_abs(x):
    # 1. 복소수이면,
    if type(x) == complex:
        # if type(x) is complex:
        return (x.imag ** 2 + x.real ** 2) ** (1 / 2)
    # 2. 복소수가 아니면,
    else:
        if x == 0:
            return x ** 2
        if x < 0:
            return x * -1
        else:
            return x


print(my_abs(3 + 4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))
