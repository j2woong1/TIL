# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    a = "0123456789" # 십진법 기본 수
    b, c = divmod(n, 2) # n을 2로 나눈 몫

    if b == 0: # 몫이 1, 0이 될 때까지 반복
        return a[c]
    else:
        return dec_to_bin(b) + a[c]

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010