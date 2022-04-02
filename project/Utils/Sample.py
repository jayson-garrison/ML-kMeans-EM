class Sample:
    def __init__(self, x, y, true_label="NA"):
        self.x = x
        self.y = y
        self.true_label = true_label

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getTrueLabel(self):
        return self.true_label

    def __str__(self):
        return f'x:{self.x},y:{self.y}'