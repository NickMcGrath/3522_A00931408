class Student:
    memes = 'meme'

    def __init__(self, name, set_, id_):
        self._name = name
        self._set_ = set_
        self._id_ = id_
        self._courses = {}

    @classmethod
    def get_memes(cls):
        return cls.memes

    def enroll(self, course, grade=0):
        self._courses[course] = grade

    def set_grade(self, course, grade):
        self._courses[course] = grade

    def __str__(self):
        return f'{self._name}, {self._set_}, {self._id_}, {self._courses}, ' \
               f'{self.memes}'

    def to_string(self):
        return self.__str__()

    def get_courses(self):
        return self._courses

    def set_courses(self, courses):
        self._courses = courses

    courses = property(get_courses, set_courses)


class ExchangeStudent(Student):
    def __init__(self, transfer_school_name, name, set_, id_):
        super().__init__(name, set_, id_)
        self._transfer_school_name = transfer_school_name

    def get_school(self):
        return self._transfer_school_name

    def set_school(self, school):
        self._transfer_school_name = school

    school = property(get_school, set_school)

    def enroll(self, course, grade=0):
        super().enroll(course, grade)
        print("hello we overrided a enroll method")

    def __str__(self):
        return f'{self._transfer_school_name}, {self._name}, {self._set_},' \
               f'{self._courses}, SUPER: {super().__str__()} '


def main():
    s1 = Student('jenny', 'c', 'a123')
    fs1 = ExchangeStudent('Exchange School in China', 'bubba', 'f', 'a001')

    print(s1)
    s1.enroll(555)
    s1.set_grade(555, 99)
    print(s1.courses)
    print(Student.memes)
    print(s1.memes)

    print(fs1)
    fs1.school = 'BCIT'
    fs1.enroll('comm', '69')
    print(fs1)


if __name__ == '__main__':
    main()
