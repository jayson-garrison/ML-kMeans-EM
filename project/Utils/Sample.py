class Sample:
    def __init__(self, x, y):
        '''
        Sample object where x is a numpy array (vector) of any dimension
        with an associated label y

        @param x: the vector

        @param y: the associated label
        '''
        self.x = x
        self.y = y

    def getX(self):
        '''
        get the vector x

        @returns the x vector
        '''
        return self.x
    
    def getY(self):
        '''
        get the label

        @return the label
        '''
        return self.y

    def setY(self, y):
        '''
        set the label associated with the vector
        
        @param y: the new label
        '''
        self.y = y

    def getDim(self):
        '''
        get the dimension of the vector of this sample

        @return dim(x)
        '''
        return len(self.x)

    def __str__(self):
        return f'x:{self.x},y:{self.y}'
