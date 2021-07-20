#라이브러리 가져오기

import requests 
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text #요청 보내고 받은 응답 text로 변환
data = BeautifulSoup(response, 'html.parser') # 응답으로 받은 걸 처리하기 쉽게 가공 (parsing)
KOSPI = data.select_one('#KOSPI_now')
result = KOSPI.next

print(f'현재 코스피 지수는 {result}입니다.')