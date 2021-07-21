# SW Expert Academy 6226
# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아 콤마(,)로 구분된 문자열

result = ""
for i in range(1, 201):  # 1부터 200까지 반복
    if not (i % 7) and (i % 5):  # 7로 나누었을때 나머지가 0이고 그리고 5로 나누었을때 나머지가 0이 아니라면
        result += "%d," % i  # result 문자열에 추가
print(result[0:len(result) - 1])  # result 값에 0번부터 뒤에서 1글짜 빼고 출력하기 # result[시작점 : 끝점]
