# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력

grade = int(input())

if 90 <= grade <= 100:
    print('A')
elif 80 <= grade:
    print('B')
elif 70 <= grade:
    print('C')
elif 60 <= grade:
    print('D')
else:
    print('F')