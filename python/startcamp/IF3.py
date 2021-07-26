# SW Expert Academy 6220
# 다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.

a = input()
if 'a' <= a <= 'z':
    print("%s 는 소문자 입니다." % a)
elif 'A' <= a <= 'Z':
    print("%s 는 대문자 입니다." % a)
