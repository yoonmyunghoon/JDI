class Shape:
    def area(self):
        return 0


class Square(Shape):
    def area(self, length):
        return length * length

a = Square()
print('정사각형의 면적: {}'.format(a.area(3)))
