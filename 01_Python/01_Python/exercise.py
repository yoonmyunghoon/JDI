class Circle:
    pi = 3.14
    x = 0
    y = 0

    def __init__(self, radius, x, y):
        self.r = radius
        self.x = x
        self.y = y
    
    def area(self):
        return self.r * self.r * self.pi
    
    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y

cy = Circle(3, 2, 4)
print(cy.area())
cy.move(2,3)
print(cy.x, cy.y)
print(cy.circumference())
print(cy.center())
