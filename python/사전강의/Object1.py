# SW Expert Academy 6203
# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

class Student:
    def __init__(self, kor, mat, eng):
        self.__kor = kor
        self.__mat = mat
        self.__eng = eng

    @property
    def kor(self):
        return self.__kor

    @property
    def mat(self):
        return self.__mat

    @property
    def eng(self):
        return self.__eng

    def grade_sum(self):
        return "국어, 영어, 수학의 총점: {0}".format(self.__kor + self.__mat + self.__eng)


data = list(map(int, input().split(', ')))
student_data = Student(data[0], data[1], data[2])
print(student_data.grade_sum())
