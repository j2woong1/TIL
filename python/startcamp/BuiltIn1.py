# SW Expert Academy 6308
# 이름과 나이를 입력 받아 올해를 기준으로 100세가 되는 해

import datetime

name = input()
t = 100 - int(input())
# 채점표가 2019년으로 되어있으므로 -1년 (현재 2021년) + 100-현재나이
year = datetime.datetime.now().year - 2 + t
print("%s(은)는 %d년에 100세가 될 것입니다." % (name, year))
