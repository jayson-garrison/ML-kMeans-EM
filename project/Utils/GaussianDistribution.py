from cmath import pi
import numpy as np
class GaussianDistribution:

    def __init__(self, points, num_samples) -> None:
        '''
        Gaussian Distribution

        phi := the proportion of this distribution related to the whole sample space of points

        mu := the mean

        big_sig := the covariance

        @param points: the points in the distribution

        @param num_samples: the number of samples in the whole space (where points are a subset
        of this space)
        
        '''
        # if div doesnt work use matmul by a scalar
        self.dim = len(points[0])
        self.points = points
        self.phi = len(points) / num_samples

        total = np.zeros(len(points[0]))

        for point in points:
            np.add(total, point)
        
        self.mu = np.divide(total, len(points[0]))
        
        cov = np.zeros((len(points[0]),len(points[0])))

        for point in points:
            var = np.divide(np.matmul(np.subtract(point, self.mu), np.matrix.transpose(np.subtract(point, self.mu))), len(points[0]))
            np.add(var, cov)
            
        self.big_sig = cov

    def calculate_gaussian_density(self):
        gd = 1 / ( (2*np.pi)^(n/2) * )
        pass

    def calculate_phi(self, points):
        '''
        calculate the phi based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''

        #perform the calculation for phi based on the m step
        self.points = points
        self.phi = -1
        pass

    def calculate_mu(self, points):
        '''
        calculate the mu based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''
        
        # perform the calculate for mu based on the m step
        self.points = points
        self.mu = -1

    def calculate_big_sig(self, points):
        '''
        calculate the big_sig based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''

        # perform the calculation for big sig based on the m step
        self.points = points
        self.big_sig = -1

    def getPhi(self):
        '''
        @returns the phi of the distribution
        '''
        return self.phi

    def getMu(self):
        '''
        @returns the mu of the distribution
        '''
        return self.mu

    def getBigSig(self):
        '''
        @returns the big_sig of the distribution
        '''
        return self.big_sig