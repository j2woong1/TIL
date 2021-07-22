# 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

def sum_of_digit(number):
    # 1. 변수 초기화
    total_sum = 0
    # 2. 한자리의 경우 0/10 => 0 즉, False 가 될 때까지.
    while number / 10:
        # 3. 몫과 나머지를 분리하기
        # 아래의 코드는 number, remainder = divmod(number, 10) 으로 변경 가능하다.
        remainder = number % 10
        number = number // 10
        # 4. 나머지를 더하기
        total_sum += remainder
    return total_sum


print(sum_of_digit(1234))

# 재귀
# def sum_of_digit(number):
#     if number < 10:
#         return number
#     else:
#         number, remainder = divmod(number, 10)
#         return sum_of_digit(number) + remainder
