# SW Expert Academy 6249
# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

# 횟수를 저장하는 리스트 생성
array = [0] * 10
num = int(input())
result = ""
# num 0이 될때까지 반복하며 숫자체크
while num:
    array[num % 10] += 1
    num //= 10
# 0~9까지 출력하기
for i in range(0, 10):
    result += "%d " % i
print(result[0:len(result) - 1])
# 변수 초기화
result = ""
# 나온횟수 출력하기
for i in range(0, 10):
    result += "%d " % array[i]
print(result[0:len(result) - 1])
