# SW Expert Academy 6225
# 가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
# 생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.

class Rectangle:

    def __init__(self, w, h):
        self.__width = w
        self.__height = h

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        return self.width * self.height


s1 = Rectangle(4, 5)
print("사각형의 면적: {}".format(s1.area()))
