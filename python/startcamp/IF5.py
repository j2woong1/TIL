# SW Expert Academy 6222

a = input()
if a.islower():  # 대문자일 경우 소문자로
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.upper(), ord(a.upper()))) # 아스키코드를 함께 출력
elif a.isupper():  # 소문자일 경우 대문자로
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.lower(), ord(a.lower())))
else:
    print(a)
