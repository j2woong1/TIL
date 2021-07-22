# 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다.
# 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 snail()을 작성하시오.

def snail(height, day, night):
    count = 0
    while True:
        count += 1
        height -= day
        if height <= 0:
            return count
        height += night
