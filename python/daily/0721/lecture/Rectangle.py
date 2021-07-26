horizon = int(input())
vertical = int(input())

def rectange(horizon, vertical):
    round = 2 * horizon + 2 * vertical
    area = horizon * vertical
    return round, area

result = rectange(horizon,vertical)

print(result)