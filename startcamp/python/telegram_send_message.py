import requests
from requests.models import Response

#기본 설정
TOKEN = '1775017911:AAG54qWmF5mMGyCZXpJAEVqFptnYJCl_Cm4'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

# chat_id 가져오기
# https://api.telegram.org/bot1775017911:AAG54qWmF5mMGyCZXpJAEVqFptnYJCl_Cm4/getUpdates

UPDATES_URL = f'{APP_URL}/getUpdates'
response = requests.get(UPDATES_URL).json()

chat_id = response.get('result')[0].get('message').get('chat').get('id')
print(chat_id)

text = '파이썬으로 보낸 메세지입니다.'

# https://api.telegram.org/bot1775017911:AAG54qWmF5mMGyCZXpJAEVqFptnYJCl_Cm4/sendMessage?chat_id=832967282&text=%EB%B3%B4%EB%82%B4%EC%A7%80%EB%82%98%EC%9A%94?
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)

