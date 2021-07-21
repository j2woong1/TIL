N = int(input())  # 입력받기
a = 0  # 배수계산을 위한 변수
t = 0  # 합을 계산하기 위한 변수

for i in range(1, 5):  # 1부터 4까지 반복
    a = a * 10 + 1  # 1, 11, 111, 1111 만듦
    t += N * a  # a + aa+ aaa+ aaaa 를 한다.

print(t)  # 결과값 출력
