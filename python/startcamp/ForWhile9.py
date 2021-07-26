# SW Expert Academy 6247
# while 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

i, k = 7, 0
while i >= 0:
    print("{0}{1}".format((" " * k), ("*" * i)))
    i -= 2
    k += 1
