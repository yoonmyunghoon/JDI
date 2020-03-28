class Pikachu:
    name = ''
    level = 1
    hp = 0
    exp = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level*20

    def __del__(self):
        print(f'{self.name} 죽음.')
        return del self

    def bark(self):
        print('pikachu')
    
    def body_attack(self, someone):
        someone.hp = someone.hp - self.level * 5
        if someone.hp <= 0:
            someone.hp = 0
            someone.__del__()
            self.exp += someone.level * 15
            if self.exp >= self.level*100:
                while(self.level*100 < self.exp):
                    self.exp -= self.level*100
                    self.level += 1

    def thousond_volt(self, someone):
        someone.hp = someone.hp - self.level * 7
        if someone.hp <= 0:
            someone.hp = 0
            someone.__del__()
            self.exp += someone.level * 15
            if self.exp >= self.level*100:
                while(self.level*100 < self.exp):
                    self.exp -= self.level*100
                    self.level += 1


first = Pikachu('첫번째놈', 1)
two = Pikachu('두번째놈', 30)
while(two.hp != 0):
    first.body_attack(two)
print(two.hp)
print(first.level)
print(first.exp)
print(two)