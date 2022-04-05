from sklearn.exceptions import NonBLASDotWarning


class Document():
    def __init__(self, line, nbow):
        self.line = line
        self.nbow = nbow
    
    def getLine(self):
        return self.line
    
    def getNbow(self):
        return self.nbow
