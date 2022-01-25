class Numbers:
    MULTIPLIER=5
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def add(self):
        return self.x + self.y

    def multiply(self, a):
        return self.MULTIPLIER * a
    

    def subtract(b, c):
        return b-c


    
    def value(self):
        return self.x, self.y


    
    def setX(self, value):
        self.x = value
    def deleteX(self):
        del self.x
    def setY(self, value):
        self.y = value
    def deleteY(self):
        del self.y

num = Numbers(5,6)
print(num.add())
print(num.multiply(2))
print(Numbers.subtract(3,2))
print(num.value)
num.setX(2)
num.setY(5)
print(num.value)
num.deleteX()
num.deleteY()