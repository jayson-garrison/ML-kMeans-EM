from cmath import pi
import numpy as np
from Utils.Cluster import Cluster
class GaussianDistribution:

    def __init__(self, cluster, num_samples, k) -> None:
        '''
        Gaussian Distribution

        phi := the proportion of this distribution related to the whole sample space of points

        mu := the mean

        big_sig := the covariance

        @param points: the points in the distribution

        @param num_samples: the number of samples in the whole space (where points are a subset
        of this space)
        
        '''
        #self.num_samples = num_samples
        self.id = k
        # if div doesnt work use matmul by a scalar
        self.dim = cluster.getX()[0].getDim()
        self.cluster = cluster
        self.phi = cluster.getMagnitude() / num_samples
        self.w = list()

        total = np.zeros(self.dim)

        for point in cluster:
            np.add(total, point.getX())
        
        self.mu = np.divide(total, self.cluster.getMagnitude())
        
        cov = np.zeros((self.dim, self.dim))

        for point in cluster:
            # verify this
            var = np.divide(np.matmul(np.subtract(point.getX(), self.mu), np.matrix.transpose(np.subtract(point.getX(), self.mu))), self.cluster.getMagnitude())
            np.add(var, cov)
            
        self.big_sig = cov

    def calculate_gaussian_density(self, given_sample):
        gd = 1 / ( (2*np.pi)^(self.dim/2) * (np.abs(self.big_sig))^(.5) )
        gd = gd * np.exp( -.5 * np.matrix.transpose( (given_sample - self.mu) ) * \
                           np.linalg.inv(self.big_sig) * (given_sample * self.mu) )
                           
        return gd

    def calculate_phi(self):
        '''
        calculate the phi based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''

        #perform the calculation for phi based on the m step
        # self.points = points
        self.phi = 0

        for possibility in self.w:
            self.phi += possibility

        self.cum_w = self.phi
        self.phi / len(self.w)

    def calculate_mu(self):
        '''
        calculate the mu based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''
        
        # perform the calculate for mu based on the m step
        # self.points = points
        for idx, possibility in enumerate(self.w):
            self.mu += possibility[self.id] * self.cluster.getX()[idx].getX()

        self.mu = self.mu / self.cum_w

    def calculate_big_sig(self):
        '''
        calculate the big_sig based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''

        # perform the calculation for big sig based on the m step
        # self.points = points
        for idx, possibility in enumerate(self.w):
            self.big_sig += self.w[idx] * np.matmul( (self.cluster.getX()[idx].getX() - self.mu), \
                            np.transpose(self.cluster.getX()[idx].getX() - self.mu) )

        self.big_sig / self.cum_w

    def replace_cluster(self, new_cluster):
        self.cluster = new_cluster

    def replace_w(self, new_w):
        self.w = new_w

    def addW(self, a_w):
        self.w.append(a_w)

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