PI = 3.14


def input_radius():
    radius_str = input("반지름을 입력하세요 : ")
    return float(radius_str)


def calc_circle_area(r):
    return PI * r * r


def calc_circumference(r):
    return 2 * PI * r


radius = input_radius()
circle_area = calc_circle_area(radius)
circumference = calc_circumference(radius)

print("원의 면적: {0:0.2F}, 원의 둘레: {1:0.2F}".format(circle_area, circumference))
