class Cluster:
    def __init__(self, X=list(), y=0):
        '''
        Cluster object consisting of Sample objects with homogeneous labels (see Sample)

        @param X: the list of samples (default empty)

        @param y: the associated label of the cluster (default 0)
        '''
        self.X = X
        self.y = y

    def removeSample(self, x):
        '''
        remove a sample from the cluster

        @param x: the sample to be removed
        '''
        self.X.remove(x)

    def addSample(self, x):
        '''
        add a sample to the cluster

        @param x: the sample to be added to the cluster
        '''
        self.X.append(x)

    def getX(self):
        '''
        get the list of samples in the cluster

        @returns the list of samples in the cluster where each sample is a Sample object 'whew, OK'
        '''
        return self.X

    def getMagnitude(self):
        '''
        get the magnitude of the cluster

        @returns the cardinality of the cluster
        '''
        return len(self.X)

    def clear(self):
        '''
        clears the cluster, sets to empty
        '''
        self.X = list()