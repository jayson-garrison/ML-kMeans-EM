class Cluster:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def removePoint(self, x):
        self.X.remove(x)

    def addPoint(self, x):
        self.X.append(x)