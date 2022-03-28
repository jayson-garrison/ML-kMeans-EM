class Kmeans():
    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.mu = None # there should be k p-dimensional mean fectors

    def learn(self):
        # get an initial estimate for the mu's

        # repeat until convergence (no point changes classification)
        #       assign class of pts based on which mu it is closest to
        #       update the mu by averaging feature vals of assigned points
        
        # save the mu's
        pass

    def paint_by_numbers(self, data):
        # for each point, assign it the value of the nearest mean vector
        # save the altered image
        # print the altered image
        pass
