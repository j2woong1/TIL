import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def total(scores):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    plus = sum(scores) # 덧셈 변수 지정해서 sum 내장함수 처리
    return plus

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json')
    scores = json.load(scores_json)
    print(total(scores))
    # 330