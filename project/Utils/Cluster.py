class Cluster:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def removeSample(self, x):
        self.X.remove(x)

    def addSample(self, x):
        self.X.append(x)

    def clear(self):
        self.X = list()