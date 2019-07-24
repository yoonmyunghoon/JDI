class Person:
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

a = Male()
print(a.getGender())
b = Female()
print(b.getGender())
