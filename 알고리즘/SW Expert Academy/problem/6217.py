class Student:

    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

class GraduateStudent(Student):

    def __init__(self, name, major):
        Student.__init__(self, name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __str__(self):
        return ('이름: {}, 전공: {}'.format(self.name, self.__major))

a = Student('홍길동')
print('이름: {}'.format(a.name))
b = GraduateStudent('이순신', '컴퓨터')
print('이름: {}, 전공: {}'.format(b.name, b.major))


