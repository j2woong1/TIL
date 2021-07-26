import json

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over(movie):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if movie.get("user_rating") >= 8: # movie에서 get으로 평점을 가져와서 비교
        return True
    else:
        return False
    return over


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # True